<h1>Email Marketing Script with Python 📧</h1>

Welcome to the **Email Marketing Script** repository! 🚀 This Python script allows you to automate email marketing campaigns by sending emails to multiple recipients listed in an Excel file. 💼✨

 <h2>Features 🌟</h2>

- Extracts email addresses from an Excel file 📋
- Sends personalized HTML emails to multiple recipients ✉️
- Includes a delay between sending emails to avoid spam filters ⏳
- Simple and easy-to-use script 🔧

<h2>Requirements 📦</h2>

Make sure you have the following installed:

- Python 3.6+
- Required Python libraries:
  - `smtplib`
  - `email`
  - `openpyxl`

You can install `openpyxl` using pip:
```bash
pip install openpyxl

<h2> Notes 📝

- Ensure your SMTP server allows sending emails through the provided credentials.
- Use dummy credentials and a test email list before running the script with real data. 🛡️
- Respect privacy and avoid sending unsolicited emails. 🙏

<h2>Example HTML Email Template ✨

The script includes a sample HTML email template:
```html
<div style="padding: 20px; text-align: center;">
    <h2 style="color: #333;">Dummy Email Content</h2>
    <p style="font-size: 16px; color: #555;">This is a dummy message body. Replace this with your actual email content.</p>
    <a href="https://example.com" target="_blank" style="background-color: #FF4B6A; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Visit Us</a>
</div>
```

Feel free to customize it to suit your needs! 🎨

<h2>💡 Pro Tip:</h2>
If you want to avoid storing sensitive information like email credentials in the script, use environment variables. For example:
```python
import os
fromEmail = os.getenv('EMAIL_ADDRESS')
login_password = os.getenv('EMAIL_PASSWORD')
```

<h2>Contact ✉️</h2>
Manish
github:https://github.com/manish676




