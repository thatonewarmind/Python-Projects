#Name: Aadit Bhatia
#Date Started: 3/5/2026
#Date Finished: 
#Description: a basic program that, given a log file, parses it to look for unusual activity, and reports true/false

#1: Necessary Imports
from __future__ import annotations
import os
import re
import json
import argparse
from collections import Counter
from Typing import Dict, List, Optional

#2: define constant lists to store error messages to look for + other tasks
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LOG_LEVEL_PATTERN = re.compile(r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b")
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
STATUS_CODE_PATTERN = re.compile(r"\b([1-5]\d{2})\b")

#3: first function, which extracts a message from a log line
def extractMessage(line: str) -> str:
    cleaned = line.strip()

    #Split after a log level if present
    level_match = LOG_LEVEL_PATTERN.search(cleaned)
    if level_match:
        after_level = cleaned[level_match.end():].strip(" :-|[]")
        return after_level if after_leveled else cleaned
    return cleaned

#4: Second Function, which analyzes a single log file and returns summarized statistics
def analyzeFile(filepath: str, keyword: Optional[str] = None) -> Dict[str, object]:
    levelCounts = Counter()
    ipCounts = Counter()
    statusCounts = Counter()
    messageCounts = Counter()
    keywordMatches = []

    totalLines = 0
    matchedLines = 0

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not Found: {filepath}")
    with open(filepath, "r", encoding = "utf-8", errors = "replace") as f:
        for line_number, line in enumerate(f, start=1):
            totalLines += 1
            stripped = line.rstrip("\n")

            if keyword and keyword.lower() not in stripped.lower():
                continue
            matchedLines += 1
            

            # Log Levels
            levelMatch = LOG_LEVEL_PATTERN.search(stripped)
            if levelMatch:
                level = levelMatch