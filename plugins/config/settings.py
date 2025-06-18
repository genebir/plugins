from dotenv import load_dotenv
import yaml
import os
from typing import Dict

load_dotenv()

def load_settings() -> Dict:
    env = os.environ.get('ENV', 'dev')
    with open(f'config/{env}.yaml', 'r') as f:
        config_text = f.read()
    
    for k, v in os.environ.items():
        config_text = config_text.replace(f"${{{k}}}", v)
    
    config = yaml.safe_load(config_text)

    return config