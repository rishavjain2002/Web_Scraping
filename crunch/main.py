import requests
import pandas as pd

url = "https://www.crunch.com/load-clubs"

payload = {}
headers = {
  'accept': 'application/json',
  'accept-language': 'en-GB,en;q=0.9',
  'priority': 'u=1, i',
  'referer': 'https://www.crunch.com/locations',
  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
  'Cookie': 'locale=en; _gcl_au=1.1.241502697.1748929080; _ga=GA1.1.1077151094.1748929080; ajs_anonymous_id=0b846098-7de8-4a0e-8475-f9a0822b7791; _fbp=fb.1.1748929080257.711580507291061763; _pin_unauth=dWlkPU5XUmtZakl6TkdVdE9ERmpNeTAwTWpJeExUZ3dOVFF0TkRoaE1UTXlOVFE0TVRCaQ; _scid=LntSKnHc5yRxeMKCIem7_TGAHqmyVRfJ; ip=14.194.5.222; __adroll_fpc=cbe1ba9d8bc28c92a0cb628ce82d4d07-1748929080894; _clck=1juurmt%7C2%7Cfwg%7C0%7C1980; ndp_session_id=4584e386-79a2-4406-88fe-149c2c04d5d3; _ScCbts=%5B%5D; __hstc=223736004.c1a0f78b1f3c84f44700532828ba141c.1748929082697.1748929082697.1748929082697.1; hubspotutk=c1a0f78b1f3c84f44700532828ba141c; __hssrc=1; _sctr=1%7C1748889000000; lat=28.4597; long=77.0282; country_code=1269750; geo_located_club_id=696; geo_located_club_slug=abq-atrisco; geo_located_club_name=Albuquerque+Atrisco; geo_located_club_type=base_club; browsing_club_id=696; browsing_club_slug=abq-atrisco; browsing_club_name=Albuquerque+Atrisco; browsing_club_type=base_club; browsing_club_city=Albuquerque; browsing_club_state=NM; browsing_club_franchisee_name=Undefeated+Tribe+Operating+Company+LLC+%28Tony+Hartl%29; _rdt_uuid=1748929080208.a9e7c6c8-7cc6-427a-8681-c9a91f05b71a; _uetsid=e9298150403c11f0b9f117b283ef842c; _uetvid=e92987c0403c11f09874716a76a7cd4a; _clsk=1mtvb4b%7C1748929101549%7C2%7C1%7Cl.clarity.ms%2Fcollect; __ar_v4=DOI3WJWKORBV5GXQXWQAPI%3A20250603%3A3%7C5U6ZA65PSJDJ7H6BW2FYUL%3A20250603%3A3%7CDKR2FV2J6ZHCREZGIOQTEE%3A20250603%3A3; __hssc=223736004.2.1748929082697; _crunch_web_session=Zm01VVlOdVZjUUJDdTRUZ2lsMVdWUWRBME0zbnV3VUVZcjA0ZG1iS3A0akdaNXlub2lwZDE0ZXhOeUQyOHRFOHludGpYaDJBWGR0cklSck5IYUJrdGZwMVZlRlhWK1R0WkZLb0VEeUtEa000UW15YnhHcW5ZblArRzNycWMrTGdmTm9tNUJYYlYxVkdnMU1jREhMb2VnPT0tLVBKWFcvalBHTFJkVGYrbFZsbkVUV1E9PQ%3D%3D--acdabfd660d0f2541e6b64acb20298c4cb409081; _scid_r=KPtSKnHc5yRxeMKCIem7_TGAHqmyVRfJ7NHIPQ; _tq_id.TV-09723609-1.08ed=ec058030f628c755.1748929081.0.1748929111..; _ga_4GV7GFESVB=GS2.1.s1748929080$o1$g1$t1748929110$j30$l0$h0; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jun+03+2025+11%3A08%3A30+GMT%2B0530+(India+Standard+Time)&version=202409.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0441018e-dba9-4502-bb3b-28c73d640b5b&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&intType=1&geolocation=IN%3BHR&AwaitingReconsent=false; OptanonAlertBoxClosed=2025-06-03T05:38:30.643Z; _crunch_web_session=QkZoRXJXRklJdDlFc0dvb01HL0h1SG9iUk1EOG14WU02VjVyaVpZblBMQnFUd2I1MG5OZTFUTUViSUd5YmlrY253SGk4NmxZYU4yZ20rTVJWTzdrR3VIaXJ1N1FweU9iZlZ6eWNZTHlXT1J5VDJ3S0p6Um1rekpnazBrU1FlU1p6ZnpHWkc4UFduWm44TlZyWW1uN0hRPT0tLXJCaGpMcE1UaXV5QUt6RHlSTi9xRWc9PQ%3D%3D--0820696dbc1a5d65d7d14bcebcf29d99e9581dc4'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json() 

clubs = data.get("clubs", [])
rows = []
for club in clubs:
    address = club.get("address", {})
    # Extract first contact email if available
    contacts = club.get("contacts", [])
    first_contact_email = contacts[0].get("email") if contacts else None

    rows.append({
        "id": club.get("id"),
        "title": club.get("name"),
        "latitude": club.get("latitude"),
        "longitude": club.get("longitude"),
        "address": address.get("address_1"),
        "address2": address.get("address_2"),
        "city": address.get("city"),
        "state": address.get("state"),
        "zip": address.get("zip"),
        "country": address.get("country_code"),
        "phone": club.get("phone"),
        "email": club.get("email") or first_contact_email,
        "facebook_url": club.get("facebook_url"),
        "facebook_handle": club.get("facebook_handle"),
        "instagram_url": club.get("instagram_url"), 
        "instagram_handle": club.get("instagram_handle")
    })

# Create DataFrame
df = pd.DataFrame(rows)
df.to_csv("crunch_gym.csv")
print(df)