#! /usr/bin/env python3

import json
import os, sys


def configuration() -> dict:
    """
    Helper function which reads the configuration file (config.json)
    and returns its contents as a dictionary.

    :return: (Dictionary) -
        A dictionary representing the contents of the configuration file.
    """

    if os.path.isfile("config.json"):
        with open("config.json") as json_file:
            data = json.load(json_file)
            return data
    else:
        sys.exit(f"Configuration file not found. Please add it and try again.")
