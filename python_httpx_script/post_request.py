import httpx  # importing the httpx module
import json

data = {
    "cp_number": "CP000ZZZ",
    "sne_id": 232546,
    "trs_area": "L/NWS"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
}

resp = httpx.post("http://127.0.0.1:9823/home/", data=json.dumps(data))
if resp.status_code == 200:
    print(resp)