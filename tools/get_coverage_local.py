import sys
import xml.etree.ElementTree as ET
from pathlib import Path

p = Path("target/site/jacoco/jacoco.xml")
if not p.exists():
    print("Coverage file not found. Run run_tests() first to generate JaCoCo report.")
    sys.exit(0)

try:
    tree = ET.parse(p)
    root = tree.getroot()
    counter = root.find(".//counter[@type='LINE']")
    if counter is None:
        print("No LINE counter found in JaCoCo report.")
        sys.exit(0)

    covered = int(counter.attrib.get("covered", "0"))
    missed = int(counter.attrib.get("missed", "0"))
    total = covered + missed if covered + missed > 0 else 1
    pct = round(covered * 100.0 / total, 2)

    print(f"Line coverage: {pct}% ({covered} covered / {missed} missed, total {total})")
except Exception as e:
    print(f"Error parsing JaCoCo report: {e}")
