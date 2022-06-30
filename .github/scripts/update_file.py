import os
import re

print("START")

WORKSPACE = os.getenv("WORKSPACE")
FILE = f"{WORKSPACE}/test.py"
GITHUB_RUN_NUMBER = os.getenv("GITHUB_RUN_NUMBER")

with open(FILE, "r") as file:
    content = file.read()

importlib = f'qwe = importlib.import_module(f"asd-{GITHUB_RUN_NUMBER}")'

content = re.sub(r"qwe = importlib.import_module(f\"asd-\*\")", importlib, content)

with open(FILE, "w") as file:
    file.write(content)

print(content)

print("END")