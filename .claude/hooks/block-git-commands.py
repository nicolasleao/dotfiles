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

        # Check for git commands
        git_pattern = r"\bgit\b"

        if re.search(git_pattern, command):
            # Send error message to stderr for LLM to see
            print("Error: Git commands are not allowed", file=sys.stderr)
            # Exit with code 2 to signal LLM to correct
            sys.exit(2)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error in block-git-commands hook: {e}", file=sys.stderr)
        sys.exit(1)


main()