# Password Verification Program

## Overview
This program performs a simple password verification process. It first checks whether the password meets a minimum length requirement and then verifies the user knows specific characters from the password.

## Program Logic
1. The user enters a password.
2. If the password is shorter than 9 characters, the program exits.
3. If valid, the program asks for **three random letters** from the password.
4. If any answer is incorrect, the program exits immediately.
5. If all answers are correct, the security check is passed.

## Notes
- Password characters are counted starting from position **1**.
- Random positions may repeat.
- The program exits immediately on failure for security reasons.
- Designed for clarity and beginner-level understanding.