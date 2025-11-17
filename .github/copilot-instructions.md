<!-- Auto-generated / merged Copilot instructions for this repo -->
# Repo-specific Copilot instructions

Purpose
- Help an AI coding agent be productive in this repository (Apache-commons-lang3 fork used for the SE333 final project).

High-level architecture
- Java library (org.apache.commons.lang3) implemented under `src/main/java/org/apache/commons/lang3`.
- Built with Maven (`pom.xml`) using Java 1.8 source/target. Key plugins: `maven-compiler-plugin`, `jacoco-maven-plugin` (coverage), `maven-surefire-plugin` (tests), `maven-assembly-plugin`.
- Tests live in `src/test/java`. The project includes a `src/test/java/generated` folder where tooling can place generated tests.
- A Python helper `server.py` exposes developer tools (via FastMCP) for running tests, parsing coverage, generating tests, and simple code review.

Developer workflows (commands you can run)
- Run unit tests: `mvn test` (configured to generate JaCoCo report in `target/site/jacoco/jacoco.xml`).
- Start the FastMCP agent: `python server.py` (it calls `mcp.run()` and exposes tools such as `run_tests`, `get_coverage`, `generate_test`).
- A helper `main.py` runs `mvn test` then calls `uv run server.py get_coverage` — note: `uv` is invoked in this script and may require the environment/tooling that the original author used; prefer `mvn test` and `python server.py` directly if unsure.

Testing & coverage details
- JaCoCo is wired to the `test` phase; after `mvn test` the XML report is at `target/site/jacoco/jacoco.xml` and an HTML report under `target/site/jacoco`.
- The `server.py` tool `get_coverage()` parses `jacoco.xml` and returns line coverage percentage — useful for quick checks.
- `maven-surefire-plugin` is configured with `testFailureIgnore=true` and `runOrder=random`. Be aware: failures may not fail `mvn test`, and test runs are randomized.

Project-specific conventions
- Encoding: source files use `ISO-8859-1` (see `pom.xml` property). Preserve encoding when editing Java source.
- Java compatibility: `source`/`target` set to 1.8 — do not use language features beyond Java 8 in library code.
- Generated tests: the project tooling (in `server.py`) writes placeholder tests to `src/test/java/generated` named like `{ClassName}GeneratedTest.java` and `{ClassName}BoundaryTest.java`. Those contain `assertTrue(true)` placeholders — ensure you replace with meaningful assertions.

Integration points and notable files
- `pom.xml` — primary build/test configuration and plugin settings (compiler, surefire, jacoco).
- `server.py` — exposes FastMCP tools: `run_tests`, `get_coverage`, `generate_test`, `generate_boundary_tests`, `simple_code_review`, plus lightweight `git_*` helpers.
- `main.py` — thin script that runs tests and attempts to fetch coverage via the `uv` CLI; useful as an example driver.
- Source: `src/main/java/org/apache/commons/lang3` — core library packages and classes.

Behavioral notes for AI agents
- Prefer making changes in small PRs limited to one logical task (bugfix, test, small refactor).
- If adding tests, place them under `src/test/java` and follow the established naming pattern `*Test.java` so Surefire picks them up; for generated scaffolding use `src/test/java/generated`.
- When running tests locally use `mvn test` and inspect `target/surefire-reports` and `target/site/jacoco` for results. Do not assume `mvn test` will fail the build on failing tests because `testFailureIgnore` is enabled.

Examples (use these exact paths)
- Generate a placeholder test from the helper: run the FastMCP tool `generate_test(class_name="StringUtils", method_name="isEmpty")` — it will create `src/test/java/generated/StringUtilsGeneratedTest.java`.
- Check coverage via the Python helper: `python server.py` then invoke the `get_coverage()` tool or run `mvn test` and inspect `target/site/jacoco/jacoco.xml`.

FastMCP usage examples
- Start the FastMCP agent (starts an MCP server exposing the decorated tools):
	- `python server.py`
	- Keep this running in a terminal while you invoke tools from another terminal.
- Quick demo (single-command):
	- `python main.py`
	- This runs `mvn test` and then attempts `uv run server.py get_coverage` (used as a convenience wrapper in this repo).
- Invoke individual tools (examples):
	- Generate a placeholder test:
		- `uv run server.py generate_test StringUtils isEmpty`
		- This creates `src/test/java/generated/StringUtilsGeneratedTest.java`.
	- Get coverage (after running tests):
		- `uv run server.py get_coverage`
		- or run `mvn test` then `python server.py` and use the FastMCP client/CLI you have available to call `get_coverage()`.
- Notes and fallbacks:
	- The `uv` CLI used in `main.py` may not be available in every environment. If `uv` is missing, prefer `python main.py` (if you only need the demo flow) or run `mvn test` then inspect `target/site/jacoco/jacoco.xml` directly.
	- The FastMCP server exposes other tools listed in `server.py` (e.g., `run_tests`, `generate_boundary_tests`, `simple_code_review`, `git_status`). Use `uv run server.py <tool> [args]` or your FastMCP client.

Exact FastMCP tool outputs (literal strings)
- `get_coverage()` when JaCoCo XML is missing (exact):
	- "Coverage file not found. Run run_tests() first to generate JaCoCo report."
- `generate_test(class_name, method_name)` (exact on success):
	- "Generated test at src/test/java/generated/{ClassName}GeneratedTest.java"
		- e.g. "Generated test at src/test/java/generated/StringUtilsGeneratedTest.java"
- `generate_boundary_tests(class_name, method_name, param_desc)` (exact on success):
	- "Generated boundary-value test at src/test/java/generated/{ClassName}BoundaryTest.java"
		- e.g. "Generated boundary-value test at src/test/java/generated/StringUtilsBoundaryTest.java"
- `simple_code_review(path)` when no findings (exact):
	- "No simple code smells found under {path}."
		- e.g. "No simple code smells found under src/main/java"
- `simple_code_review(path)` when findings exist (example line):
	- "Simple code review findings:\nsrc/main/java/org/apache/commons/lang3/SomeClass.java:123: TODO comment"

Example `mvn test` summary (real output will vary)
- Maven prints a long log; the near-final summary typically includes a line like:
	- "Tests run: 123, Failures: 0, Errors: 0, Skipped: 0"
- JaCoCo report parsing format returned by `get_coverage()` when report exists (example):
	- "Line coverage: 85.32% (153 covered / 26 missed, total 179)"

These exact strings help automation parse FastMCP outputs reliably. If you want, I can run `mvn test` here and attach the real summary and a real `get_coverage()` output from this workspace.

If uncertain / where to look
- Start with `pom.xml` (build logic), `server.py` (developer tools), and `src/main/java/org/apache/commons/lang3` (implementation).
- Use `target/surefire-reports` and `target/site/jacoco` to inspect test outputs and coverage.

Feedback
- If anything in these instructions is incomplete or you have preferred workflows (e.g., CI steps, `uv` usage), tell me and I'll update this file.
