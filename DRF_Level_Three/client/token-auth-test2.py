import requests


def client():
    data = {"username": "resttest",
            "email": "test@rest.com",
            "password1": "testpass12",
            "password2": "testpass12"}

    response = requests.post("http://localhost:8000/api/rest-auth/registration/",
                             data=data)

    # response = requests.get("http://localhost:8000/api/profiles")

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
