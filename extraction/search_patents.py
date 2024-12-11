import requests
import json
import time
import os
import xml.etree.ElementTree as ET
import utils
from dotenv import load_dotenv

load_dotenv()
CLIENT_KEY = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
KEYWORDS = os.getenv("KEYWORDS")
output_path = "search_patents"   
os.makedirs(output_path, exist_ok=True)

# keywords = ['Low Carbon Hydrogen', 'Energy Hydrogen']

# access_token = utils.get_access_token(CLIENT_KEY, CLIENT_SECRET)
# if access_token:
#     for keyword in keywords:
#         search_results = utils.search_patents(access_token, keyword, 1, 100, 2000)
#         with open(os.path.join(output_path, f"{keyword}_2001_4000.json"), "w") as f:
#             json.dump(search_results, f, indent=4, ensure_ascii=False)


cpcs = [KEYWORDS]
start = 2000
batch_size = 100
max_results = 4000

access_token = utils.get_access_token(CLIENT_KEY, CLIENT_SECRET)
if access_token:
    for cpc in cpcs:
        search_results = utils.search_patents_by_cpc(access_token, cpc, start, batch_size, max_results)
        with open(os.path.join(output_path, f"{cpc}_{start}_{max_results}.json"), "w") as f:
            json.dump(search_results, f, indent=4, ensure_ascii=False)