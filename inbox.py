import imaplib
import email

host = 'imap.gmail.com'
username = 'kenajunwa@gmail.com'
password = 'zscrmhkgqfzsychx'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

_, search_data = mail.search(None, 'UNSEEN')

print(search_data)