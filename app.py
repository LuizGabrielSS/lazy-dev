from huggingface_hub import login

from components.logger import logger
from components.timer_decorator import timer
from components.get_secret import get_secret

from src.report_email.init import report_email

@timer('Função principal')
def main():

    result = report_email()

    logger.info(result)

main()
