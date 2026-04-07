# CS1350 - Computer Science II
# Cody Burton
# 4/7/2026
# CS1350-Week10-Lab.py

import re

# Unit 3: Introduction to Regular Expressions

# Exercises

# Beginner — Search for Patterns
import re
text = "My student ID is s12345 and my room is B204"
match = re.search(r"\d", text)
if match:
    print(f"First digit: {match.group()}")
    print(f"Found at position: {match.start()}")
    
match2 = re.search(r"[A-Z]\d", text)
if match2:
    print(f"Letter-digit pair: {match2.group()}")
    print(f"Span: {match2.span()}")
    
match3 = re.search(r"s\d{5}", text)
if match3:
    print(f"Student ID: {match3.group()}")
    
# Intermediate — Character Type Detective
samples = [
    "Room A3 is open",
    "Call 5551234 now",
    "hello world",
    "ERROR: code 42",
]
for text in samples:
    print(f"\nAnalyzing: '{text}'")
    
    upper_digit = re.search(r"[A-Z]\d", text)
    if upper_digit:
        print(f" Upper+digit pair: '{upper_digit.group()}' at {upper_digit.span()}")
        
    digit_lower = re.search(r"\d[a-z]", text)
    if digit_lower:
        print(f" Digit+lower pair: '{digit_lower.group()}' at {digit_lower.span()}")
        
    space_nonspace = re.search(r"\s\S", text)
    if space_nonspace:
        print(f" Space boundary at position: {space_nonspace.start()}")
        
    special = re.search(r"[^a-zA-Z0-9]", text)
    if special:
        print(f" Special char: '{special.group()}' at {special.start()}")
    else:
        print(f" No special characters found")
        
# Advanced — Date Stamp Finder

log_lines = [
    "2026-03-10 INFO Server started on port 8080",
    "2026-03-10 ERROR Connection refused",
    "no date here, just a message",
    "2026-03-11 WARN Memory usage high",
]

for line in log_lines:
    # TODO 1: Search for a date stamp: 4 digits, dash, 2 digits, dash, 2 digits
    # Use only \d and literal dashes
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", line)
    # TODO 2: Search for "ERROR" as a literal string
    is_error = re.search(r"ERROR", line)
    # TODO 3: Search for a 4-digit number (digit NOT preceded/followed by dash)
    port_match = re.search(r"(?<!-)\b\d{4}\b(?!-)", line)
    # Build output
    if date_match:
        date_str = date_match.group()
        rest = line[date_match.end():]
        status = "ERROR" if is_error else "ok "
        port = port_match.group().strip() if port_match else "n/a"
        print(f"[{date_str}] {status} | port: {port} | {rest.strip()}")
    else:
        print(f"[no date ] skipped | {line}")
