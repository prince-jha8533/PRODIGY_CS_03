import re


def check_password(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Decide password strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


print("=" * 40)
print("       PASSWORD COMPLEXITY CHECKER")
print("=" * 40)

password = input("Enter your password: ")

strength, feedback = check_password(password)

print("\nPassword Strength:", strength)

if strength == "Strong":
    print("Good! Your password meets all the basic criteria.")

else:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

print("\nPassword check completed.")