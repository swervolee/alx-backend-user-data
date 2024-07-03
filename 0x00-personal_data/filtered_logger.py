#!/usr/bin/env python3
"""
DATA OBFUSCATION
"""
import re
from typing import List


def filter_datum(fields: List,
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates data
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
