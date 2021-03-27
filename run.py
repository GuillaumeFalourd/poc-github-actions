import requests
import json

print("✅ You can add your script rules here to execute them with the GH workflow.")

### SCRIPT SAMPLE BELOW

print(f"💡 \033[36mExample: Getting Brazil Covid-19 datas\033[0m")

response = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Brazil")

if response.status == 200:
    datas = response.json()

    country_summary = datas["All"]

    print("🤒 Confirmed cases:", country_summary["confirmed"])
    print("🥳 Recovered cases:", country_summary["recovered"])
    print("😢 Deaths:", country_summary["deaths"])

else:
    print("❌ Couldn't get Brazil Covid-19 datas")
    print (response.status_code, response.reason)