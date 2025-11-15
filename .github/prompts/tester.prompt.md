---
mode: "agent"
tools: [
  "mvn_test_and_coverage",
  "coverage_summary",
  "coverage_by_class",
  "read_java_file",
  "create_test_skeleton",
  "test_quality_metrics",
  "git_status",
  "git_add_all",
  "git_commit",
  "git_push",
  "generate_string_edge_cases",
  "generate_integer_edge_cases"
]
description: "SE333 testing agent that improves tests and coverage for the provided Maven codebase."
---

## Follow instruction below: ##

1. Run mvn test.
2. Use JaCoCo coverage to find uncovered code.
3. Generate JUnit tests to raise coverage.
4. Retry testing until coverage improves.
5. Commit changes automatically when coverage increases.
6. Push commits to GitHub.

## Specifications


# 1. Testing & Coverage
- Start by running `run_tests`.
- After it finishes, call `get_coverage` to see current coverage.
- Use this to decide which class or method needs tests.

# 2. Generating & Improving Tests
- Use `generate_test(class_name, method_name)` to create a basic test file.
- Or use `generate_boundary_tests(class_name, method_name, param_desc)` for edge-case tests.
- Then improve the generated tests by:
    - Adding real parameters
    - Writing real assertions
    - Testing edge cases or failing scenarios

# 3. Bug Exposure & Fix
- If a test fails unexpectedly, analyze the failure.
- Suggest or apply a small fix to the Java code.
- Re-run tests to confirm the fix works.

# 4. Git Workflow
After a meaningful improvement:
- Run `git_status`
- Stage with `git_add_all`
- Commit using `git_commit("Explain what changed")`
- Push with `git_push()`


## Goal

Iterate until:
- Coverage increases
- The bug is exposed and fixed
- All changes are committed and pushed
