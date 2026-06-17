import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run_script(name, *args):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / name), *map(str, args)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


class ScriptTests(unittest.TestCase):
    def test_check_skill_structure_accepts_project_root(self):
        result = run_script("check_skill_structure.py", ROOT)

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("PASS", result.stdout)

    def test_check_skill_structure_reports_missing_required_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: temp\ndescription: temp\n---\n# Temp\n",
                encoding="utf-8",
            )

            result = run_script("check_skill_structure.py", skill_dir)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("references", result.stdout)
        self.assertIn("assets", result.stdout)

    def test_inspect_skill_package_classifies_files_and_detects_tests(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample\ndescription: sample skill\n---\n# Sample\n",
                encoding="utf-8",
            )
            (skill_dir / "references").mkdir()
            (skill_dir / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (skill_dir / "assets").mkdir()
            (skill_dir / "assets" / "template.md").write_text("# Template\n", encoding="utf-8")
            (skill_dir / "scripts").mkdir()
            (skill_dir / "scripts" / "tool.py").write_text("print('ok')\n", encoding="utf-8")
            (skill_dir / "tests").mkdir()
            (skill_dir / "pyproject.toml").write_text("[tool.pytest.ini_options]\n", encoding="utf-8")

            result = run_script("inspect_skill_package.py", skill_dir)

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["root_type"], "skill_package")
        self.assertIn("SKILL.md", payload["files"]["entrypoints"])
        self.assertIn("references/guide.md", payload["files"]["references"])
        self.assertIn("assets/template.md", payload["files"]["assets"])
        self.assertIn("scripts/tool.py", payload["files"]["scripts"])
        self.assertIn("python -m pytest", payload["validation"]["candidate_commands"])

    def test_inspect_skill_package_ignores_python_cache_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample\ndescription: sample skill\n---\n# Sample\n",
                encoding="utf-8",
            )
            (skill_dir / "tests" / "__pycache__").mkdir(parents=True)
            (skill_dir / "tests" / "__pycache__" / "test.cpython-311.pyc").write_bytes(b"cache")
            (skill_dir / "tests" / "test_real.py").write_text("def test_real(): pass\n", encoding="utf-8")

            result = run_script("inspect_skill_package.py", skill_dir)

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["files"]["tests"], ["tests/test_real.py"])

    def test_inspect_skill_package_treats_scripts_as_optional(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample\ndescription: sample skill\n---\n# Sample\n",
                encoding="utf-8",
            )
            (skill_dir / "references").mkdir()
            (skill_dir / "assets").mkdir()

            result = run_script("inspect_skill_package.py", skill_dir)

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertNotIn("scripts", payload["missing"])
        self.assertFalse(payload["validation"]["script_validation_needed"])

    def test_validate_patch_yaml_accepts_template(self):
        result = run_script("validate_patch_yaml.py", ROOT / "assets" / "candidate-patch-template.yaml")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("PASS", result.stdout)

    def test_validate_patch_yaml_rejects_script_patch_without_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            patch_file = Path(tmp) / "patch.yaml"
            patch_file.write_text(
                """patches:
  - id: PATCH-001
    file: "scripts/tool.py"
    op: "replace_block"
    target_text: "old"
    rationale: "Fix script behavior."
    risk: "Could break execution."
    content: |
      print("new")
""",
                encoding="utf-8",
            )

            result = run_script("validate_patch_yaml.py", patch_file)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("script patch requires validation", result.stdout)

    def test_scripts_support_help_smoke_tests(self):
        for name in [
            "check_skill_structure.py",
            "inspect_skill_package.py",
            "validate_patch_yaml.py",
        ]:
            with self.subTest(name=name):
                result = run_script(name, "--help")
                self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
                self.assertIn("usage:", result.stdout)

    def test_templates_require_versioned_candidate_sessions(self):
        training_log = (ROOT / "assets" / "training-log-template.md").read_text(encoding="utf-8")
        workflow = (ROOT / "references" / "training-workflow.md").read_text(encoding="utf-8")

        self.assertIn("base_version:", training_log)
        self.assertIn("candidate_version:", training_log)
        self.assertIn("session_id:", training_log)
        self.assertIn(".anxi/candidates/<session_id>/", workflow)
        rubric = (ROOT / "references" / "acceptance-rubric.md").read_text(encoding="utf-8")
        self.assertIn("UTF-8 BOM", rubric)
        self.assertIn("line-ending-only noise", rubric)


if __name__ == "__main__":
    unittest.main()
