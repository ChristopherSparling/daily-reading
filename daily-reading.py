import smtplib
from hidden import credentials
from collections import namedtuple

Book = namedtuple('Book', ['s_title', 'i_recc_divisions', 's_division_word', 'ndifficulty'])
BookList = []

email_text = """
Subject: %s
Daily Readings: 
%s
%s
""" % (subject, "\n ".join)


def send(message):
    to_number = credentials['number'] + credentials['carrier']
    auth = (credentials['user'], credentials['password'])

    try:
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(auth[0], auth[1])
        server.sendmail( auth[0], to_number, message)
    except Exception as e:
        print("Failed to send daily message: " + str(e))

if __name__ == "__main__":
    send(email_text)