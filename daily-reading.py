import smtplib
import random as rnd
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
    """
    books_csv keys:
    []'suit', 'rank', 'title', 'author', 'recommended_divisions',
       'division_word', 'completed']
    """
    bookList = []
    books_df = pd.read_csv(books_csv, sep=',', header=0)
    incomplete_books_df = books_df[books_df.completed == False]

    for suit, groupdata in incomplete_books_df.groupby('suit', as_index=False):
        randint = rnd.randrange(len(groupdata))
        print(suit, randint, len(groupdata))
        # print(randint, groupdata)
        # bookList.append(groupdata.iloc[[randint]])
        # print("randint:" ,randint, "\n", bookList)
        # print(suit, groupdata, len(groupdata))
        

if __name__ == "__main__":
    # send(email_text)
    print(getBookList('books.csv'))