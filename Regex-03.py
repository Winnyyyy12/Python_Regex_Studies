import re


def validate_jira_ticket(ticket):

    pattern = r'^[A-Z]{2,5}-\d+$'

    if re.fullmatch(pattern, ticket):
        return True
    else:
        return False

test_cases = [
    "AB-123",         # valid
    "PROJ-45678",     # valid
    "A-123",          # invalid
    "PROJECT-12",     # invalid
    "ABCD-XYZ",       # invalid
    "abc-123",        # invalid
    "AB_123",         # invalid
    "XYZ-987654321",  # valid
]

for ticket in test_cases:
    result = validate_jira_ticket(ticket)
    print(f"{ticket}: {'Valid' if result else 'Invalid'}")
