import requests
import json
import pandas as pd


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
    "StartDate": "2025-06-16",
    "EndDate": "2025-06-30",
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
  'accept-language': 'en-GB,en;q=0.9',
  'activityid': 'y2kX2i1DVa',
  'authorization': 'ApiKey MDAxMjF+dVNKZlBxNkNpazBlb2Q5SkEwL0xmVXBEVmJiQWFBcnZtT3FHUkN1RnJqZHFxZFNFR1pmWmFFSGFHWnNpSEN6MDRyZnVoa1cvdXAwazc2M2IyZWI5UXc9PQ==',
  'content-type': 'application/json',
  'origin': 'https://book.westgateresorts.com',
  'priority': 'u=1, i',
  'referer': 'https://book.westgateresorts.com/?_ga-ft=aE_97Q.AA.AA.AA.AA.yfurMp1LQDCNR7XP_e7Mog..0&_gl=1*awrk1c*_gcl_au*NTU0NjQ0MDg1LjE3NTAwNzI4MTQ.*_ga*MTAxMDAwMDM3NS4xNzUwMDcyNzIz*_ga_Z5K7TGE5FM*czE3NTAwNzI3MjIkbzEkZzEkdDE3NTAwNzI4MTMkajYwJGwwJGgw&adult=1&arrive=2025-06-16&chain=19007&child=0&currency=USD&depart=2025-06-17&dest=LAS-VEGAS&hotel=67577&level=hotel&locale=en-US&productcurrency=USD&rooms=1&start=availresults',
  'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'Cookie': '_ga=GA1.1.1010000375.1750072723; _ga_Z5K7TGE5FM=GS2.1.s1750072722$o1$g1$t1750072813$j60$l0$h0; _gcl_au=1.1.554644085.1750072814; sbeSessionID=T8EpUYhWLIej7eBWGNSamtqX; visid_incap_2233116=dFQ9xD2FT7O7xzU1M/xh7O39T2gAAAAAQUIPAAAAAACv+aTWhXPktAglgas4A8ua; nlbi_2233116=jbMRUwoIbS+pbKDIzW1W4gAAAAAFQzW6MQauN6eiJBcUJj0e; nlbi_2233116_3112535=F3IbXuPx+ApSCOxxzW1W4gAAAABxkelC4t+YZFRzz0YdrU6l; _up=1.2.769698324.1750072816; QuantumMetricSessionID_sabre=148cabf9a5f501972439aa6c25870058; QuantumMetricUserID_sabre=947d10d38b667d45dcdae7278618ef2b; nlbi_2233116_2849146=pQP3FAAmHDuiYnhizW1W4gAAAACgBGgbNFl0VNuePvhQ0AIS; incap_ses_713_2233116=5kpHSuww3hz9v9dsERblCfcIUGgAAAAAB+7c3xZDHJQS48fBrvk//Q==; AWSALBTG=tDSu2seeNF/185IK5NXAniFSg/9P+6931aiEkR+/OGkYONvlIAVYtSUZmeKWMAHuYvPpRkFQs13kw4gDWqGMSgsZ6XAFEGXlWf+B7IM+CPfKTCpmlMweSVNUtDWVLc85KK342PHUvADWhnbK6DfInCdyoBSrS4KLdCxYB0Nq0kAyCV/2fBE=; AWSALBTGCORS=tDSu2seeNF/185IK5NXAniFSg/9P+6931aiEkR+/OGkYONvlIAVYtSUZmeKWMAHuYvPpRkFQs13kw4gDWqGMSgsZ6XAFEGXlWf+B7IM+CPfKTCpmlMweSVNUtDWVLc85KK342PHUvADWhnbK6DfInCdyoBSrS4KLdCxYB0Nq0kAyCV/2fBE=; AWSALB=rB8d6eIVBgG814tRngEcroI7YWRBcnqYvbHK5IgphCjX0Ap4C8d/cocl5DYXDMgKl2OcoVEdD9JnZUgj+mGmOdqlaUdCtQNxU05DADWHmFPUNVueP7z5f8FGEeSL; AWSALBCORS=rB8d6eIVBgG814tRngEcroI7YWRBcnqYvbHK5IgphCjX0Ap4C8d/cocl5DYXDMgKl2OcoVEdD9JnZUgj+mGmOdqlaUdCtQNxU05DADWHmFPUNVueP7z5f8FGEeSL; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jun+16+2025+17%3A48%3A11+GMT%2B0530+(India+Standard+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9f5da6c6-8680-4a0a-8100-807611edb626&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0005%3A0%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false; sa_ftid.5044=c9fbab32-9d4b-4030-8d47-b5cffdeecca2.1750072721.2.1750076374.1750072909.4cd8eb3d-3613-4aad-829a-31fd5a1e2e40.b8e9c6b4-7025-4589-ab7c-803b8f2f2de0.7e0be59c-8b57-4bb6-80e4-40207bed4dad.1750075697640.11; apisession=MDAxMjF-VXZXQndGZ0FMT3pxVmZ2Y1AyR1NsR1B6M2dLMmFWeUVTd3c2MTlYNlF2UE1HcTAwWktVUWxLNHd1blhteTJLaGQwYnBNYjUwb2VxSWRQYnovSWlEWWVTRUZFN0tFeW5FdlFFSDhPZWkzUFczTE10ZnJsTHBWajdTbFQxaGlJZExtNEtPWjVGbmYwY1ZFejRzM2tZbUMyM0Q3ZlNISCs4amd0ek90RU1GVVYvY0hMc2NnNWE3dnhsSlB1ZkJteXg2Tm5rREJJclZXQWdXWGx3MTdWbDN0UHN5cCs0cndKVVFOWjhIa1FFZ2gwaDB1bFNueEpHeURkeFl6L1pwUW5DTXJBK2dRbnlBZE5oa3Z1bVlVd3lEeFRBeDhLZlJ2dFVzdmdiVVdHYlR3ZHRWVTgwTk1wa3lEeHpVRGpxUGx3THQ; nlbi_2233116_2147483392=7D2CQZ6fURPym8tdzW1W4gAAAACFFztqspTvunpf6rkNLa0h; reese84=3:a0c37MljD4JPL7LKtL2EWA==:yJx0Lgo8kMRDcpFn2rJkci8YddVwmCDeMX8ffuokHspy5+rT+y7bih5CeBl60V3y007IfH35FI/zl2mCGSyO4hFOxtDkk8cXzUlaBUwj/otSO80nA1Xn2N0D18fmw9pWETlXHA67YRiSk/fTH0Wrt4vXHp4CQwhAs3NmHDLnkmMe30b8ozmkkEsMaJxBPAaAOOw/XlV/QUl1Rif+9H9+DItDkdTLNBoznIHTCoZb8+2/cdKBBYz/cCImrBxqPGyFarU2DHVPAeA5QhVCloRrfwLhPT+2frInPcyyh7hDBksqHpc0CidUPpmX+rG6LjYlAoo88eDS3uK/OthugBb1QI1qnKkY25sGV1VsBPyhqUHIFMAkfRzNeolTEm4Y+OTUVnCmh2PhqcU69sRq2A5xRCt8frv0b8EVn5MHNRPx2Ji1RERbENAI/2MFC/aPwyadW+1CJ8mGGbg1kZT59bWjBDqzLK9/dC5rlQ8+ZZzhGL4=:EHaqHsU2H25bFcJjOxSExbEDfUGdoksub7IP9/mkHr8=; apisession=MDAxMjF-VXZXQndGZ0FMT3pxVmZ2Y1AyR1NsSGJET3grNzYvWmZyc1Npb0llaHp6VDU3eXN3VDZQSW9UOWV4U1pqL24yeVVKVC9STGhZdktlVGtVNjBhZ0lSUHVZL0kyU1dMME9LZmw4QzY5b0JEaTFVWThxSnExN2x2T2t5bVBveEhya3lreXdNZkZHUlU0WTZadzJPZGhtbzJYYW1Jd3J2KzVEak9Celk3ZVVOdkFNZW1HVHJyV280SVRyZUI5VUhlTmFVWElzNVJPVXN3MHVvWGdtNGdUakRRWlhOcG5YNHViUWhEZVkyS1VmNllZeStvcnNwWVk4Ti83ZWdsbUtwS2xoQUFndU4zUmpvVkdiVWNlYkQ3NlJpUGRIWlJZTzFzbktNMUYzNkEwcGhQVk5hc2dMK3FUMDAwd2tMR0s5U1dyUWs; incap_ses_713_2233116=kKf0V604kApQTd5sERblCeQPUGgAAAAA3JT12DTgb3d2jjPECAZFUg==; nlbi_2233116_3112535=8s9wZIy9jSSSzKvlzW1W4gAAAAABo80I13300xJRBA8xeLy2; visid_incap_2233116=j53zmGyFRhCu/TklJ/LYS7AJUGgAAAAAQUIPAAAAAABeH+IKL6lmYJ3jUWk512t3'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

results = []
if response.status_code == 200:
    data = response.json()
    
    results = []
    for record in data.get("LeadAvailabilityList", []):
        start_date = record.get("ArrivalDate")
        end_date = record.get("DepartureDate")
        prices = record.get("Price", [])
        
        # Find price with Type == "Minimum"
        min_price = next((p for p in prices if p.get("Type") == "Minimum"), None)
        amount_with_fees = min_price.get("AmountWithFees") if min_price else None
        
        results.append({
            "start_date": start_date,
            "end_date": end_date,
            "AmountWithFees_Minimum": amount_with_fees
        })
    
    for r in results:
        print(f"From {r['start_date']} to {r['end_date']}: Minimum AmountWithFees = {r['AmountWithFees_Minimum']}")
else:
    print(f"Failed to get data: {response.status_code}")
    print(response.text)


if not results:
    print("No results found.")
else:
    dataFrame = pd.DataFrame(results)
    print(dataFrame)
    dataFrame.to_csv("westgateHotel_availability.csv", index=False)
    print("Data saved to westgateHotel_availability.csv")