import os                #lets you interact with the operating system (like working with file paths, environment variables, etc.)
from pathlib import Path #object-oriented way to handle filesystem paths (more convenient and readable than using os.path)
import logging           #used to record messages (logs) from your program, like debug info, warnings, or errors.


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "signLanguage"

#creating list of the files for the project

list_of_files = [
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",              #for writing some utility related functions
    f"{project_name}/utils/main_utils.py",
    "template/index.html", #because using flask
    ".dockerignore",
    "app.py", #end point
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

#creating folders and files using for loop

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")