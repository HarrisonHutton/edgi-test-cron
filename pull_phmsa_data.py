import requests

PHMSA_DATA_URL = "https://primis.phmsa.dot.gov/enforcement-documents/PHMSA%20Pipeline%20Enforcement%20Raw%20Data.txt"

data = requests.get(PHMSA_DATA_URL)

print(data.text)