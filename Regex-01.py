import re

def valid_commit(message):
    pattern = r'^(\w+),\(([\w\-]+)\): (.+) ([A-Z]+-\d+)$'
    match = re.match(pattern, message)
    return match is not None


def extract_parts(message):
    pattern = r'^(\w+)\(([\w\-]+)\): (.+) ([A-Z]+-\d+)$'
    match = re.match(pattern, message)
    if match:
        return {
            'type': match.group(1),
            'scope': match.group(2),
            'subject': match.group(3),
            'jira_id': match.group(4)
        }
    return None


test_messages = [
    "feature(auth): add login flow HSU-123",    # valid
    "fix(core): correct bug in parser ABC-456",  # valid
    "docs(readme): update documentation DOC-12",  # valid
    "feat(auth): improve security",             # invalid, missing JIRA-ID
    "feature(auth): incomplete HSU-",          # invalid
    "refactor(utils): better error handling HSU-999",  # valid
]

print("Testing commit message validation and extraction:\n")

for msg in test_messages:
    print(f"Message: '{msg}'")
    if valid_commit(msg):
        parts = extract_parts(msg)
        print("Valid commit")
        print(f"Type   : {parts['type']}")
        print(f"Scope  : {parts['scope']}")
        print(f"Subject: {parts['subject']}")
        print(f"JIRA-ID: {parts['jira_id']}")
    else:
        print("Invalid commit")