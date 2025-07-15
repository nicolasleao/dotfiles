#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from datetime import datetime

# Constants for file paths and directories
OUTPUT_FILENAME = "_log_bash_commands.json"
CLAUDE_DIR = Path(__file__).parent.parent  # .claude directory
LOG_FILE_PATH = CLAUDE_DIR / OUTPUT_FILENAME


def log_to_file(activity_record):
    """
    Append an activity record to the log file.
    
    Args:
        activity_record: Dictionary containing the log entry to save
    """
    # Load existing records or initialize empty list
    existing_records = []
    if LOG_FILE_PATH.exists():
        with open(LOG_FILE_PATH, "r") as file_handle:
            existing_records = json.load(file_handle)
    
    # Add new record to the collection
    existing_records.append(activity_record)
    
    # Write updated records back to file
    with open(LOG_FILE_PATH, "w") as file_handle:
        json.dump(existing_records, file_handle, indent=2)


def main():
    try:
        # Parse incoming data from standard input
        received_data = json.load(sys.stdin)

        # Extract tool parameters from the received data
        tool_parameters = received_data.get("tool_input", {})

        # Build activity record with relevant information
        activity_record = {
            "timestamp": datetime.now().isoformat(),
            "session_id": received_data.get("session_id"),
            "tool_name": received_data.get("tool_name"),
            "command": tool_parameters.get("command"),
            "description": tool_parameters.get("description"),
        }

        # Save the activity record to file
        log_to_file(activity_record)

        print(f"Tool input logged to {LOG_FILE_PATH}")

    except json.JSONDecodeError as decode_error:
        print(f"Error parsing JSON input: {decode_error}", file=sys.stderr)
        sys.exit(1)
    except Exception as general_error:
        print(f"Error: {general_error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()