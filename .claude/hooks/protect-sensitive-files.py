#!/usr/bin/env python3
"""
Security hook to protect sensitive files
Blocks access to credentials, keys, and environment files
"""
import sys
import json
from pathlib import Path

SENSITIVE_PATTERNS = {
    '.env', '.env.local', '.env.production', '.env.development',
    '.pem', '.key', '.credential', '.token',
    'credentials.json', 'google-credentials.json',
    'service-account.json', 'private-key.json',
    'id_rsa', 'id_ed25519', '.ssh',
    'secrets', 'password'
}

SENSITIVE_DIRS = {
    'secrets', '.ssh', '.gnupg', 'credentials'
}

def is_sensitive_file(file_path: str) -> bool:
    """Check if file path matches sensitive patterns"""
    path = Path(file_path)

    # Check filename and extension
    if path.name in SENSITIVE_PATTERNS:
        return True
    if path.suffix in {'.pem', '.key', '.credential'}:
        return True

    # Check if in sensitive directory
    for part in path.parts:
        if part in SENSITIVE_DIRS:
            return True

    # Check for common patterns
    name_lower = path.name.lower()
    if any(pattern in name_lower for pattern in SENSITIVE_PATTERNS):
        return True

    return False

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)

        # Extract file path
        tool_input = input_data.get('tool_input', {})
        file_path = tool_input.get('file_path', '')

        if not file_path:
            sys.exit(0)  # No file path, allow

        if is_sensitive_file(file_path):
            # Block access
            error_msg = f"""SECURITY_POLICY_VIOLATION: Access to sensitive file '{file_path}' is blocked.

Files containing credentials, keys, or environment variables should not be accessed.
Instead:
- Use environment variables for secrets
- Ask for specific configuration values
- Reference documentation for setup instructions
"""
            print(error_msg, file=sys.stderr)
            sys.exit(2)  # Exit code 2 blocks the tool

        sys.exit(0)  # Allow

    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(0)  # On error, allow (fail open)

if __name__ == '__main__':
    main()
