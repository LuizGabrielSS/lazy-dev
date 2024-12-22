from huggingface_hub import InferenceClient
from deep_translator import GoogleTranslator

from components.get_config import get_config

def classification_subject(subject:str) -> dict:

    configs = get_config()

    client = InferenceClient()

    labels = configs['classifications']

    subject_translated = GoogleTranslator(source='auto', target='en').translate(subject)

    result = client.zero_shot_classification(subject_translated,labels)

    return {
        'status':True,
        'result':result[0]['label']
    }
