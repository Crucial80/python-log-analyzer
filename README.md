# python-log-analyzer
SOC-style Python log analyzer for basic threat detection
# Python Log Analyzer (SOC Automation)

## Overview
This project is a simple Python-based log analyzer designed to simulate SOC-style log monitoring and basic threat detection.

It analyzes Linux authentication logs to identify failed login attempts, successful logins, and invalid user access attempts.

---

## Objectives
- Understand Linux log formats
- Detect suspicious authentication activity
- Automate basic SOC tasks using Python
- Improve log analysis and scripting skills

---

## Features
- Detects failed login attempts
- Identifies successful SSH logins
- Flags invalid user access attempts
- Extracts and counts source IP addresses

---

## Technologies Used
- Python 3
- Regular Expressions
- Linux authentication logs (auth.log)

---

## How It Works
1. Reads authentication logs line by line
2. Matches security-related patterns
3. Extracts source IP addresses
4. Displays a summarized report

---

## Example Use Case
This tool can help SOC analysts quickly identify brute-force attempts or suspicious login behavior during initial incident triage.

---

## Disclaimer
This project is created for educational and learning purposes only and was tested in controlled lab environments.
