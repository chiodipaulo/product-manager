import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_eval_ids_are_stable_and_unique(self):
        data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        ids = [case["id"] for case in data["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(
            set(ids),
            {
                "rice_missing_inputs",
                "positioning_missing_competitor",
                "prd_sparse_context",
                "ai_feature_launch",
                "simple_reversible_decision",
                "decision_tradeoff",
            },
        )


if __name__ == "__main__":
    unittest.main()
