import urequests
import time
import gc

def make_https_request():
    url = "https://example.com"  # Replace with your target URL
    response = urequests.get(url)
    return response.text

def extract_p_tags(data):
    start_tag = "<p>"
    end_tag = "</p>"
    start = data.find(start_tag)
    end = data.find(end_tag)

    while start != -1 and end != -1:
        p_data = data[start+len(start_tag):end]
        print("Received data within <p> tags:", p_data)
        start = data.find(start_tag, end)
        end = data.find(end_tag, start)

def print_received_data():
    data = make_https_request()
    extract_p_tags(data)

while True:
    try:
        print_received_data()
    except Exception as e:
        print("Error:", e)

    # Free up memory (optional)
    gc.collect()

    # Wait for 3 seconds
    time.sleep(3)
