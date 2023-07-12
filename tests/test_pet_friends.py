import pytest
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_new_pets_with_photo(name = 'Alex', age = '8', animal_type = 'Кот', pet_photo = "images/FRxmI1tx5Kg.jpg"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_pets():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.post_api_pets_with_photo(auth_key, "new pet", "кот", "3", "images/-YVoi8nlTNU.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_api_pets(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_update_pets (name = "sdgaadgfad", age = "2314", animal_type = 'what'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, age, animal_type)


    assert status == 200
    assert result['name'] == name



