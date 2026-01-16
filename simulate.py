import argparse
import json

from src.collect_iam import collect_principals
from src.collect_cloudtrail import lookup_events
from src.simulator import simulate


def main():
    parser = argparse.ArgumentParser(description="IAM Failure Simulator")
    parser.add_argument("--target", help="role:NAME or user:NAME (optional)")
    parser.add_argument("--users", action="store_true", help="Include IAM users")
    parser.add_argument("--roles", action="store_true", help="Include IAM roles")
    parser.add_argument("--days", type=int, default=30, help="CloudTrail lookback days")
    parser.add_argument("--rules", default="rules/scenarios.yml", help="Scenario rules file")
    parser.add_argument("--out", help="Output file (JSON)")
    args = parser.parse_args()

    include_roles = args.roles or (not args.roles and not args.users)
    include_users = args.users

    principals = collect_principals(
        target=args.target,
        include_users=include_users,
        include_roles=include_roles,
    )

    cloudtrail_events = lookup_events(days_back=args.days)

    findings = simulate(
        principals=principals,
        cloudtrail_events=cloudtrail_events,
        rules_path=args.rules,
    )

    output = [f.__dict__ for f in findings]
    text = json.dumps(output, ensure_ascii=False, indent=2)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
