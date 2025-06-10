import requests
import pandas as pd

import requests

url = "https://www.anytimefitness.co.in/wp-json/anytime/v1/map-locations"

payload = {}
headers = {
  'sec-ch-ua-platform': '"macOS"',
  'Referer': 'https://www.anytimefitness.co.in/find-gym/',
  'x-dtpc': '9$571227228_497h12vPSSKFUICCDKKIBEMVPPGOMVHOFDPUFFL-0e0',
  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Cookie': 'dtCookie=v_4_srv_6_sn_4B1B9850D706636F64941EAB2A83C693_perc_100000_ol_0_mul_1_app-3Ab2adb474e34b7e36_0_rcs-3Acss_0; incap_ses_707_1706395=Je2lN7ButzHmdwOu/cTPCWmMPmgAAAAA6P8w7UQ3hrYFeB0i6crrLA==; incap_ses_740_1706395=+/2ocXJGpFjcrSdDNwJFCqmMPmgAAAAA7yGs6aRZOeyfTUdhHnUctA==; incap_ses_742_1706395=UH4gR8zrcWrYllRyZR1MCmIsP2gAAAAAfxwpajGFHOxwtFUTDgbS4A==; nlbi_1706395=LbAdI8kmiWiZ2bGCHtLK/gAAAAD8KHapRdNeIkj6OhgOgBrT; visid_incap_1706395=Wz/Bz7QiTlCJ5KAW6ydiSC9nPmgAAAAAQUIPAAAAAABdrDtx3qHmGhegi1zvO+OT'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json() 
print(data)
rows = []
for gym in data:
    main_content = gym.get("content", {})

    rows.append({
        "latitude": gym.get("latitude"),
        "longitude": gym.get("longitude"),
        "address": main_content.get("address"),
        "address2": main_content.get("address_2"),
        "city": main_content.get("city"),
        "state": main_content.get("state"),
        "country": main_content.get("country"),
        "zip": main_content.get("zip"),
        "id" : main_content.get("number"),
        "contact_number": main_content.get("phone"),
        "email_id": main_content.get("email"),
        "gym_name": main_content.get("title")  
    })

# Create DataFrame
df = pd.DataFrame(rows)
# df.to_csv("anytimefitness_gym.csv")
df.to_csv("anytimefitness_gym2.csv", index=False, encoding='utf-8-sig')
print(df)