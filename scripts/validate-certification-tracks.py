#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "certifications/CERTIFICATION_INDEX.md",
    "certifications/README.md",
    "certifications/PORTFOLIO_READINESS.md",

    "certifications/ex280/README.md",
    "certifications/ex280/PREPARATION.md",
    "certifications/ex280/CHECKLIST.md",
    "certifications/ex280/LABS.md",
    "certifications/ex280/STATUS.md",
    "certifications/ex280/track/labs/lab17-capstone-examblanc.md",

    "certifications/ex288_real_final_repo_enriched/README.md",
    "certifications/ex288_real_final_repo_enriched/PREPARATION.md",
    "certifications/ex288_real_final_repo_enriched/CHECKLIST.md",
    "certifications/ex288_real_final_repo_enriched/LABS.md",
    "certifications/ex288_real_final_repo_enriched/STATUS.md",
    "certifications/ex288_real_final_repo_enriched/track/09-mock-exams/09A-mock-exam-core-build-config/README.md",

    "certifications/ex370/README.md",
    "certifications/ex370/PREPARATION.md",
    "certifications/ex370/CHECKLIST.md",
    "certifications/ex370/LABS.md",
    "certifications/ex370/STATUS.md",
    "certifications/ex370/book-v1/labs/09-mock-exam-ex370/scenario.md",

    "certifications/ex380/README.md",
    "certifications/ex380/PREPARATION.md",
    "certifications/ex380/CHECKLIST.md",
    "certifications/ex380/LABS.md",
    "certifications/ex380/STATUS.md",
    "certifications/ex380/EVIDENCE_PLAN.md",
    "certifications/ex380/READINESS.md",
    "certifications/ex380/book-v1/08-exam-scenarios/scenario-01-full-stack-dr.md",
    "certifications/ex380/book-v1/08-exam-scenarios/scenario-02-cluster-partitioning.md",
    "certifications/ex380/book-v1/08-exam-scenarios/scenario-03-gitops-end-to-end.md",
    "certifications/ex380/book-v1/08-exam-scenarios/scenario-04-observability-incident.md",

    "certifications/ex480/track/README.md",
    "certifications/ex480/track/labs/lab01-acm-intro.md",
    "certifications/ex480/track/labs/lab02-policies-placement.md",

    "certifications/ex482/README.md",
    "certifications/ex482/PREPARATION.md",
    "certifications/ex482/CHECKLIST.md",
    "certifications/ex482/LABS.md",
]

missing = [p for p in required if not (ROOT / p).is_file()]
if missing:
    print("Missing certification assets:")
    for p in missing:
        print(f" - {p}")
    sys.exit(1)

index = (ROOT / "certifications/CERTIFICATION_INDEX.md").read_text(encoding="utf-8")
for label in ("EX280", "EX288", "EX370", "EX380", "EX480", "EX482"):
    if label not in index:
        print(f"Certification index missing {label}")
        sys.exit(1)

truth = (ROOT / "certifications/README.md").read_text(encoding="utf-8").lower()
for phrase in ("does not mean", "official", "runtime"):
    if phrase not in truth:
        print(f"Truth-boundary wording missing keyword: {phrase}")
        sys.exit(1)

print("CERTIFICATION_TRACK_STRUCTURE_PASS")
