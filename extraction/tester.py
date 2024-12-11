import os
import utils
from dotenv import load_dotenv

load_dotenv()
CLIENT_KEY = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

access_token = utils.get_access_token(CLIENT_KEY, CLIENT_SECRET)
patent_number = 'US2004163997'

response = utils.get_patent_biblio(patent_number, access_token)
if isinstance(response, str):
    print('No patent found')
elif response:
    print(f'Response: {response}')
    biblio_dict = utils.xml_to_dict(response)
    print(biblio_dict)