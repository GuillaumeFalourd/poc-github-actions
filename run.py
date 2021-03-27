import requests
import json

print("You can add your script rules here to execute them with the GH workflow.")

print("Example:")

url = "https://api.github.com/repos/octocat/hello-world/collaborators"
headers = {
        "Accept": "application/vnd.github.v3+json",
        }
response = requests.get(
        url = url,
        headers = headers
        )

datas = response.json()
collaborators = []

for d in datas:
    collaborators.append(d["login"])

print(collaborators)