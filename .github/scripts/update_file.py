import os
import re

print("START")

WORKSPACE = os.getenv("WORKSPACE")
GITHUB_RUN_NUMBER = os.getenv("GITHUB_RUN_NUMBER")

FILE = f"{WORKSPACE}/test.py"

with open(FILE, "r") as file:
    content = file.read()

importlib = f'qwe = importlib.import_module("asd-{GITHUB_RUN_NUMBER}")'

content = re.sub(r"#placeholder1", importlib, content)

with open(FILE, "w") as file:
    file.write(content)

#print(content)

print("END")