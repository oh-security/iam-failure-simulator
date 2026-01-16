# IAM Failure Simulator

> Simulating how IAM misconfigurations realistically evolve into security incidents — and how they could have been prevented.

---

## What this tool does

**IAM Failure Simulator** is a security analysis tool that models how IAM misconfigurations can turn into real-world security incidents **over time**.

Instead of only flagging risky permissions, this tool:
- Simulates **incident timelines**
- Explains **why each step was possible**
- Highlights **decision points where incidents could have been prevented**

The goal is not just detection, but **explainable security decision support**.

---

## Why this matters

Many IAM-related incidents are not caused by a lack of security tools, but by:
- Temporary workarounds becoming permanent
- Overly broad permissions added under time pressure
- Risks being technically detected but not *understood*

As a former sales professional, I repeatedly saw how security risks fail to translate into actionable decisions.

This project was built to bridge that gap:
**turning IAM configurations into incident stories that decision-makers can actually understand.**

---

## How it works (high level)

1. **Collects real AWS data** using boto3  
   - IAM Users / Roles
   - Inline and attached policies
   - Trust policies (AssumeRole)
   - CloudTrail events (contextual signals)

2. **Evaluates effective permissions**
   - Identifies over-privileged actions
   - Detects broad trust boundaries
   - Highlights escalation capabilities

3. **Simulates incident scenarios**
   - CI/CD credential leakage
   - Lateral movement via AssumeRole
   - Privilege escalation through IAM policy manipulation
   - Audit log disabling

4. **Outputs explainable findings**
   - Timeline of how the incident unfolds
   - Evidence tied to actual permissions
   - Clear prevention points

---

## Example scenario (simplified)

```text
Day 0:
  CI/CD role created with broad permissions (temporary workaround)

Day 30:
  No review or permission reduction performed

Day 45:
  Access key leaked from automation logs

Day 46:
  Attacker escalates privileges via IAM

Day 47:
  Audit logging disabled

## Sample output

```json
{
  "scenario_id": "CICD_KEY_LEAK",
  "severity": "HIGH",
  "principal": {
    "type": "Role",
    "name": "ci-cd-role"
  },
  "timeline": [
    {"day": 0, "event": "Automation principal exists with long-lived credentials"},
    {"day": 45, "event": "Access key is leaked"},
    {"day": 46, "event": "Privilege escalation and persistence"}
  ],
  "preventable_points": [
    "Use short-lived credentials (STS)",
    "Restrict IAM write permissions"
  ]
}

Intended audience

This tool is designed for:

Security Engineers

Cloud / Platform Engineers

Solutions Architects

Technical Sales & Security Advisors

Especially those responsible for explaining risk, not just detecting it.

Philosophy

Most security tools answer "Is this risky?"
This tool answers "How did this become an incident?"

Security improves when risks are understood, not just reported.

Disclaimer

This tool does not execute attacks

All incident timelines are simulated

Findings are intended for educational and preventive analysis

日本語概要（簡易）

IAM Failure Simulator は、AWS IAM の設定ミスが
「どのような意思決定の積み重ねで事故に発展するか」を
時系列で説明するセキュリティ分析ツールです。

検知だけでなく、

なぜ起きたのか

どこで防げたのか
を可視化することを目的としています。
