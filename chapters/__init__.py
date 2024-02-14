import json
import os

DEFAULT_DIR = os.path.dirname(__file__)


def read_data(file_name: str):
    data_file_path = os.path.join(DEFAULT_DIR, "data", file_name)
    with open(data_file_path, "r") as file:
        data = json.load(file)
    return data
