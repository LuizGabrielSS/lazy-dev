from cookiecutter.main import cookiecutter

# Componentes
from components.get_config import get_config
from components.timer_decorator import timer
from components.logger import logger
from components.get_secret import get_secret


@timer('Criação de template')
def create_project():

    configs = get_config()

    output_dir = get_secret('output_dir')

    print(output_dir)

    cookiecutter(
        template=configs['github_templates']['api'],
        output_dir=output_dir,
        no_input=True,
        extra_context={
            'project_name': 'test_via_python',
        }
    )

