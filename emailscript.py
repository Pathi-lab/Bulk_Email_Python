import os
import smtplib
import openpyxl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'abe@gmail.com'
sender_password = 'Password#3'  # Replace with your Gmail password
email_subject = 'Your Subject Here'
email_template = '''
Dear {name},

This is the content of the email.

Best regards,
Your Name
'''

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the Excel file name to the current directory path
excel_file_path = os.path.join(current_dir, 'Testexcel.xlsx')

# Function to send an email
def send_email(to_address, name):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_address
    message['Subject'] = email_subject

    email_body = email_template.format(name=name)
    message.attach(MIMEText(email_body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_address, message.as_string())
        print(f"Email sent successfully to {to_address}")
        server.quit()
    except Exception as e:
        print(f"Error sending email to {to_address}: {e}")

# Read email addresses from the Excel file
def read_emails_from_excel(file_path, sheet_name, column_name='Email Address'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]

    # Find the exact column index for 'Email Address' (case-insensitive comparison)
    email_column_index = None
    for col_idx, cell in enumerate(sheet[1], start=1):
        if cell.value and column_name.lower() == str(cell.value).strip().lower():
            email_column_index = col_idx
            break

    if email_column_index is None:
        raise ValueError(f"Column '{column_name}' not found in the Excel file.")

    # Extract email addresses from the column
    email_addresses = [row[email_column_index - 1].value for row in sheet.iter_rows(min_row=2)]

    wb.close()
    return email_addresses


# Main function to send emails to all email addresses in the Excel file
def send_emails_to_all():
    email_addresses = read_emails_from_excel(excel_file_path, 'Sheet1')  # Replace 'Sheet1' with the name of your sheet
    for email in email_addresses:
        # Assuming the first column in the Excel file is the "Name" column, change this according to your setup
        name = email.split('@')[0]
        send_email(email, name)

if __name__ == "__main__":
    send_emails_to_all()
