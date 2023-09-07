import urequests
import utime

url = "https://raw.githubusercontent.com/LinkNatureAi/python_esp8266/main/blink"  # Modify the URL as needed

while True:
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print("Response Data:")
            print(response.text)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except urequests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    utime.sleep(5)
