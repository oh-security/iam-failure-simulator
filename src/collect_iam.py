import boto3
from typing import Any, Dict, List, Optional
from .models import Principal


def collect_role(iam, role_name: str) -> Principal:
    role = iam.get_role(RoleName=role_name)["Role"]
    trust = role.get("AssumeRolePolicyDocument")
    policies: List[Dict[str, Any]] = []

    attached = iam.list_attached_role_policies(RoleName=role_name).get(
        "AttachedPolicies", []
    )
    for ap in attached:
        policies.append(
            {
                "type": "managed",
                "policy_name": ap["PolicyName"],
                "policy_arn": ap["PolicyArn"],
            }
        )

    inline_names = iam.list_role_policies(RoleName=role_name).get("PolicyNames", [])
    for name in inline_names:
        doc = iam.get_role_policy(
            RoleName=role_name, PolicyName=name
        )["PolicyDocument"]
        policies.append({"type": "inline", "policy_name": name, "document": doc})

    return Principal(
        principal_type="Role",
        name=role_name,
        arn=role["Arn"],
        trust_policy=trust,
        policies=policies,
    )


def collect_user(iam, user_name: str) -> Principal:
    user = iam.get_user(UserName=user_name)["User"]
    policies: List[Dict[str, Any]] = []
    access_keys: List[Dict[str, Any]] = []

    keys = iam.list_access_keys(UserName=user_name)["AccessKeyMetadata"]
    for k in keys:
        last_used = iam.get_access_key_last_used(
            AccessKeyId=k["AccessKeyId"]
        ).get("AccessKeyLastUsed", {})
        access_keys.append(
            {
                "access_key_id": k["AccessKeyId"],
                "status": k["Status"],
                "create_date": k["CreateDate"].isoformat(),
                "last_used": last_used,
            }
        )

    attached = iam.list_attached_user_policies(UserName=user_name).get(
        "AttachedPolicies", []
    )
    for ap in attached:
        policies.append(
            {
                "type": "managed",
                "policy_name": ap["PolicyName"],
                "policy_arn": ap["PolicyArn"],
            }
        )

    inline_names = iam.list_user_policies(UserName=user_name).get("PolicyNames", [])
    for name in inline_names:
        doc = iam.get_user_policy(
            UserName=user_name, PolicyName=name
        )["PolicyDocument"]
        policies.append({"type": "inline", "policy_name": name, "document": doc})

    return Principal(
        principal_type="User",
        name=user_name,
        arn=user["Arn"],
        policies=policies,
        access_keys=access_keys,
    )


def collect_principals(
    target: Optional[str], include_users: bool, include_roles: bool
) -> List[Principal]:
    iam = boto3.client("iam")
    principals: List[Principal] = []

    if target:
        kind, name = target.split(":", 1)
        if kind == "role":
            principals.append(collect_role(iam, name))
        elif kind == "user":
            principals.append(collect_user(iam, name))
        return principals

    if include_roles:
        for r in iam.list_roles()["Roles"]:
            principals.append(collect_role(iam, r["RoleName"]))

    if include_users:
        for u in iam.list_users()["Users"]:
            principals.append(collect_user(iam, u["UserName"]))

    return principals
