import json
import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

# Creating updating and deleting locations
@allure.epic("Test create place")
class Test_create_place():


    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):


        print("Method POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET POST")
        result_get = Google_maps_api.checking_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09' )
        # "address": "29, side layout, cohen 09",

        print("Method PUT")
        result_put = Google_maps_api.updating_location(place_id)
        Checking.check_status_code(result_put, 200)
        print(result_put.status_code)
        Checking.check_json_token(result_put, ['msg'])
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        #
        print("Method GET PUT")
        result_get = Google_maps_api.checking_updated_place(place_id)
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'address', 'Bandery street, AYAYAYYA' )

        print("Method DELETE")
        result_delete = Google_maps_api.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        print(result_delete.status_code)
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Method GET DELETE")
        result_get = Google_maps_api.checking_deleted_place(place_id)
        Checking.check_status_code(result_get, 404)
        print(result_get.status_code)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_search_word(result_get, 'msg', " failed")


        print("Test Creating updating and deleting locations was fine")