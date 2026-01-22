import re
from collections import defaultdict

# Sample log file path
LOG_FILE = "auth.log"

# Patterns to detect events
FAILED_LOGIN_PATTERN = r"Failed password for"
SUCCESS_LOGIN_PATTERN = r"Accepted password for"
INVALID_USER_PATTERN = r"Invalid user"

failed_logins = defaultdict(int)
successful_logins = defaultdict(int)
invalid_users = defaultdict(int)

def analyze_logs():
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                if re.search(FAILED_LOGIN_PATTERN, line):
                    ip = extract_ip(line)
                    failed_logins[ip] += 1

                elif re.search(SUCCESS_LOGIN_PATTERN, line):
                    ip = extract_ip(line)
                    successful_logins[ip] += 1

                elif re.search(INVALID_USER_PATTERN, line):
                    ip = extract_ip(line)
                    invalid_users[ip] += 1

        print_results()

    except FileNotFoundError:
        print("Log file not found. Please check the file path.")

def extract_ip(log_line):
    match = re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", log_line)
    return match.group() if match else "Unknown"

def print_results():
    print("\n=== FAILED LOGIN ATTEMPTS ===")
    for ip, count in failed_logins.items():
        print(f"{ip} : {count} times")

    print("\n=== SUCCESSFUL LOGINS ===")
    for ip, count in successful_logins.items():
        print(f"{ip} : {count} times")

    print("\n=== INVALID USER ATTEMPTS ===")
    for ip, count in invalid_users.items():
        print(f"{ip} : {count} times")

if __name__ == "__main__":
    analyze_logs()
