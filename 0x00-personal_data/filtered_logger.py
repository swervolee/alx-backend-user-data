#!/usr/bin/env python3
"""
DATA OBFUSCATION
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates data
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
