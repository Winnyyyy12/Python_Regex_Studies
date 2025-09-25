import re

def valid_email(email):

    pattern = r'^[\w\.]+@[A-Z,a-z,0-9\-]+\.[A-Z,a-z]{2,6}$'
    match = re.match(pattern, email)
    return match is not None

test_emails = [
    "user.name123@domain.com",    # valid
    "user_name@sub-domain.org",   # valid
    "username@domain.co.uk",      # invalid
    "user@domain",                # invalid
    "user@domain.c",              # invalid
    "user@domain.toolongext",     # invalid
    "user.name@domain.com",       # valid
    "user..name@domain.com",      # valid
    "user@domain..com",           # invalid
    "user@-domain.com",           # invalid
]

print("Testing email validation:\n")

for email in test_emails:
    print(f"Email: '{email}'")
    if valid_email(email):
        print("Valid email")
    else:
        print("Invalid email")


# import re

# email=input("what's your email?").strip()

# if re.search(r'^[a-z,A-Z,0-9._%+-]+@[a-z,A-Z,0-9.-]+\.[a-z,A-Z]{2,}$',email):
#     print("valid email")
# else:
#     print("invalid email")
