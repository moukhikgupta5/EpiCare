import time
import requests
from celery import shared_task

# def get_eeg_data():
#     api_url = "http://127.0.0.1:9797/"
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         json_data = response.json()
#         return json_data['Data'] 
#     return None

# def detect_seizure(eeg_data):
#     api_url = 'http://127.0.0.1:3254?eegdata=[' + eeg_data + ']'
#     response = requests.get(api_url)
#     json_data = response.json()
#     return json_data[0]

@shared_task
def fetch_eeg_data():
    while True:
        # Fetch EEG data (replace this with your actual data fetching mechanism)
        # eeg_data = get_eeg_data()
        print(1)
        # Send data to seizure detection API
        # seizure_detected = detect_seizure(eeg_data)

        # if seizure_detected:
        #     # Call API if seizure is detected
        #     call_seizure_api()

        #     # Save seizure history in the database
        #     save_seizure_history(eeg_data)

        time.sleep(1)  # Adjust the time interval as needed
