#!/usr/bin/env python3

import json
import sys
import re

def main():
    try:
        # Read input data from stdin
        input_data = json.load(sys.stdin)

        # tool_name = input_data.get("tool_name")
        tool_input = input_data.get("tool_input", {})

        command = tool_input.get("command", "")
        if not command:
            sys.exit(0)

        # Check for npm commands
        npm_build_pattern = r"\bnpm run build\b"
        npm_run_dev_pattern = r"\bnpm run dev\b"

        if re.search(npm_build_pattern, command):
            # Send error message to stderr for LLM to see
            print("Error: NPM build commands are not allowed, use the simpler `npm run lint` instead.", file=sys.stderr)
            # Exit with code 2 to signal LLM to correct
            sys.exit(2)

        if re.search(npm_run_dev_pattern, command):
            # Send error message to stderr for LLM to see
            print("Error: NPM run dev commands are not allowed, the server is already running on hot-reload mode.", file=sys.stderr)
            # Exit with code 2 to signal LLM to correct
            sys.exit(2)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error in block-npm-build-and-dev hook: {e}", file=sys.stderr)
        sys.exit(1)


main()