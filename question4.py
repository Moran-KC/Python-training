import csv
import smtplib
from email.message import EmailMessage

with open('testinfo.csv', 'w+', newline='') as info:
    field_names = ['name', 'gender', 'city', 'email', 'status']

    csv_writer = csv.DictWriter(info, fieldnames=field_names, delimiter=',')

    csv_writer.writeheader()

    for line in info:
        csv_writer.writerow(line)


def party_mail_list(contact):
    EMAIL_ADDRESS = ' '
    EMAIL_PASSWORD = ' '
    name = info['name']
    city = info['city']
    status = info['status']
    msg = EmailMessage()
    msg['Subject'] = ' '
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = info['email']