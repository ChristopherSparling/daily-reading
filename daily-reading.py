import smtplib
import random as rnd
import pandas as pd
from hidden import credentials

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
    ['suit', 'rank', 'title', 'author', 'recommended_divisions',
       'division_word', 'completed']
    """

    bookList = pd.DataFrame(
        columns=['suit', 'card_rank', 'title', 'author', 'recommended_divisions',
       'division_word', 'completed']
       )
    books_df = pd.read_csv(books_csv, sep=',', header=0)
    incomplete_books_df = books_df[books_df.completed == False]

    for suit, groupdata in incomplete_books_df.groupby('suit', as_index=False):
        randint = rnd.randrange(len(groupdata))
        bookList = pd.concat([bookList,groupdata.iloc[[randint]]], ignore_index=True)
        # print(bookList)
    return bookList
        
def createMessage (bookList) :
    # """
    # readings format:
    #     book.title \n
    #     book.author \n
    #     book.suit|book.rank book.reccomended_divisions book.division_word \n
    #     \n
    # """
    # print('BookList:\n',bookList)
    # for index,book in bookList.iterrows():
    #     print(index, book.card_rank)
    # print( [book.rank for index, book in bookList.iterrows()]
    # )
    readings = "\n\n".join(
        [f"{book.title}\n{book.author}\n{book.suit}{book.card_rank}|{book.recommended_divisions} {book.division_word}" for index, book in bookList.iterrows()]
        )
    email_text = f"""
    Subject: Daily Readings
    {readings}
     """
    print(email_text)

if __name__ == "__main__":
    bookList = getBookList('books.csv')
    createMessage(bookList)