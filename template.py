import os
import pathlib
import logging

# Configure logging to display INFO level messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name and a list of files to be created
project_name = "mlopsproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# Loop through each file path in the list
for filepath in list_of_files:
    # Convert the filepath string into a Path object for easier manipulation
    filepath = pathlib.Path(filepath)
    
    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)

    # If the file's directory is not empty (i.e., it's not the current directory)
    if filedir != "":
        # Create the directory if it doesn't exist, including any necessary parent directories
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass  # No content to write, just creating an empty file
        logging.info(f"Creating empty file: {filepath}")

    else:
        # If the file already exists, log a message indicating its presence
        logging.info(f"{filename} already exists")
