import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sample_pr.json")


def load_pr_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


class CodeUnderstandingAgent:
    name = "Code Understanding Agent"

    def review(self, pr_data):
        important_files = []
        behavior_summary = []

        for changed_file in pr_data["changed_files"]:
            important_files.append(changed_file["path"])

            if changed_file["area"] == "controller":
                behavior_summary.append(
                    f"{changed_file['path']} updates request handling."
                )
            elif changed_file["area"] == "service":
                behavior_summary.append(
                    f"{changed_file['path']} contains the main business rule change."
                )
            elif changed_file["area"] == "tests":
                behavior_summary.append(
                    f"{changed_file['path']} updates automated test coverage."
                )

        return {
            "agent": self.name,
            "important_files": important_files,
            "behavior_summary": behavior_summary,
            "conclusion": "The PR mainly adds duplicate-title validation to the create-book flow."
        }


class StyleQualityAgent:
    name = "Style and Quality Agent"

    def review(self, pr_data):
        findings = []

        for changed_file in pr_data["changed_files"]:
            if changed_file["area"] == "controller":
                findings.append(
                    f"Check whether {changed_file['path']} is holding business logic that should stay in the service layer."
                )

            for note in changed_file["notes"]:
                if "controller" in note.lower() or "business logic" in note.lower():
                    findings.append(note)

        if not findings:
            findings.append("No major style or maintainability concerns found.")

        return {
            "agent": self.name,
            "findings": findings,
            "conclusion": "Most quality attention should go to separation of concerns."
        }


class TestRiskAgent:
    name = "Test and Risk Agent"

    def review(self, pr_data):
        findings = []
        risks = []

        for changed_file in pr_data["changed_files"]:
            if changed_file["area"] == "tests":
                findings.append(f"Tests were updated in {changed_file['path']}.")

            for note in changed_file["notes"]:
                if "No update-book duplicate-title test yet" in note:
                    risks.append(
                        "There may be a missing duplicate-title test for update-book behavior."
                    )

        if not findings:
            findings.append("No direct test file changes detected.")

        if not risks:
            risks.append("No major regression risk identified from the sample data.")

        return {
            "agent": self.name,
            "findings": findings,
            "risks": risks,
            "conclusion": "Test coverage improved, but there may still be one missing edge case."
        }


class CoordinatorAgent:
    name = "Coordinator Agent"

    def __init__(self):
        self.code_agent = CodeUnderstandingAgent()
        self.style_agent = StyleQualityAgent()
        self.test_agent = TestRiskAgent()

    def run(self, pr_data):
        print(f"\n{self.name}: Received PR review task")
        print(f"Title: {pr_data['title']}")
        print(f"Summary: {pr_data['summary']}")

        print(f"\n{self.name} -> {self.code_agent.name}")
        code_result = self.code_agent.review(pr_data)

        print(f"{self.name} -> {self.style_agent.name}")
        style_result = self.style_agent.review(pr_data)

        print(f"{self.name} -> {self.test_agent.name}")
        test_result = self.test_agent.review(pr_data)

        print(f"\n{self.name}: Collecting outputs from specialist agents")
        final_report = self.merge_results(code_result, style_result, test_result)

        return final_report

    def merge_results(self, code_result, style_result, test_result):
        report_lines = []
        report_lines.append("FINAL MULTI-AGENT REVIEW REPORT")
        report_lines.append("=" * 40)

        report_lines.append("\n1. Code Understanding")
        for line in code_result["behavior_summary"]:
            report_lines.append(f"- {line}")
        report_lines.append(f"- Conclusion: {code_result['conclusion']}")

        report_lines.append("\n2. Style and Quality")
        for finding in style_result["findings"]:
            report_lines.append(f"- {finding}")
        report_lines.append(f"- Conclusion: {style_result['conclusion']}")

        report_lines.append("\n3. Test and Risk")
        for finding in test_result["findings"]:
            report_lines.append(f"- {finding}")
        for risk in test_result["risks"]:
            report_lines.append(f"- Risk: {risk}")
        report_lines.append(f"- Conclusion: {test_result['conclusion']}")

        report_lines.append("\n4. Final Coordinator Decision")
        report_lines.append(
            "- This PR is a good example of why multi-agent review helps:"
        )
        report_lines.append(
            "- one agent explains behavior, one checks quality, and one checks tests and risks."
        )

        return "\n".join(report_lines)


def main():
    pr_data = load_pr_data()
    coordinator = CoordinatorAgent()
    final_report = coordinator.run(pr_data)

    print("\n" + final_report)


if __name__ == "__main__":
    main()