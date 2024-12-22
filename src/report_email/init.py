import imaplib
import email

from src.report_email.get_data import get_important_fields
from src.report_email.classification import classification_subject

from components.get_secret import get_secret
from components.get_config import get_config
from components.timer_decorator import timer
from components.logger import logger

@timer('Relatório de e-mail')
def report_email():

    email_user = get_secret('email_user')

    email_password = get_secret('email_password')

    configs = get_config()

    mail = imaplib.IMAP4_SSL(configs['email']['imap_server'])
    
    mail.login(email_user, email_password)

    mail.select('inbox')

    status, messages = mail.search(None, 'UNSEEN')

    if status != 'OK':

        logger.error('Erro ao buscar e-mails não lidos')

        return {
            'status':False,
            'status_msg': status
        } 
    
    messages_ids = messages[0].split()

    results = []

    if len(messages_ids) == 0:

        logger.info('Nenhum e-mail não lido')

    for msg_id in messages_ids:
        
        status, data = mail.fetch(msg_id, '(RFC822)')

        if status == 'OK':

            try:
                # Obter o conteúdo do e-mail
                raw_email = data[0][1]

                email_message = email.message_from_bytes(raw_email)

                fields = get_important_fields(email_message)

                fields['classification'] = classification_subject(fields['Subject'])

                results.append(fields)

            except Exception as e:

                logger.error(f'Erro ao tentar ler o email:{e}')

                email_message = None
        
        else:

            logger.error('Erro ao tentar acessar o email')

            return {
                'status':False,
                'status_msg': status
            } 
        
    mail.logout()

    return results