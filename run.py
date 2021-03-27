import requests
import json

print("You can add your script rules here to execute them with the GH workflow.")

print("Example:")

print(f"Getting Brazil Covid-19 datas.")

response = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Brazil")

datas = response.json()

all_country = datas["All"]

confirmed_cases = all_country["confirmed"]
recovered_cases = all_country["recovered"]
deaths = all_country["deaths"]

print("🤒 Confirmed cases:", confirmed_cases)
print("🥳 Recovered cases:", recovered_cases)
print("😢 Deaths:", deaths)
