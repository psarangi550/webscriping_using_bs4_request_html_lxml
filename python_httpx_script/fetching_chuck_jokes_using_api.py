import httpx #importing the httpx module
import time
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
}

#her creating the connection pool for this application

def get_data():
    with httpx.Client(headers=headers) as client:
        jokes=[]
        for i in range(10):
            resp=client.get("https://api.chucknorris.io/jokes/random")
            if resp.status_code == 200:
                jokes.append(resp.json()["value"])
            else:
                print("something went wrong")
        return jokes

if __name__ == "__main__":
    t1=time.perf_counter()
    print(get_data())
    t2=time.perf_counter()
    print(f"total time is {t2-t1}")