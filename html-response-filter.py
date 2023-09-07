import urequests
import time
import gc

def make_https_request():
    url = "https://example.com"  # Replace with your target URL
    response = urequests.get(url)
    return response.text

def extract_p_tags(data):
    # Find all occurrences of <p>...</p> in the data
    p_tags = []
    start = 0
    while True:
        start = data.find("<p>", start)
        if start == -1:
            break
        end = data.find("</p>", start)
        if end == -1:
            break
        p_tags.append(data[start:end+4])
        start = end + 4
    return p_tags

def print_received_data():
    data = make_https_request()
    p_tags = extract_p_tags(data)
    for tag in p_tags:
        print("Received data:", tag)

while True:
    try:
        print_received_data()
    except Exception as e:
        print("Error:", e)

    # Free up memory (optional)
    gc.collect()

    # Wait for 2 seconds
    time.sleep(2)
