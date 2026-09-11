# 🔐 Password Complexity Checker

A simple **Python-based Password Complexity Checker** that evaluates the strength of a password based on common complexity requirements.

The program checks whether the password contains sufficient length, uppercase letters, lowercase letters, numbers, and special characters. It then classifies the password as **Weak, Medium, or Strong** and provides suggestions for improvement.

---

## 🚀 Features

* 🔢 Checks password length
* 🔠 Checks for uppercase letters
* 🔡 Checks for lowercase letters
* 🔢 Checks for numbers
* 🔣 Checks for special characters
* 📊 Calculates a password complexity score
* 💡 Provides feedback for missing requirements
* 🛡️ Simple and lightweight command-line tool

---

## 🧠 Password Strength Criteria

The checker evaluates **5 basic criteria**:

| Criteria          | Requirement                    | Score |
| ----------------- | ------------------------------ | ----: |
| Length            | At least 8 characters          |    +1 |
| Uppercase         | At least one `A-Z`             |    +1 |
| Lowercase         | At least one `a-z`             |    +1 |
| Number            | At least one `0-9`             |    +1 |
| Special Character | At least one special character |    +1 |

The program uses regular expressions to identify uppercase, lowercase, numeric, and special characters.

---

## 📊 Strength Classification

The final score determines the password strength:

| Score | Strength  |
| ----: | --------- |
|   0–2 | 🔴 Weak   |
|   3–4 | 🟡 Medium |
|     5 | 🟢 Strong |

This classification is implemented directly in the program.

---

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re` module)**

---

## 📂 Project Structure

```text
Password-Complexity-Checker/
│
├── passchecker.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Password-Complexity-Checker.git
```

### 2. Navigate to the project

```bash
cd Password-Complexity-Checker
```

### 3. Run the program

```bash
python passchecker.py
```

No external Python packages are required because the project uses Python's built-in `re` module.

---

## ▶️ Usage

Run the program:

```bash
python passchecker.py
```

You will see:

```text
========================================
       PASSWORD COMPLEXITY CHECKER
========================================

Enter your password:
```

Enter your password when prompted.

### Example — Strong Password

```text
Enter your password: Cyber@2026Secure

Password Strength: Strong
Good! Your password meets all the basic criteria.

Password check completed.
```

### Example — Weak Password

```text
Enter your password: password

Password Strength: Weak

Suggestions:
- Add at least one uppercase letter.
- Add at least one number.
- Add at least one special character.

Password check completed.
```

The program displays suggestions whenever one or more complexity requirements are not satisfied.

---

## 🔍 How It Works

The password is passed to the `check_password()` function.

The function:

1. Initializes a score of `0`.
2. Checks password length.
3. Searches for uppercase characters.
4. Searches for lowercase characters.
5. Searches for numbers.
6. Searches for special characters.
7. Calculates the total score.
8. Assigns a strength level.
9. Returns the strength and improvement suggestions.

### Basic Flow

```text
User enters password
        ↓
Check password length
        ↓
Check uppercase
        ↓
Check lowercase
        ↓
Check numbers
        ↓
Check special characters
        ↓
Calculate score
        ↓
Determine strength
        ↓
Display feedback
```

---

## ⚠️ Security Note

This project is intended for **educational purposes** and demonstrates basic password-complexity validation.

Password complexity alone does **not** determine whether a password is secure. A real-world password security system should also consider factors such as:

* Password length
* Password reuse
* Common/compromised passwords
* Password breach databases
* Secure password hashing
* Rate limiting
* Multi-factor authentication (MFA)

Also, avoid entering real passwords into demonstration tools if the tool is not specifically designed for secure password handling.

---
