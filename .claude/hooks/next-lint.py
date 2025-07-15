#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def main():
    try:
        # Read input data from stdin
        input_data = json.load(sys.stdin)

        tool_input = input_data.get("tool_input", {})
        print(tool_input)

        # Get file path from tool input
        file_path = tool_input.get("file_path")
        if not file_path:
            sys.exit(0)

        # Only check TypeScript/JavaScript files
        if not file_path.endswith((".ts", ".tsx", ".js", ".jsx")):
            sys.exit(0)

        print(f"Run `npm run lint` in the /frontend/vectal.ai directory to check and fix any linting errors")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error in next lint hook: {e}", file=sys.stderr)
        sys.exit(1)


main()