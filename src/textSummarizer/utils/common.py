import os

import sys
sys.path.append("D:/My_Work/UdeMy/MyCompleteDataScience/NLP_Project_with_HuggingFace_Transformers")
from ensure_patch import ensure_annotations
#from ensure import ensure_annotations

from box.exceptions import BoxValueError
import yaml

from src.textSummarizer.logging import logger
from box import ConfigBox

from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args: path_to_yaml (str): path like input
    Raises: ValueError: if yaml file is empty
                    e: empty file
    Returns: ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml File: {path_to_yaml} Loaded Successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("Yaml file is Empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Successfully Created Directory at: {path}")
