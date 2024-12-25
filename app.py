from huggingface_hub import login,auth_list

from components.logger import logger
from components.timer_decorator import timer
from components.get_secret import get_secret

from src.report_email.init import report_email
from src.create_folders.init import create_project

@timer('Função principal')
def main():

    # Realizando login na lib huggingface_hub

    logger.info('Iniciando login na lib huggingface_hub')

    try:

        login(
            token=get_secret('token_huggingface')
        )

        logger.info('Login realizado com sucesso')

    except Exception as e:

        logger.error('Erro ao realizar login na lib huggingface_hub')

        logger.error(e)

        return False

    # result = report_email()

    # logger.info(result)

    create_project()

main()
