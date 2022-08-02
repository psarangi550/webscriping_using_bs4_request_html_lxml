import requests #importing the requests module 


def get_data():
    jokes=[]
    with requests.Session() as session:
        for i in range(10):
            resp=session.get("https://api.chucknorris.io/jokes/random")
            if resp.status_code == 200:
                jokes.append(resp.json()["value"])
    return jokes


if __name__ == "__main__":
    print(get_data())
