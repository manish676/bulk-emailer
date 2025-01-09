import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openpyxl
import os
import time  # Importing time module for sleep function

# Function to extract email addresses from Excel file
def extractEmailsFromExcel(excel_file):
    emailList = []
    try:
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        # Assuming emails are in the first column starting from row 2
        for row in sheet.iter_rows(min_row=2, values_only=True):
            email = row[0]  # First column of each row
            if email:  # Only add non-empty emails
                emailList.append(email)
        print(f"Extracted Emails: {emailList}")  # Debug print to see the extracted emails
    except Exception as e:
        print(f"Error reading Excel file: {e}")
    return emailList

# Function to send email
def sendMail(fromEmail, toEmail, subject, message, smtp_server, smtp_port, login_password):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = ", ".join(toEmail)  # Multiple recipients
        msg['Subject'] = subject

        # Attach the email message body (HTML content)
        msg.attach(MIMEText(message, 'html'))

        # Connect to the SMTP server (using SSL)
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # Login to the email server
        server.login(fromEmail, login_password)

        # Send the email
        server.sendmail(fromEmail, toEmail, msg.as_string())

        # Close the server connection
        server.quit()
        print(f"Email sent successfully to: {toEmail}")

    except Exception as e:
        print(f"Error sending email to {toEmail}: {e}")

# Main function to send an email using an Excel file
if __name__ == "__main__":
    print("Welcome to Email Marketing")

    # Email details
    fromEmail = 'your_email@example.com'  # Your email address
    subject = 'Dummy Subject'  # Replace with your subject

    # Dummy HTML content
    message = '''
    <div style="padding: 20px; text-align: center;">
        <h2 style="color: #333;">Dummy Email Content</h2>
        <p style="font-size: 16px; color: #555;">This is a dummy message body. Replace this with your actual email content.</p>
        <p style="font-size: 16px; color: #555;">Click the link below to know more:</p>
        <a href="https://example.com" 
           target="_blank" 
           style="background-color: #FF4B6A; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
            Visit Us
        </a>
        <p style="font-size: 14px; color: #777; margin-top: 20px;">Dummy Footer Text</p>
    </div>
    '''

    # Dummy SMTP details
    smtp_server = 'smtp.example.com'
    smtp_port = 465  # Port for SSL encryption
    login_password = 'your_password'  # Your password (replace with actual password cautiously)

    # Path to the Excel file containing email addresses
    excel_file_path = r'path_to_your_excel_file.xlsx'

    # Extract email addresses from the Excel file
    emailList = extractEmailsFromExcel(excel_file_path)

    # Counter for how many emails were sent
    email_counter = 0

    if emailList:
        # Send the email to each recipient with a delay of 5 seconds between each send
        for email in emailList:
            sendMail(fromEmail, [email], subject, message, smtp_server, smtp_port, login_password)
            email_counter += 1  # Increment counter after sending an email
            print(f"Waiting 5 seconds before sending the next email...")
            time.sleep(5)  # Wait for 5 seconds before sending the next email

        print(f"\nTotal emails sent: {email_counter}")
    else:
        print("No emails found in the Excel file!")
