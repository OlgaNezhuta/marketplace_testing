from helpers.users_helpers import *
from data_generators.products_generator.products_test_data import *


CREATE_PRODUCT_URI = '/products'


def products_generator():
    url = BASE_URL + CREATE_PRODUCT_URI
    token = login(LOGIN_CREDS)
    for el in products:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json", "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE
    logout(token)


new_products = products_generator()



