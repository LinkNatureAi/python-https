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
    
    if start != -1 and end != -1:
        return data[start+len(start_tag):end]
    else:
        return None

def print_received_data():
    data = make_https_request()
    p_data = extract_p_tags(data)
    
    if p_data is not None:
        print("Received data:", p_data)

while True:
    try:
        print_received_data()
    except Exception as e:
        print("Error:", e)

    # Free up memory (optional)
    gc.collect()

    # Wait for 2 seconds
    time.sleep(2)
