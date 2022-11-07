from duneanalytics import DuneAnalytics
import pandas as pd
from matplotlib import pyplot as plt
import os
from dotenv import load_dotenv


# initialize client
load_dotenv()
username = os.getenv('username')
password = os.getenv('password')

# login
dune = DuneAnalytics(username, password)

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

# query
query_id = 1539675
result_id = dune.query_result_id(query_id)
data = dune.query_result(result_id)

df = pd.DataFrame(data['data']['get_result_by_result_id'])

data2 = pd.json_normalize(df['data'], max_level=0)
print(data2)






