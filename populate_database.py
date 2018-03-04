import json
import pandas as pd
import requests

BASE_URL = "https://blockchain-team-badass.herokuapp.com"
PARKING_SPOT_URL = BASE_URL + "/parkingspots/"
STATE_URL = BASE_URL + "/state/"

headers = {'Content-type': 'application/json'}

def convert_timestamp(old_stamp):
    day, time = old_stamp.split("_")
    month, day, year = day.split("/")
    hour, minute = time.split(":")

    year = "20" + str(year)

    return "%s-%s-%sT%s:%s:%sZ" % (year, month, day, hour, minute, "00")

def populate_spots(data):
    unique_parking_spots = data.drop_duplicates(subset="parking_spot_id")

    for index, spot in unique_parking_spots.iterrows():
        body = {
            "uuid": spot['parking_spot_id'],
            "latitude": spot['coordinate_tag_x'],
            "longitude": spot['coordinate_tag_y'],
            "name": ""
        }
        data_json = json.dumps(body)

        try:
            response = requests.post(PARKING_SPOT_URL, data=data_json, headers=headers)
            print(response.text)
        except Exception as e:
            print(e)

def populate_states(data):
    for index, state in data.iterrows():
        if state['car_present'] == "True":
            occupied = True
        else:
            occupied = False

        body = {
            "occupied": occupied,
            "parking_spot": state['parking_spot_id'],
            "time_in": convert_timestamp(state['start_time_stamp']),
            "time_out": convert_timestamp(state['end_time_stamp'])
        }
        data_json = json.dumps(body)

        try:
            response = requests.post(STATE_URL, data=data_json, headers=headers)
            print(response.text)
        except Exception as e:
            print(e)

def main():
    data = pd.read_csv("raw_data.csv")

    print("Populating spots\n")
    populate_spots(data)

    print("Populating states\n")
    populate_states(data)

if __name__ == '__main__':
    main()
