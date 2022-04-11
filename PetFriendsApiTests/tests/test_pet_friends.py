from api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    """Проверка API ключа и возвращения статуса 200, а так же наличия слова KEY"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверка запроса всех питомцев возвращает не пустой список"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверка добавления питомца с корректными данными"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """Удаление питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Обновление информации о питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_creat_pet_simple(name="Клюватый", animal_type="Пернатый", age="1"):
    """Добавление питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_pets_photo(pet_photo='images/img1.jpg'):
    """Добавление фото к созданному ранее питомцу"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets'])>0:
        pet_id= my_pets['pets'][0]['id']
        status, result = pf.post_add_photo_pets(auth_key, pet_id, pet_photo)
        assert status == 200
        print (status)
    else:
        raise Exception("список питомцев пуст")

def test_no_valid_api_key(email="fhhhfhhrpkdsjpk@asfijdasoifj.com",password="sdafdadfq113245r"):
    """Попытка получения API ключа с неверными данными"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_add_pets_text_age(name='Усатый', animal_type='Полосатый',
                           age='много', pet_photo='images/img2.jpg'):
    """Добавление питомца с текстовым значение возраста"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age

def test_delete_no_valid_id_pets():
    """Удление питомца с несуществуещим id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.delete_pet(auth_key,"my_pets")

    pet_id = "no_valid_pet_id"
    status, result = pf.delete_pet(auth_key,pet_id)
    assert status == 200

def test_add_photo_no_corect_id_pets(pet_photo='images/img2.jpg'):
    """Добавление фото к питомцу с несуществуещем id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_photo_pets(auth_key, 'pet_id', pet_photo)
    assert status == 200

def test_name_pets_simbol(name='1111', animal_type='222222',
                          age='3333333333', pet_photo='images/img1.jpg'):
    """Создание питомца, вместо имени, породы и возраста-цифры"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name