#!/usr/bin/env python3
"""
A module to obfuscate data
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    A function to obfuscate data
    """
    pattern = f"({'|'.join(fields)})[^{separator}]*"
    result = re.sub(pattern, lambda x: f"{x.group(1)}={redaction}", message)
    return result
