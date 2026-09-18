import os

env_file = os.getenv('GITHUB_ENV')
output_file = os.getenv('GITHUB_OUTPUT')

allRepos = [
   {"name":"repo1"},
   {"name":"repo2"},
   {"name":"repo3"},   
]

allRepoNames=[]

for repo in allRepos:
  allRepoNames.append(repo['name'])
  allRepoNamesList = ','.join(allRepoNames)
  print("List:", allRepoNamesList)

with open(env_file, "a") as myfile:
    myfile.write(f"TEST={allRepoNamesList}")
    
with open(output_file, "a") as myfile:
    myfile.write(f"TEST={allRepoNamesList}")