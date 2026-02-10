password = input("Enter your password: ")

length = len(password)

has_digit = False
has_special = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if not ch.isalnum():
        has_special = True

if length < 8:
    print("Weak password ❌")
elif has_digit and has_special:
    print("Strong password ✅")
else:
    print("Medium password ⚠️")
