import os

def save_output(name: str, value: str): 
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
        print(f'{name}={value}', file=output_file)

save_output('TEST1', 'VALUE1')
save_output('TEST2', 'VALUE2')
save_output('TEST3', 'VALUE3')