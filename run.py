import requests
import json

print("You can add your script rules here to execute them with the GH workflow.")

print("Example:")

url = "https://api.github.com/repos/ZupIT/ritchie-cli/collaborators"
headers = {
        "Accept": "application/vnd.github.v3+json",
        }
response = requests.get(
        url = url,
        headers = headers
        )

datas = response.json()

if "documentation_url" not in datas:
    for d in datas:
        print(d["login"] + " - " + d["url"])

else:
    print("No collaborator for this repository.")
