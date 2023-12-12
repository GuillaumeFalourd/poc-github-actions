import os

def save_output(name: str, value: str): 
    with open(os.getenv('GITHUB_OUTPUT'), "a") as output_file:
        output_file.write(f"{name}={value}")

save_output("TEST1", "VALUE1")
save_output("TEST2", "VALUE2")
save_output("TEST3", "VALUE3")