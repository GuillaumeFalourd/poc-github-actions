import os

env_file = os.getenv('GITHUB_ENV')
output_file = os.getenv('GITHUB_OUTPUT')

hello='hello'

with open(env_file, "a") as myfile:
    myfile.write(f"TEST={hello}")
    
with open(output_file, "a") as myfile:
    myfile.write(f"TEST={hello}")