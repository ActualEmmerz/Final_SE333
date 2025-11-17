import os
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP(name="SE333TestingAgent")

@mcp.tool
def run_tests() -> str:
    try:
        result = subprocess.run(
            ["mvn", "test"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        return result.stdout
    except Exception as e:
        return f"Error running mvn test: {e}"


@mcp.tool
def get_coverage() -> str:
    path = Path("target/site/jacoco/jacoco.xml")
    if not path.exists():
        return "Coverage file not found. Run run_tests() first to generate JaCoCo report."

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        counter = root.find(".//counter[@type='LINE']")
        if counter is None:
            return "No LINE counter found in JaCoCo report."

        covered = int(counter.attrib.get("covered", "0"))
        missed = int(counter.attrib.get("missed", "0"))
        total = covered + missed if covered + missed > 0 else 1
        pct = round(covered * 100.0 / total, 2)

        return f"Line coverage: {pct}% ({covered} covered / {missed} missed, total {total})"
    except Exception as e:
        return f"Error parsing JaCoCo report: {e}"


@mcp.tool
def generate_test(class_name: str, method_name: str) -> str:
    test_dir = Path("src/test/java/generated")
    test_dir.mkdir(parents=True, exist_ok=True)

    file_path = test_dir / f"{class_name}GeneratedTest.java"

    content = f"""import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang3.{class_name};

public class {class_name}GeneratedTest {{

    @Test
    public void test_{method_name}() {{
        // Call org.apache.commons.lang3.{class_name}.{method_name} with
        // appropriate parameters and add meaningful assertions.
        assertTrue(true);
    }}

}}
"""

    file_path.write_text(content, encoding="UTF-8")
    return f"Generated test at {file_path}"


@mcp.tool
def git_status() -> str:
    return subprocess.getoutput("git status")


@mcp.tool
def git_add_all() -> str:
    return subprocess.getoutput("git add -A")


@mcp.tool
def git_commit(message: str) -> str:
    cmd = f'git commit -m "{message}"'
    return subprocess.getoutput(cmd)


@mcp.tool
def git_push(remote: str = "origin", branch: str = "main") -> str:
    cmd = f"git push --set-upstream {remote} {branch}"
    return subprocess.getoutput(cmd)


@mcp.tool
def generate_boundary_tests(
    class_name: str,
    method_name: str,
    param_desc: str,
) -> str:
    """
      "int index: -1, 0, 1, 10, Integer.MAX_VALUE"

    """
    test_dir = Path("src/test/java/generated")
    test_dir.mkdir(parents=True, exist_ok=True)

    file_path = test_dir / f"{class_name}BoundaryTest.java"

    content = f"""import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang3.{class_name};

public class {class_name}BoundaryTest {{

    /**
     * Boundary / equivalence-class tests for {class_name}.{method_name}.
     *
     * Parameters description:
     * {param_desc}
     *
     */
    @Test
    public void test_{method_name}_boundaries() {{
        // TODO: Construct inputs for each boundary / equivalence class
        // and call {class_name}.{method_name}.

        // Example pattern (to be refined by the agent):
        // {class_name} obj = new {class_name}();
        // Object result = obj.{method_name}(...);
        // assertEquals(expected, result);

        assertTrue(true);
    }}
}}
"""

    file_path.write_text(content, encoding="UTF-8")
    return f"Generated boundary-value test at {file_path}"



@mcp.tool
def simple_code_review(path: str = "src/main/java") -> str:
    """
    Perform a very simple static scan of Java files under `path`
    and report basic code smells:
      - TODO comments
      - System.out.println (debug prints)
      - printStackTrace calls
    """
    base = Path(path)
    if not base.exists():
        return f"Path not found: {path}"

    findings = []
    for java_file in base.rglob("*.java"):
        try:
            for i, line in enumerate(java_file.read_text(encoding="UTF-8").splitlines(), start=1):
                if "TODO" in line:
                    findings.append(f"{java_file}:{i}: TODO comment")
                if "System.out.println" in line:
                    findings.append(f"{java_file}:{i}: System.out.println (debug print)")
                if "printStackTrace(" in line:
                    findings.append(f"{java_file}:{i}: printStackTrace call")
        except Exception as e:
            findings.append(f"Error reading {java_file}: {e}")

    if not findings:
        return f"No simple code smells found under {path}."

    return "Simple code review findings:\n" + "\n".join(findings)


if __name__ == "__main__":
    mcp.run()
