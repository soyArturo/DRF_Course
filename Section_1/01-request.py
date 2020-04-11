import requests


def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("There was an error!")
    print("Content-Type: ", response.headers['Content-Type'])
    data = response.json()
    print("JSON Data: ", data)


if __name__ == "__main__":
    main()
