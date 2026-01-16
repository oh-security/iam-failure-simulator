from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Principal:
    principal_type: str  # "Role" or "User"
    name: str
    arn: str
    trust_policy: Optional[Dict[str, Any]] = None
    policies: List[Dict[str, Any]] = field(default_factory=list)
    access_keys: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class Finding:
    scenario_id: str
    title: str
    principal: Dict[str, str]
    severity: str
    evidence: Dict[str, Any]
    timeline: List[Dict[str, Any]]
    preventable_points: List[str]
    notes: List[str] = field(default_factory=list)
