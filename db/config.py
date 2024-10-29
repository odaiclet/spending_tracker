import os
from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # Get the directory of the current file (config.py)
    base_dir = os.path.dirname(__file__)
    # Create the absolute path to database.ini
    filepath = os.path.join(base_dir, filename)

    parser = ConfigParser()
    parser.read(filepath)

    # Debug print to check sections
    print("Sections found:", parser.sections())

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file.")

    return db
