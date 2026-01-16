import yaml
from typing import Any, Dict, List

from .models import Finding, Principal
from .policy_eval import evaluate_policies


def trust_is_broad(trust_policy: Dict[str, Any]) -> bool:
    if not trust_policy:
        return False
    statements = trust_policy.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]
    for st in statements:
        principal = st.get("Principal")
        if principal == "*" or (isinstance(principal, dict) and "*" in str(principal)):
            return True
    return False


def simulate(
    principals: List[Principal],
    cloudtrail_events: List[Dict[str, Any]],
    rules_path: str,
) -> List[Finding]:
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = yaml.safe_load(f)

    findings: List[Finding] = []

    for pr in principals:
        perm = evaluate_policies(pr.policies)

        ctx = {
            "has_access_keys": len(pr.access_keys) > 0,
            "trust_is_broad": trust_is_broad(pr.trust_policy),
            "perm_actions": perm["actions"],
            "perm_has_wildcard_admin": perm["wildcard_admin"],
        }

        for sc in rules.get("scenarios", []):
            triggered = False
            evidence: Dict[str, Any] = {}

            for trig in sc.get("risk_triggers", {}).get("any", []):
                if "perm_has_wildcard_admin" in trig and ctx["perm_has_wildcard_admin"]:
                    triggered = True
                    evidence["wildcard_admin"] = True
                if "perm_contains_actions" in trig:
                    if set(trig["perm_contains_actions"]) & ctx["perm_actions"]:
                        triggered = True
                        evidence["actions"] = list(
                            set(trig["perm_contains_actions"]) & ctx["perm_actions"]
                        )

            if not triggered:
                continue

            findings.append(
                Finding(
                    scenario_id=sc["id"],
                    title=sc["title"],
                    principal={
                        "type": pr.principal_type,
                        "name": pr.name,
                        "arn": pr.arn,
                    },
                    severity="HIGH" if ctx["perm_has_wildcard_admin"] else "MEDIUM",
                    evidence=evidence,
                    timeline=sc.get("timeline", []),
                    preventable_points=sc.get("preventable_points", []),
                    notes=["Simulation based on current IAM state"],
                )
            )

    return findings
