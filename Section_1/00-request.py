import requests


def main():
    response = requests.get("https://excel.network/")
    print("Status code: ", response.status_code)


if __name__ == "__main__":
    main()
