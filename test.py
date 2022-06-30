import json
from importlib import reload
import hashlib
from logging import raiseExceptions
import os
import importlib

GITHUB_RUN_NUMBER = os.getenv("GITHUB_RUN_NUMBER")

qwe = importlib.import_module(f"asd-{GITHUB_RUN_NUMBER}")