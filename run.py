import requests
import json

print("You can add your script rules here to execute them with the GH workflow.")

print("Example:")

print(f"Getting Brazil Covid-19 datas.")

response = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Brazil")

datas = response.json()

print(datas)
