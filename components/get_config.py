import yaml

from components.logger import logger

def get_config():

    config_file = "settings.yaml"

    with open(config_file, 'r') as stream:
        
        try:
            
            config = yaml.safe_load(stream)

            logger.debug("Configurações obtidas com sucesso!")
            
            return config
        
        except yaml.YAMLError as exc:
        
            logger.error(f'Erro encontrado com o yaml: {exc}')

        except Exception as exc:

            logger.error(f'Erro não mapeado: {exc}')

    return None