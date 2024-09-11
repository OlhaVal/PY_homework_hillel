import json
from pathlib import Path
import logging

new_dirctory = Path('json_files')

logging.basicConfig(
        filename='json_log.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s'
        )

def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        json.load(file)

json_files = [f for f in new_dirctory.iterdir() if f.suffix == '.json']

for file_name in json_files:
    try:
        read_json_file(file_name)
    except json.decoder.JSONDecodeError as e:
        logging.error(f"File with error JSONDecodeError: {file_name}")
