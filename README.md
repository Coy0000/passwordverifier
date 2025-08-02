# 🔐 Password Strength Checker

A beginner-friendly Python project to check the strength of a password using basic string methods and conditions.

---

## 🧠 What It Does

- Ensures the password is at least **8 characters** long  
- Prevents using **only numbers** or **only letters**  
- Encourages use of **uppercase letters**  
- Gives helpful, friendly feedback at each step

---

##  💡 Sample Outputs
```text

Enter your password: 1234567
Too short! Password should be at least 8 characters.

Enter your password: password
Almost there! Don't use only letters.

Enter your password: password1
Going strong! Add at least one uppercase letter.

Enter your password: Password1
Good password!
```
## 🧰Key Concepts Used
```text
len() – check password length

.isdigit() – check for only numbers

.isalpha() – check for only letters

.islower() – check if all letters are lowercase

input() – to get user input

if-elif-else – control flow
```
