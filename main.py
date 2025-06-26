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
    "StartDate": "2025-06-26",
    "EndDate": "2025-09-26",
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
  'activityid': 't1gpzjZxbt',
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
  'Cookie': 'OptanonAlertBoxClosed=2025-06-17T02:52:08.457Z; _gcl_au=1.1.134375990.1750128738; sbeSessionID=R2EdbQ0MATga88vtvjc0mx6z; visid_incap_2233116=fYcovuhuQiOjZcSIfxNL92HYUGgAAAAAQUIPAAAAAACY7EqajE6NTWWswJjk4sDQ; nlbi_2233116=nF3aWasN6wkPA3qCzW1W4gAAAAAE3k9Ef++tkr9xg9Aa6Ig5; _up=1.2.1559878977.1750128740; _fbp=fb.1.1750128740062.528776638114042139; __attentive_id=b9ef01a48a844140ab8e9593950116dc; __attentive_cco=1750128740088; _pin_unauth=dWlkPVpEZGlNemxqWWpZdFpESTNaQzAwTnprekxXRmpPVGd0Wm1NMk9XTXlOell4WXpKaw; nlbi_2233116_3112535=tKgfCJivfU7+ueInzW1W4gAAAAAvksWS2r//i6/y9jeoT4CK; _attn_bopd_=none; _li_dcdm_c=.westgateresorts.com; _lc2_fpi=a7ba6acc884a--01jxxwtn386nm367tkp2cnvjvc; _lc2_fpi_js=a7ba6acc884a--01jxxwtn386nm367tkp2cnvjvc; _li_ss=CgA; addshoppers.com=2%7C1%3A0%7C10%3A1750128746%7C15%3Aaddshoppers.com%7C44%3AOTMyYjEyOGI3NGZmNGY1YmJiOWZhMjgwNGU1NjFhZWU%3D%7Cee56c6b0abb5b477fefb5447d062a7c9360a71b4219834de952aa356f83de479; sa-user-id=s%253A0-6bf98041-d000-4126-7b1a-91b828ece4c0.7NNATMsB36mnGBZn%252FhcvOoDOChwY11If1tdvQVqZPo0; sa-user-id-v2=s%253Aa_mAQdAAQSZ7GpG4KOzkwLZFt5I.nzo0ky1be6xKb5r3%252FrlvJupFCRrJ7z7o2X5Sb4idti8; sa-user-id-v3=s%253AAQAKIBAyHVou9dhnd_uItXXiBQKkyzRQDvqNzAp3uETg0HEzEJIFGAIgh4-6vgY6BAaSRaJCBPYjsMg.fPYqMuyvLcPdcOIA8iWaSyUCgyKRm01DEQujjNSHaS0; QuantumMetricUserID_sabre=2b9eb56828c8f1b49ad55087554a83b3; incap_ses_713_2233116=YR/zB0MRrwBJTou/ExblCet4XWgAAAAA8Ngs6xCpxF5y0xZRGtkefQ==; reese84=3:focwC6rQuzpH76+LoQ+EIA==:teZRSTGy5x8POdFgR1BjUlBxlXOuabSKZQIzOp+5673Nh8FWzrx1w1buwFEehUgpCTxNj9Mc/MVn6sGjpVp92rQq/6ER2QftFUkkOXEyUwWYDzchcvED+BJiZ1VATxuhN3PWGRdymeRpB1hB7RGDzT3d7l7NLLp+ZsaDnciNo9ty9HZI5ZWfiEX/vg76zVMwMpZt35yxtQN/bGdFAQwXlV6GW0AuFqRzuyMy15ECDo8HAFY0lEPk3TNrCdIKlM6hyESZYHzPF49m/I6+UA5tE7yRfX7TEVUZPoNNHll9NF3VoDKcvpLZWubTmz/3+a/zHqve7+WNxqXpAxx6OVJ6SZ71vOJ6f1lGL9LLFdO4KUXlYVIlbWcn5vcjVl7xQJkxfp/6ZzasjqNDysQTToUjuwkOa95t1mNQL2g9Xd0ycC3yd/EEhyNo3nwIZa0DXa1vrOcgx0yVuE71jKyptK20GQgN0SoeyP+4v+Wo4SLdT5E=:SK3VfbnCbieLLjJxmmwBjlUazS9/gh94tG6V5GSngJw=; incap_ses_740_2233116=eThwds/oZDebHHPkOwJFCvN4XWgAAAAAPVjXWFZYq5v4tUci9rp6+w==; MgidSensorNVis=1; MgidSensorHref=https://www.westgateresorts.com/hotels/nevada/las-vegas/westgate-las-vegas-resort-casino/accommodations/; _pin_unauth=dWlkPVpEZGlNemxqWWpZdFpESTNaQzAwTnprekxXRmpPVGd0Wm1NMk9XTXlOell4WXpKaw; sa_ftses.5044=*; _clck=1i2fppj%7C2%7Cfx3%7C0%7C1994; __qca=P1-db30edca-5783-4430-b50f-d158f882b085; tag_user_id=0f8d1aba-a405-451a-98ca-7449a404dec3-1750956295607; tag_session=a656aca5-6979-4bc5-84c4-abbc71232973-c57f6b9c-b6fc-4db9-93db-82f8e8529e42; _rdt_uuid=1750128739779.efcf4b54-fc6f-408b-b724-b75ed6824221; SnapABugRef=https%3A%2F%2Fbook.westgateresorts.com%2F%3Farrive%3D06%252F27%252F2025%26depart%3D06%252F30%252F2025%26hotel%3D67577%26Chain%3D19007%26dest%3Dlas-vegas%26adult%3D1%26child%3D0%26rooms%3D1%26rate%3D%26promo%3D%26start%3Davailresults%26configcode%3D%26_ga-ft%3DaF15Bw.AA.AA.AA.AA.LXI0pAUOQpKHR37lnl2pvg..0%26_gl%3D1*11jrgh0*_gcl_au*MTM0Mzc1OTkwLjE3NTAxMjg3Mzg.*_ga*ODg2NTg3ODg5LjE3NTAxMjg2NjY.*_ga_Z5K7TGE5FM*czE3NTA5NTYyODYkbzQkZzAkdDE3NTA5NTYyOTUkajUxJGwwJGgw%20https%3A%2F%2Fwww.westgateresorts.com%2F; SnapABugHistory=3#; SnapABugUserAlias=%23; SnapABugVisit=1#1750956309; nlbi_2233116_2147483392=+8MCIt00L2Au+sbIzW1W4gAAAADrTO2W4jjdJ+leSgb3xxde; _gid=GA1.2.380503817.1750956309; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+26+2025+22%3A15%3A09+GMT%2B0530+(India+Standard+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=bc9516e9-a040-4d9c-b0a0-b59dea3f9297&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BDL&AwaitingReconsent=false; __attentive_session_id=310624a3ae1e467b8500cf491a98434a; _attn_=eyJ1Ijoie1wiY29cIjoxNzUwMTI4NzQwMDg3LFwidW9cIjoxNzUwMTI4NzQwMDg3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImI5ZWYwMWE0OGE4NDQxNDBhYjhlOTU5Mzk1MDExNmRjXCJ9Iiwic2VzIjoie1widmFsXCI6XCIzMTA2MjRhM2FlMWU0NjdiODUwMGNmNDkxYTk4NDM0YVwiLFwidW9cIjoxNzUwOTU2MzA5OTM2LFwiY29cIjoxNzUwOTU2MzA5OTM2LFwibWFcIjowLjAyMDgzMzMzMzMzMzMzMzMzMn0ifQ==; __attentive_dv=1; _gbsess=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiLU8zQ182dGNIMG96bFlUMW9VTGkiLCJzIjpudWxsLCJydCI6bnVsbCwiYyI6eyJ1c2VJRCI6dHJ1ZSwidG9zIjp0cnVlLCJjYXJ0IjpbXSwicWYiOm51bGwsImlwIjoxMCwiYXVkaWVuY2UiOnRydWUsImJ1c2luZXNzIjp0cnVlLCJtZXNzYWdpbmciOnRydWUsInYiOjF9LCJpYXQiOjE3NTA5NTYzMTEsImV4cCI6MTc1MDk1OTkxMSwiYXVkIjoidHJhY2suZ2V0Z29ib3QuY29tIiwiaXNzIjoiLU8zQ182dGNIMG96bFlUMW9VTGgifQ.JmBnFiItQvAcFnp5SJNXiORhmD8Tg4sSVYGY2n9JG6I; nlbi_2233116_2849146=8+vfJk00XimsYdWPzW1W4gAAAACRc44jSYYKaGi5NshP4ndo; __attentive_pv=1; __attentive_ss_referrer=https://www.westgateresorts.com/; _clsk=sqtc91%7C1750956317594%7C2%7C1%7Cwww.clarity.ms%2Feus-f%2Fcollect; sa_ftid.5044=2d7234a4-050e-4292-8747-7ee59e5da9be.1750128665.3.1750956318.1750314117.7a943c1e-e70c-4ab7-b764-9192244420ae.d3ce9773-09f6-4b59-9231-e2a48b128742.cde5760b-ad58-40f7-a5d1-51fdaaf86b98.1750956285072.6; _ga=GA1.1.886587889.1750128666; _ga_Z5K7TGE5FM=GS2.1.s1750956286$o4$g1$t1750956321$j25$l0$h0; _ga_902GY8W2RT=GS2.1.s1750956321$o4$g0$t1750956321$j60$l0$h0; AWSALBTG=4IgYbpjuh2XX3TIRV5fqmwu0Ie2b/0qsbAAyfCKhSYSSP0wi6PmF1MJAuFaAB7Nu08ahqDkbPhZknJRrct6BxYHrLq9s4Ra/Jb0daEImHFcF4/DpiT8LRNUKPF/XmGoY5UuOgAF2ZQfsPkkaZNH2gdtM1MZMO02kxzcVCXigH87/L7AR+wA=; AWSALBTGCORS=4IgYbpjuh2XX3TIRV5fqmwu0Ie2b/0qsbAAyfCKhSYSSP0wi6PmF1MJAuFaAB7Nu08ahqDkbPhZknJRrct6BxYHrLq9s4Ra/Jb0daEImHFcF4/DpiT8LRNUKPF/XmGoY5UuOgAF2ZQfsPkkaZNH2gdtM1MZMO02kxzcVCXigH87/L7AR+wA=; AWSALB=oJ4LXFaQ3iAvrBdSajJ4rbMiXj4HTHgIVA+guqKGm9apdesmFQQ6vgT0j27O6jeQnc9B3N1qqJgAh0Rr/b9zkodXwwSQ6iwa9csmzP7hVkos8N1GaiflRhUESLNs; AWSALBCORS=oJ4LXFaQ3iAvrBdSajJ4rbMiXj4HTHgIVA+guqKGm9apdesmFQQ6vgT0j27O6jeQnc9B3N1qqJgAh0Rr/b9zkodXwwSQ6iwa9csmzP7hVkos8N1GaiflRhUESLNs; MgidSensorNVis=3; MgidSensorHref=https://book.westgateresorts.com/?_ga-ft=aF15Bw.AA.AA.AA.AA.LXI0pAUOQpKHR37lnl2pvg..0&_gl=1*11jrgh0*_gcl_au*MTM0Mzc1OTkwLjE3NTAxMjg3Mzg.*_ga*ODg2NTg3ODg5LjE3NTAxMjg2NjY.*_ga_Z5K7TGE5FM*czE3NTA5NTYyODYkbzQkZzAkdDE3NTA5NTYyOTUkajUxJGwwJGgw&adult=1&arrive=2025-06-27&chain=19007&child=0&currency=USD&depart=2025-06-30&dest=LAS-VEGAS&hotel=67577&level=hotel&locale=en-US&productcurrency=USD&rooms=1&start=availresults; QuantumMetricSessionID_sabre=34ee696cf9f9ea69745a558cf759041a; apisession=MDAxMjF-Z1JEazF6c1lyQ1VGTFJIdUNDL3p5bVhlMERuQXRQSTNJeDQ5Mk42d0tBbHRmdEcrUzdzQmwvb2k5ekRkUnhyV0hZajFaWWlRNTFmKzdzZklNaFNpTjM2cWJFK1VySlkwbC9WTitTTTAxNGNBTkNQTjFmK2pnSFc5Z1N4R0crQStHS201aUs2bHlnVHpxcjlIaENnRFB5NVByVEp5YnJsODIyMmZ0amtTaDZ4Z21mVFo5U2MrKzJXd2svbkdMcE5ZSnkwbElNMHlNMGRQeUhxVnRxdE92ZVQ4NDZnWHlCZ0ZXTUNaQnZ0RUNQWlRBZHlZS2ZkU0g1QnFIL0l6Rmp4RVYxVzZqaklwMnNnSlliMmpkUXZVMlFFcUVVWTU2c2RlTHdCSExweGxGU1dhR1RjcjFxUjhGY1haMFltYVF6bXk; apisession=MDAxMjF-VXZXQndGZ0FMT3pxVmZ2Y1AyR1NsRHRhYUpOVGppdDFTRm4vZ054LytiQU9IRzFKTy95eXQ1WW0yQ3BJcnJVcGFtWC9QOU9JV2RZSGFKSVdsU0JNckdROXo3bWRJWU5MV0N3cStUSkFQV2dtME43cWEzcTREM1hsNU5jTjRZTjRxRDcyK3IvOVhuRDIwdC84QWVGbWlqUWhQSUhkKzZFNWV4dlc1Y2JCL2hhQkp3V0d4NHk4OWZaeE5NQmFXbUpvKzJuTk5OSjc5L2pOcHBTOFo3K0YxREIxdkJaY2ZaaHNCQ2NIZnBUQ2E1TnBOZFFsUFdnOVVKQ0FKNjNMWkVVdFozUGZmTWFhNGJ3RUl1OEVjRjBCQW94YmxxZFQrQUtTTjg3elJySFZuc2Z0MU5jQXZXSUUvcjZEaU9GMWVlSjg; visid_incap_2233116=j53zmGyFRhCu/TklJ/LYS7AJUGgAAAAAQUIPAAAAAABeH+IKL6lmYJ3jUWk512t3'
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
    dataFrame.to_csv("temp.csv", index=False)
    print("Data saved to westgateHotel_availability.csv")