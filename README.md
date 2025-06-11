# Email Sending Script for Internship Applications

 Candidature Sender is a Python-based automated email sender designed to help students and job seekers efficiently send personalized internship or job application emails in batches. It reads recipient email addresses from a file, attaches your CV, and sends custom messages securely via Gmail SMTP using an app password. Perfect for anyone looking to streamline their application process while respecting email sending limits.

---

## Features

- Reads recipient emails from a text file (`emails.txt`)
- Sends personalized email with subject and message body
- Supports attachment (e.g., CV.PDF)
- Sends emails securely via Gmail SMTP using App Password
- Can be enhanced to send batches and run in the background (see script comments)

---

## Requirements

- Python 3.x
- `smtplib`, `email` (standard libraries)
- A Gmail account with **App Password** enabled (if 2FA is on)


---

## Setup
### 1. Create app password from gmail:
#### Enable 2-Step Verification 
(if not already enabled)
```
1. Go to: https://myaccount.google.com/security

2. Under "Signing in to Google", click "2-Step Verification"

3. Follow the steps to enable it using your phone or another method.
```
#### Generate App Password
Once 2-Step Verification is enabled, go to:
```
1. https://myaccount.google.com/apppasswords
2. Login again if asked.
3. Under "Select app", choose:
4. Mail or Other (Custom name) → e.g. Python Email Script
5, Under "Select device", choose:
6. Other or your device name.
7.Click "Generate"
```
#### Google will show you a 16-character password like:
`abcd abcd abcd abcd`


### 2. Clone the repo:
   ```
   git clone https://github.com/moza369/candidaturesender.git
   cd candidaturesender
```
### 3. Edit your email credentials and message in the script:
```
your_email = "youremail@gmail.com"
your_password = "abcdabcdabcdabcd"
```
### 4. Prepare emails.txt with one recipient email per line.
if you have a pdf file or a text file with mixed emails and email use this one to grep emails:
note :For pdf files `use first pdftotext test.pdf` 
`cat text.txt | grep -Eo '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' > emails.txt`
### 5.Add your CV file (e.g., cv.pdf) in the same directory.

## USAGE

`  python3 candidaturesender.py  `

### In background (bash linux)
if you like to let the script run in the background even if you close the terminal:

` nohup python3 candidaturesender.py & `

## Author
Zahir Mohamed.
