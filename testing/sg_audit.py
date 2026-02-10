import argparse
import csv
import json
import sys
from typing import List, Dict, Any

RISKY_PORTS = {22: "SSH", 3389: "RDP"}
PUBLIC_CIDRS = {"0.0.0.0/0", "::/0"}


def load_groups(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of security groups")
    return data


def find_findings(groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings = []
    for sg in groups:
        gid = sg.get("GroupId", "unknown")
        gname = sg.get("GroupName", "unknown")
        perms = sg.get("IpPermissions", [])
        for perm in perms:
            from_port = perm.get("FromPort")
            to_port = perm.get("ToPort")
            proto = perm.get("IpProtocol")
            ip_ranges = perm.get("IpRanges", [])
            for ipr in ip_ranges:
                cidr = ipr.get("CidrIp")
                if cidr in PUBLIC_CIDRS and from_port in RISKY_PORTS:
                    findings.append(
                        {
                            "GroupId": gid,
                            "GroupName": gname,
                            "Protocol": proto,
                            "FromPort": from_port,
                            "ToPort": to_port,
                            "Cidr": cidr,
                            "Risk": RISKY_PORTS.get(from_port, "RISKY"),
                        }
                    )
    return findings


def print_table(findings: List[Dict[str, Any]]) -> None:
    if not findings:
        print("No risky public rules found.")
        return
    headers = ["GroupId", "GroupName", "Protocol", "FromPort", "ToPort", "Cidr", "Risk"]
    widths = {h: len(h) for h in headers}
    for row in findings:
        for h in headers:
            widths[h] = max(widths[h], len(str(row[h])))
    print(" | ".join(h.ljust(widths[h]) for h in headers))
    print("-+-".join("-" * widths[h] for h in headers))
    for row in findings:
        print(" | ".join(str(row[h]).ljust(widths[h]) for h in headers))


def write_csv(findings: List[Dict[str, Any]], path: str) -> None:
    headers = ["GroupId", "GroupName", "Protocol", "FromPort", "ToPort", "Cidr", "Risk"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in findings:
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit security groups for risky public rules")
    parser.add_argument("input", help="Path to JSON file of security groups")
    parser.add_argument("--csv", help="Optional path to write findings as CSV")
    args = parser.parse_args()

    try:
        groups = load_groups(args.input)
        findings = find_findings(groups)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print_table(findings)

    if args.csv:
        write_csv(findings, args.csv)
        print(f"\nWrote CSV: {args.csv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
