from typing import Any, Dict, List, Set


def _to_list(x):
    if isinstance(x, list):
        return x
    if x is None:
        return []
    return [x]


def extract_actions(policy_doc: Dict[str, Any]) -> Set[str]:
    actions: Set[str] = set()
    statements = policy_doc.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]

    for st in statements:
        if st.get("Effect") != "Allow":
            continue
        for act in _to_list(st.get("Action")):
            actions.add(act)
    return actions


def has_wildcard_admin(policy_doc: Dict[str, Any]) -> bool:
    statements = policy_doc.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]

    for st in statements:
        if st.get("Effect") != "Allow":
            continue
        actions = _to_list(st.get("Action"))
        resources = _to_list(st.get("Resource"))
        if "*" in actions and "*" in resources:
            return True
    return False


def evaluate_policies(policies: List[Dict[str, Any]]) -> Dict[str, Any]:
    actions: Set[str] = set()
    wildcard_admin = False

    for p in policies:
        if p["type"] == "inline":
            doc = p["document"]
            actions |= extract_actions(doc)
            wildcard_admin = wildcard_admin or has_wildcard_admin(doc)

    return {
        "actions": actions,
        "wildcard_admin": wildcard_admin,
    }
