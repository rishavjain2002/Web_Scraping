import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def fetch_availability(start_date, end_date):
    url = "https://book.westgateresorts.com/gw/product/v1/getLeadAvailability"

    payload = json.dumps({
    "Version": "1",
    "Criterion": {
        "listAllocationBlocks": True,
        "NumRooms": 1,
        "Currency": {
        "Code": "USD"
        },
        "ChannelList": {
        "PrimaryChannel": {
            "code": "WEB"
        },
        "SecondaryChannel": {
            "code": "GC"
        }
        },
        "StartDate": start_date,
        "EndDate": end_date,
        "LengthOfStay": 1,
        "LoyaltyList": [],
        "onlyCheckRequested": False,
        "AgentInfo": {},
        "AccessCode": {},
        "RoomStay": {
        "GuestCount": [
            {
            "ageQualifyingCode": "Adult",
            "numGuests": 1
            },
            {
            "ageQualifyingCode": "Child",
            "numGuests": 0,
            "Ages": []
            }
        ],
        "RateList": [],
        "RoomList": [],
        "RateFilterList": []
        }
    },
    "HotelList": [
        {
        "id": "67577"
        }
    ],
    "UserDetails": {
        "Preferences": {
        "ResponseOptions": "ReturnAllocationBlocks"
        }
    },
    "Chain": {
        "id": "19007"
    }
    })
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'activityid': 'uKhiee9aju',
    'authorization': 'ApiKey MDAxMjF+dVNKZlBxNkNpazBlb2Q5SkEwL0xmVXBEVmJiQWFBcnZtT3FHUkN1RnJqZHFxZFNFR1pmWmFFSGFHWnNpSEN6MDRyZnVoa1cvdXAwazc2M2IyZWI5UXc9PQ==',
    'content-type': 'application/json',
    'origin': 'https://book.westgateresorts.com',
    'priority': 'u=1, i',
    'referer': 'https://book.westgateresorts.com/?_ga-ft=aF15Bw.AA.AA.AA.AA.LXI0pAUOQpKHR37lnl2pvg..0&_gl=1*11jrgh0*_gcl_au*MTM0Mzc1OTkwLjE3NTAxMjg3Mzg.*_ga*ODg2NTg3ODg5LjE3NTAxMjg2NjY.*_ga_Z5K7TGE5FM*czE3NTA5NTYyODYkbzQkZzAkdDE3NTA5NTYyOTUkajUxJGwwJGgw&adult=1&arrive=2025-06-27&chain=19007&child=0&currency=USD&depart=2025-06-30&dest=LAS-VEGAS&hotel=67577&level=hotel&locale=en-US&productcurrency=USD&rooms=1&start=availresults',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Cookie': 'OptanonAlertBoxClosed=2025-06-17T02:52:08.457Z; _gcl_au=1.1.134375990.1750128738; sbeSessionID=R2EdbQ0MATga88vtvjc0mx6z; visid_incap_2233116=fYcovuhuQiOjZcSIfxNL92HYUGgAAAAAQUIPAAAAAACY7EqajE6NTWWswJjk4sDQ; nlbi_2233116=nF3aWasN6wkPA3qCzW1W4gAAAAAE3k9Ef++tkr9xg9Aa6Ig5; _up=1.2.1559878977.1750128740; _fbp=fb.1.1750128740062.528776638114042139; __attentive_id=b9ef01a48a844140ab8e9593950116dc; __attentive_cco=1750128740088; _pin_unauth=dWlkPVpEZGlNemxqWWpZdFpESTNaQzAwTnprekxXRmpPVGd0Wm1NMk9XTXlOell4WXpKaw; nlbi_2233116_3112535=tKgfCJivfU7+ueInzW1W4gAAAAAvksWS2r//i6/y9jeoT4CK; _attn_bopd_=none; _li_dcdm_c=.westgateresorts.com; _lc2_fpi=a7ba6acc884a--01jxxwtn386nm367tkp2cnvjvc; _lc2_fpi_js=a7ba6acc884a--01jxxwtn386nm367tkp2cnvjvc; _li_ss=CgA; addshoppers.com=2%7C1%3A0%7C10%3A1750128746%7C15%3Aaddshoppers.com%7C44%3AOTMyYjEyOGI3NGZmNGY1YmJiOWZhMjgwNGU1NjFhZWU%3D%7Cee56c6b0abb5b477fefb5447d062a7c9360a71b4219834de952aa356f83de479; sa-user-id=s%253A0-6bf98041-d000-4126-7b1a-91b828ece4c0.7NNATMsB36mnGBZn%252FhcvOoDOChwY11If1tdvQVqZPo0; sa-user-id-v2=s%253Aa_mAQdAAQSZ7GpG4KOzkwLZFt5I.nzo0ky1be6xKb5r3%252FrlvJupFCRrJ7z7o2X5Sb4idti8; sa-user-id-v3=s%253AAQAKIBAyHVou9dhnd_uItXXiBQKkyzRQDvqNzAp3uETg0HEzEJIFGAIgh4-6vgY6BAaSRaJCBPYjsMg.fPYqMuyvLcPdcOIA8iWaSyUCgyKRm01DEQujjNSHaS0; QuantumMetricUserID_sabre=2b9eb56828c8f1b49ad55087554a83b3; incap_ses_713_2233116=YR/zB0MRrwBJTou/ExblCet4XWgAAAAA8Ngs6xCpxF5y0xZRGtkefQ==; incap_ses_740_2233116=eThwds/oZDebHHPkOwJFCvN4XWgAAAAAPVjXWFZYq5v4tUci9rp6+w==; MgidSensorNVis=1; MgidSensorHref=https://www.westgateresorts.com/hotels/nevada/las-vegas/westgate-las-vegas-resort-casino/accommodations/; _pin_unauth=dWlkPVpEZGlNemxqWWpZdFpESTNaQzAwTnprekxXRmpPVGd0Wm1NMk9XTXlOell4WXpKaw; _clck=1i2fppj%7C2%7Cfx3%7C0%7C1994; __qca=P1-db30edca-5783-4430-b50f-d158f882b085; tag_user_id=0f8d1aba-a405-451a-98ca-7449a404dec3-1750956295607; SnapABugRef=https%3A%2F%2Fbook.westgateresorts.com%2F%3Farrive%3D06%252F27%252F2025%26depart%3D06%252F30%252F2025%26hotel%3D67577%26Chain%3D19007%26dest%3Dlas-vegas%26adult%3D1%26child%3D0%26rooms%3D1%26rate%3D%26promo%3D%26start%3Davailresults%26configcode%3D%26_ga-ft%3DaF15Bw.AA.AA.AA.AA.LXI0pAUOQpKHR37lnl2pvg..0%26_gl%3D1*11jrgh0*_gcl_au*MTM0Mzc1OTkwLjE3NTAxMjg3Mzg.*_ga*ODg2NTg3ODg5LjE3NTAxMjg2NjY.*_ga_Z5K7TGE5FM*czE3NTA5NTYyODYkbzQkZzAkdDE3NTA5NTYyOTUkajUxJGwwJGgw%20https%3A%2F%2Fwww.westgateresorts.com%2F; SnapABugHistory=3#; _gid=GA1.2.380503817.1750956309; __attentive_dv=1; nlbi_2233116_2849146=8+vfJk00XimsYdWPzW1W4gAAAACRc44jSYYKaGi5NshP4ndo; MgidSensorHref=https://book.westgateresorts.com/?_ga-ft=aF15Bw.AA.AA.AA.AA.LXI0pAUOQpKHR37lnl2pvg..0&_gl=1*11jrgh0*_gcl_au*MTM0Mzc1OTkwLjE3NTAxMjg3Mzg.*_ga*ODg2NTg3ODg5LjE3NTAxMjg2NjY.*_ga_Z5K7TGE5FM*czE3NTA5NTYyODYkbzQkZzAkdDE3NTA5NTYyOTUkajUxJGwwJGgw&adult=1&arrive=2025-06-27&chain=19007&child=0&currency=USD&depart=2025-06-30&dest=LAS-VEGAS&hotel=67577&level=hotel&locale=en-US&productcurrency=USD&rooms=1&start=availresults; QuantumMetricSessionID_sabre=34ee696cf9f9ea69745a558cf759041a; incap_ses_737_2233116=iAXzXkjmmBOSE0Hc8Fk6CjuBXWgAAAAA4auKAJVKLA4WsGeNnt/1qQ==; reese84=3:lMvHx7KuQqUtCHnZe83Tcg==:wwgy6A4OZ0hpg+gjVcqtsyWBFoFyEvL9JnX/6WyceT+BZ5emDD7w6Bt4EV5LqKmfEMuBtElwN6LmeJOf1Sy9yIDSO/b46dmxJR8WbsK9d2XJ8fzQtzKBw1jVK59BzCevSKFLG7ROoTQqQA0CzdY1kSU2mGTR3TE8htRCNFZ66mxoI7nBLuZbZSEBuzH0DpRCaL5BRXFHlUh+3Z7yO3whGdposbaMuNQKIcA+rYSBG0wUCcPUgWuO2Ea/9XD2JsVVk5ZxAw9NxPGlNlT2Nxjpi+4wzWRxKi/pp0UnZPSSTBp+0sg9wcnYGFf//4TUl9L0um7H0Qc6Zd/aCgUxF7Y9MEl7dVh3InHUjA6YJTYahZA4agyJ7VgempITO9BF93ktY/oIpDPDHPosoBG1SNGq1LdoZV1Fn29raD60OM8SjVNGVWjYl5YPjof9aeFnigJmGdI0EhNfp7ccsun1aiu65w==:Hmh+DoAAxr4C25kRei4lp7+sVmiaTraBbzUrkiutWZg=; nlbi_2233116_2147483392=xNFaPstSlznjT9M5zW1W4gAAAADeM6BtMBnroWHR2AFmLg+i; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+26+2025+22%3A50%3A02+GMT%2B0530+(India+Standard+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=bc9516e9-a040-4d9c-b0a0-b59dea3f9297&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BDL&AwaitingReconsent=false; _rdt_uuid=1750128739779.efcf4b54-fc6f-408b-b724-b75ed6824221; SnapABugUserAlias=%23; SnapABugVisit=2#1750956309; __attentive_session_id=e98d35878bc34a969cacdb255d5f6aec; _attn_=eyJ1Ijoie1wiY29cIjoxNzUwMTI4NzQwMDg3LFwidW9cIjoxNzUwMTI4NzQwMDg3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImI5ZWYwMWE0OGE4NDQxNDBhYjhlOTU5Mzk1MDExNmRjXCJ9Iiwic2VzIjoie1widmFsXCI6XCJlOThkMzU4NzhiYzM0YTk2OWNhY2RiMjU1ZDVmNmFlY1wiLFwidW9cIjoxNzUwOTU4NDAzNjE4LFwiY29cIjoxNzUwOTU4NDAzNjE4LFwibWFcIjowLjAyMDgzMzMzMzMzMzMzMzMzMn0ifQ==; __attentive_pv=1; __attentive_ss_referrer=https://www.westgateresorts.com/; AWSALBTG=nOc9O8paV9bpLu9bthVAVpuQeYCfQc20+8CcmqFJGQExpnV859lxX25SN8+dMiGJfmtwO9L89pmYPVq4icTqEVPTJ0GD16v7cF3Urd6t4KJTxF2G5c7QfYZiXiIlztpfCSwgAcW+YRcrJnMzzqdkAjKRoLKnir9xofdwVgqeC03YtNbXj0U=; AWSALBTGCORS=nOc9O8paV9bpLu9bthVAVpuQeYCfQc20+8CcmqFJGQExpnV859lxX25SN8+dMiGJfmtwO9L89pmYPVq4icTqEVPTJ0GD16v7cF3Urd6t4KJTxF2G5c7QfYZiXiIlztpfCSwgAcW+YRcrJnMzzqdkAjKRoLKnir9xofdwVgqeC03YtNbXj0U=; AWSALB=vLqRMzC9AS0Puti1tEith3fpCuPE72YycejkAkGotyW6UhkTmOHn/hmx8/XdXyAUX1FOgNtPIcJ/nuWVJTHI3zWYMka46W6bG+c5RjjoZ+TaBBYYEY5pF4Qhnt83; AWSALBCORS=vLqRMzC9AS0Puti1tEith3fpCuPE72YycejkAkGotyW6UhkTmOHn/hmx8/XdXyAUX1FOgNtPIcJ/nuWVJTHI3zWYMka46W6bG+c5RjjoZ+TaBBYYEY5pF4Qhnt83; sa_ftses.5044=*; sa_ftid.5044=2d7234a4-050e-4292-8747-7ee59e5da9be.1750128665.4.1750958405.1750956356.bf7b89a5-a5bc-4b3e-a05c-ae5f3e9d3763.7a943c1e-e70c-4ab7-b764-9192244420ae.5b5f855c-a197-4448-9993-c66f43d8071b.1750958404641.3; _clsk=1m5hvpm%7C1750958404767%7C1%7C1%7Cwww.clarity.ms%2Feus2-d%2Fcollect; _gbtest=2025-06-26T17:20:05.554Z; _gbsess=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiLU8zQ182dGNIMG96bFlUMW9VTGkiLCJzIjpudWxsLCJydCI6bnVsbCwiYyI6eyJ1c2VJRCI6dHJ1ZSwidG9zIjp0cnVlLCJjYXJ0IjpbXSwicWYiOm51bGwsImlwIjoxMCwiYXVkaWVuY2UiOnRydWUsImJ1c2luZXNzIjp0cnVlLCJtZXNzYWdpbmciOnRydWUsInYiOjF9LCJpYXQiOjE3NTA5NTg0MDYsImV4cCI6MTc1MDk2MjAwNiwiYXVkIjoidHJhY2suZ2V0Z29ib3QuY29tIiwiaXNzIjoiLU8zQ182dGNIMG96bFlUMW9VTGgifQ.LFN8axxbeFl89Wu89_xer7Nqqbk_HcYKmJnQb5vPFsQ; _ga=GA1.1.886587889.1750128666; _ga_902GY8W2RT=GS2.1.s1750958399$o5$g1$t1750958407$j52$l0$h0; _ga_Z5K7TGE5FM=GS2.1.s1750958399$o5$g1$t1750958407$j52$l0$h0; MgidSensorNVis=2; apisession=MDAxMjF-VXZXQndGZ0FMT3pxVmZ2Y1AyR1NsQjM2cWV3RmpTdGcwWCs4UUl1VmZwSjY0bXhCV3pGYXZjSnNOU3FQTjd6YXUxOTRkM3VGV01iVkNEWFFObVJWMG5ML1U5NFZ0L1NRRkVFM0FyZkUraGxldmlqWkZ5ZFMwN0xPTnVzOXJSQnR1N01xQlJqVHlSaUdKUkZDc2ltenFmRzh6K0xFWG92UktZejJqeUpPWDg2aGNodXBBMVlBTjMwTW9mYW5XYXg3MzE3S3I3VXVWRFJNV2R3bUFHdllsMlcrSXNZeUI3ZUFUY1hvanJDZ2I2a1IybHhaZGpPalo5cmZMM1lodkJLN3N4clFIcmFDR2ZrYjAreG9peGZuY3VrSmxRK0hJREl5RW9ZTkF5bjJDckp4U0didkJVa3l1cmgxcVdLRzhIL2E; apisession=MDAxMjF-VXZXQndGZ0FMT3pxVmZ2Y1AyR1NsSDlBMGI3RlJZbEFMZkFzbTliT2NQMWtuOVVPUjNwdWRhYTZQdk1TV0U3UW5SSTBFdG15ZmlzREpmTGk5NC9uSWNqQjZJRFJqQ3F0NkpuVjVyWW0wUmNqOXBEbVh2OFQ4SEFRWW5iSys3aE1ScTRKRUlxSTNraW0wN2xDaENXa3lhL1BsdmpraUF6ZCtyNkl3eHRVUkNtS2crRWcrU2Q4SU5LblViVUpNczU3aE54R2JVeVJtWG1YYnVIa2VMM3pacmVldW9qSlVkQi9sS05odG1qOVBBNElpT0RhZ2ZSMUtCMTUyU2dsQTJKSHZvWGlDS1RYMDc5M3VIU3Bhd2gxSTdsdFJ2cEYyVU54cFdTNi82Z3RnWVpTTDR3enNkcEc2K2RiZk5LVFVKa1Y; visid_incap_2233116=j53zmGyFRhCu/TklJ/LYS7AJUGgAAAAAQUIPAAAAAABeH+IKL6lmYJ3jUWk512t3'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    results = []

    if response.status_code == 200:
        data = response.json()
        for record in data.get("LeadAvailabilityList", []):
            arrival = record.get("ArrivalDate")
            departure = record.get("DepartureDate")
            prices = record.get("Price", [])
            min_price = next((p for p in prices if p.get("Type") == "Minimum"), None)
            amount = min_price.get("AmountWithFees") if min_price else None

            results.append({
                "start_date": arrival,
                "end_date": departure,
                "AmountWithFees_Minimum": amount
            })
    else:
        print(f"Error {response.status_code}: {response.text}")

    return results

def fetch_until_exhausted():
    all_results = []
    batch_size_days = 60
    today = datetime.today()
    current_start = today

    while True:
        current_end = current_start + timedelta(days=batch_size_days)
        start_str = current_start.strftime('%Y-%m-%d')
        end_str = current_end.strftime('%Y-%m-%d')

        print(f"Fetching from {start_str} to {end_str}...")
        batch_results = fetch_availability(start_str, end_str)

        if not batch_results:
            print("No more data available. Stopping.")
            break

        all_results.extend(batch_results)
        current_start = current_end + timedelta(days=1)

    return all_results

data = fetch_until_exhausted()

if data:
    df = pd.DataFrame(data)
    df.to_csv("AllHotelPriceUntilAvailable.csv", index=False)
    print("Saved to westgate_availability_dynamic.csv")
else:
    print("No availability data found.")
