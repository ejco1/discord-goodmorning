import requests
import random
import json

with open(r"config.json", 'r') as config:
    config_data = json.load(config)

urls = config_data["urls"]
auth = {'authorization': config_data["authKey"]}
variations = config_data["variations"]
lengthOfArray = len(variations) - 1

def main():
    for url in urls:
        requests.post(url, headers = auth, data = {'content': variations[random.randint(0,lengthOfArray)]})

if __name__ == "__main__":
    main()

