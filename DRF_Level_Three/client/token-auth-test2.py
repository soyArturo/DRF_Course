import requests


def client():
    # cred = {"username": "admin", "password": "123456789"}
    #
    # response = requests.post("http://localhost:8000/api/rest-auth/login/",
    #                          data=cred)

    response = requests.get("http://localhost:8000/api/profiles")

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
