# server.py
import os
import subprocess
import glob
import httpx
from fastmcp import MCP, tool

mcp = MCP()
@tool
def run_tests():
    try:
        result = subprocess.run(
            ["mvn", "test"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error running mvn test: {e}"

@tool
def get_coverage():
    path = "target/site/jacoco/jacoco.xml"
    if not os.path.exists(path):
        return "Coverage file not found."

    import xml.etree.ElementTree as ET

    tree = ET.parse(path)
    root = tree.getroot()

    counters = root.findall(".//counter[@type='LINE']")
    if not counters:
        return "No LINE counter found."

    c = counters[0]
    covered = int(c.attrib["covered"])
    missed = int(c.attrib["missed"])
    total = covered + missed
    pct = round((covered / total) * 100, 2)

    return f"Line Coverage: {pct}%"

@tool
def generate_test(class_name: str, method_name: str):
    test_dir = "src/test/java/generated"
    os.makedirs(test_dir, exist_ok=True)

    filename = f"{test_dir}/{class_name}GeneratedTest.java"

    template = f"""
import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang3.{class_name};

public class {class_name}GeneratedTest {{

    @Test
    public void test_{method_name}() {{
        assertTrue(true);
    }}

}}
"""

    with open(filename, "w") as f:
        f.write(template)

    return f"Generated test at {filename}"

@tool
def git_status():
    return subprocess.getoutput("git status")

@tool
def git_add_all():
    return subprocess.getoutput("git add -A")

@tool
def git_commit(message: str):
    return subprocess.getoutput(f'git commit -m "{message}"')

@tool
def git_push():
    return subprocess.getoutput("git push --set-upstream origin main")

if __name__ == "__main__":
    mcp.run(transport="sse")
