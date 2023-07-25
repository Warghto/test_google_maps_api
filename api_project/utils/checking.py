# Methods for Control of every requestttt
import json

from requests import Response

class Checking():

    # Method for control status code
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        print("Status code is Fine: " + str(response.status_code))
        if response.status_code != status_code:
            print("Something went wrong, ur status code is: " + str(response.status_code))



    # Method for control reqierent fields in answer of request

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields are good")

    # Method for control znachenij v pole vvoda

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Checked: " + field_name)

    @staticmethod
    def check_json_search_word(response: Response, field_name, search_word):
        check = response.json()

        check_info = check.get(field_name)
        if search_word in check_info:
            print("WORD IS FINE: " + field_name)
        else:
            print("SLOVO NE NAJDENO: " + field_name)