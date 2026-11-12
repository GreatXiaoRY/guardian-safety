#!/usr/bin/env python3
"""Check Markdown links and essential Guardian project structure."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "references/core/safety-principles.md",
    "references/core/risk-assessment.md",
    "references/core/emergency-protocol.md",
    "references/core/capability-detection.md",
    "references/core/privacy-and-consent.md",
    "references/scenarios/pre-incident-planning.md",
    "references/scenarios/vehicle-accident.md",
    "references/scenarios/personal-threat.md",
    "references/scenarios/abduction-and-confinement.md",
    "references/scenarios/arrest-and-detention.md",
    "references/scenarios/medical-emergency.md",
    "references/scenarios/post-incident.md",
    "references/evidence/evidence-preservation.md",
    "references/evidence/audio-video-recording.md",
    "references/evidence/location-recording.md",
    "references/evidence/chain-of-custody.md",
    "references/legal/legal-information-boundaries.md",
    "references/legal/finding-legal-assistance.md",
    "references/legal/jurisdiction-guide.md",
    "references/integrations/tool-capability-contract.md",
    "references/integrations/integration-safety.md",
    "assets/emergency-message-template.md",
    "assets/personal-safety-plan.md",
    "assets/incident-report-template.md",
    "docs/SAFETY-CASE.md",
]

SCENARIO_FILES = [
    "pre-incident-planning.md",
    "vehicle-accident.md",
    "personal-threat.md",
    "abduction-and-confinement.md",
    "arrest-and-detention.md",
    "medical-emergency.md",
    "post-incident.md",
]
SCENARIO_HEADINGS = [
    "Scope",
    "Risk Indicators",
    "Immediate Priorities",
    "Response Workflow",
    "Communication",
    "Evidence Preservation",
    "Legal Considerations",
    "Tool Requirements",
    "Fallback Procedures",
    "Completion Criteria",
]
CASE_ID = re.compile(r"\|\s*((?:ACT|EMG|SAF|CAP|VEH|ABD|DET|NET|TOOL)-\d+)\s*\|")


def main() -> int:
    errors = []
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.exists():
        skill = skill_path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", skill, re.DOTALL)
        if not frontmatter:
            errors.append("SKILL.md has missing or malformed frontmatter")
        else:
            fields = {}
            malformed = False
            for line in frontmatter.group(1).splitlines():
                if not line.strip():
                    continue
                if ":" not in line:
                    malformed = True
                    break
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
            if malformed or fields.get("name") != "guardian-safety" or not fields.get("description"):
                errors.append("SKILL.md frontmatter must define name=guardian-safety and a description")
        if len(skill.splitlines()) > 500:
            errors.append("SKILL.md exceeds the 500-line project limit")

    for filename in SCENARIO_FILES:
        path = ROOT / "references" / "scenarios" / filename
        if not path.is_file():
            continue
        headings = {
            match.group(1).strip()
            for match in re.finditer(r"^##\s+(.+?)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        }
        missing = [heading for heading in SCENARIO_HEADINGS if heading not in headings]
        if missing:
            errors.append(f"scenario {filename} is missing headings: {', '.join(missing)}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            if not (path.parent / local).resolve().is_file():
                errors.append(f"broken Markdown link: {path.relative_to(ROOT)} -> {target}")

    case_paths = {}
    for path in (ROOT / "tests").rglob("*.md"):
        if path.name == "README.md":
            continue
        for case_id in CASE_ID.findall(path.read_text(encoding="utf-8")):
            case_paths.setdefault(case_id, []).append(path.relative_to(ROOT))
    duplicates = {case_id: paths for case_id, paths in case_paths.items() if len(paths) > 1}
    if duplicates:
        for case_id, paths in sorted(duplicates.items()):
            errors.append(f"duplicate test case {case_id}: {', '.join(map(str, paths))}")
    cases = len(case_paths)
    if cases < 20:
        errors.append(f"found only {cases} unique test cases; at least 20 are required")

    if errors:
        print("Guardian checks failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(
        "Guardian checks passed: required files, Markdown links, frontmatter, "
        f"scenario headings, and {cases} unique test cases."
    )
    print("Note: behavior cases require manual execution in a compatible AI Agent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
