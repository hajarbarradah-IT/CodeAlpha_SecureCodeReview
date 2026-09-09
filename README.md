# CodeAlpha - Secure Code Review

## 📌 Description
Security audit of a Python user authentication application, developed as part of the CodeAlpha Virtual Internship in Cybersecurity (Task 3).

## 🛠 Technologies Used
- Python 3
- SQLite3
- bcrypt

## 📂 Repository Contents
- `app_a_auditer.py` — original code, intentionally containing 5 security vulnerabilities
- `app_corrigee.py` — corrected, secured version
- `RAPPORT_AUDIT.md` — detailed audit report (vulnerabilities found, severity, recommendations)

## 🔍 Methodology
Manual code review (static analysis), searching for common vulnerabilities based on OWASP principles and secure coding best practices.

## 🎓 Vulnerabilities Identified and Fixed
1. Hardcoded credentials → environment variables
2. SQL Injection → parameterized queries
3. Dangerous use of `eval()` → `ast.literal_eval()`
4. Missing input validation → `try/except` error handling
5. Plaintext password storage → hashing with `bcrypt`

See `RAPPORT_AUDIT.md` for full details.

## ⚠️ Note
This project was completed as part of the CodeAlpha Virtual Cybersecurity Internship.
