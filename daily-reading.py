import smtplib
import pandas as pd
from hidden import credentials


# email_text = """
# Subject: %s
# Daily Readings: 
# %s
# %s
# """ % (subject, "\n ".join(), )


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

def getBookList(books_csv):
    books_df = pd.read_csv(books_csv, sep=',', header=0)
    print(books_df)
    print(books_df.keys())



if __name__ == "__main__":
    # send(email_text)
    print(getBookList('books.csv'))