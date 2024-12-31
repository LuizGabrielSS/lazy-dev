from components.logger import logger

from huggingface_hub import InferenceClient

from deep_translator import GoogleTranslator

def generate_text(text:str):

    client = InferenceClient()

    try:
        # Envia o texto para a geração
        response_generated = client.text_generation(
            prompt=GoogleTranslator(source='auto', target='en').translate(text), 
            max_new_tokens=500,
            repetition_penalty=1.3,
            )
        
        logger.info("Texto gerado com sucesso:")
        
        logger.info(GoogleTranslator(source='auto', target='pt').translate(response_generated))
    
    except Exception as e:
    
        logger.error("Erro ao chamar o método text_generation.")
    
        logger.error(e)