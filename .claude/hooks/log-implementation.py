#!/usr/bin/env python3
"""
Log all implementation steps to JSONL for tracking
"""
import json
import sys
import os
from datetime import datetime
from pathlib import Path

PROJECT_DIR = os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())
LOG_DIR = Path(PROJECT_DIR) / '.claude' / 'logs'
LOG_FILE = LOG_DIR / 'implementation-steps.jsonl'

def ensure_log_dir():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_step(input_data):
    ensure_log_dir()

    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'tool_name': input_data.get('tool_name', 'unknown'),
        'tool_input': input_data.get('tool_input', {}),
        'success': input_data.get('success', True)
    }

    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def main():
    try:
        input_data = json.load(sys.stdin)
        log_step(input_data)
    except Exception as e:
        print(f"Logging error: {e}", file=sys.stderr)

    sys.exit(0)

if __name__ == '__main__':
    main()
