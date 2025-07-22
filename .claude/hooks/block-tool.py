#!/usr/bin/env python3

import sys

def main():
    try:
        print("Error: This tool is not allowed, just reply to the user instead.", file=sys.stderr)
        # Exit with code 2 to signal LLM to correct
        sys.exit(2)
    except Exception as e:
        print(f"Error in block-tool hook: {e}", file=sys.stderr)
        sys.exit(1)


main()