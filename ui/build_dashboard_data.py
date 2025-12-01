from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


def count_scenarios(feature_files: list[Path]) -> int:
    scenario_pattern = re.compile(r"^\s*Scenario:", re.IGNORECASE)
    total = 0
    for file_path in feature_files:
        if not file_path.exists():
            continue
        for line in file_path.read_text(encoding="utf-8").splitlines():
            if scenario_pattern.match(line):
                total += 1
    return total


def read_last_run_summary(summary_file: Path) -> tuple[str, int | None, int | None]:
    if not summary_file.exists():
        return ("BİLİNMİYOR", None, None)

    try:
        summary = json.loads(summary_file.read_text(encoding="utf-8"))
        pass_count = (
            summary.get("passCount")
            or summary.get("passed")
            or summary.get("pass", summary.get("passes"))
        )
        fail_count = (
            summary.get("failCount")
            or summary.get("failed")
            or summary.get("fail", summary.get("failures"))
        )

        status = "PASS"
        if fail_count:
            status = "FAIL"
        elif not pass_count:
            status = "BİLİNMİYOR"

        return (status, pass_count, fail_count)
    except json.JSONDecodeError:
        return ("BİLİNMİYOR", None, None)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    karate_root = repo_root / "karate-project"
    feature_dir = karate_root / "src" / "test" / "resources" / "features"

    manual_features = sorted(feature_dir.glob("manual_*.feature"))
    ai_feature = feature_dir / "ai_generated_scenarios.feature"

    manual_count = count_scenarios(manual_features)
    ai_count = count_scenarios([ai_feature]) if ai_feature.exists() else 0

    summary_file = (
        karate_root / "target" / "karate-reports" / "karate-summary-json.txt"
    )
    status, pass_count, fail_count = read_last_run_summary(summary_file)

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "manualScenarioCount": manual_count,
        "aiScenarioCount": ai_count,
        "lastRun": {
            "status": status,
            "passCount": pass_count,
            "failCount": fail_count,
        },
    }

    out_file = Path(__file__).with_name("dashboard-data.json")
    out_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Dashboard verisi güncellendi: {out_file}")


if __name__ == "__main__":
    main()

