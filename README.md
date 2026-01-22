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
- ## Automation (Cron Job)
To simulate SOC-style continuous monitoring, the log analyzer can be scheduled using a cron job.

Example cron entry:
*/5 * * * * python3 /path/to/python-log-analyzer/log_analyzer.py >> /path/to/output.log

This allows the script to run periodically and automate log analysis without manual intervention.


## How It Works
1. Reads authentication logs line by line
2. Matches security-related patterns
3. Extracts source IP addresses
4. Displays a summarized report

---
## Log Source Note
Different Linux distributions store authentication logs differently.
This project was tested using both `/var/log/auth.log` and `journalctl` output.
The analyzer reports events only when relevant authentication activity is present.

## Example Use Case
This tool can help SOC analysts quickly identify brute-force attempts or suspicious login behavior during initial incident triage.

---
## Live Execution Screenshot
The following screenshot shows the Python log analyzer running on a Linux system and detecting authentication-related events from real log files.

![Python Log Analyzer Output](screenshots/Script_Output.png)


## Disclaimer
This project is created for educational and learning purposes only and was tested in controlled lab environments.
