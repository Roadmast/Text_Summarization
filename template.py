import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/common.py",
    f"src/{project_name}/looging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/confihuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/init.py",
    "config/config.yml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reasearch/trails.ipynb"


]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Created empty file: {filepath}")


    else:
        logging.info(f"File: {filepath} already exists.")