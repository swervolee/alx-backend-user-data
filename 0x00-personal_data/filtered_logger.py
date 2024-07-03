#!/usr/bin/env python3
"""
DATA OBFUSCATION
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates data

    Args:
        fields (List[str]):
        A list of strings representing all fields to obfuscate.

        redaction (str):
        A string representing by what the field will be obfuscated.

        message (str):
        A string representing the log line.

        separator (str):
        A string representing by which character is
        separating all fields in the log line (message).

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
