"""https://www.sec.gov/edgar/sec-api-documentation"""
import requests
import json


#submissions
submission_api_point = "https://data.sec.gov/submissions/CIK{cik_nbr}.json"

# companyconcept
account_payable_point = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik_nbr}/us-gaap/AccountsPayableCurrent.json"

# companyfacts
comp_fct_point = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik_nbr}.json"

# frames
frames_point = "https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY{year}Q{quarter}I.json"

APPL_CIK = "0000320193"


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
headers = {'User-Agent': user_agent}

print(submission_api_point.format(cik_nbr=APPL_CIK))
result = requests.get(submission_api_point.format(cik_nbr=APPL_CIK), headers=headers).json()
print(result)
 
   


