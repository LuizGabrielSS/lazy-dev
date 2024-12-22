from datetime import datetime
from email.header import decode_header

def get_important_fields(email_message) -> dict:

    date_format = "%a, %d %b %Y %H:%M:%S %z"

    sender = email_message['From'].split('<')

    subjet = decode_header(email_message['Subject'])

    decoded_text = ''.join(part.decode(charset or 'utf-8') if isinstance(part, bytes) else part for part, charset in subjet)

    important_fields = {
        'SenderEmail': sender[1].replace('>', ''),
        'SenderName': sender[0],
        'Subject': decoded_text,
        'Content-Type': email_message['Content-Type'],
        'Date': datetime.strptime(email_message['Date'], date_format)
    }

    return important_fields