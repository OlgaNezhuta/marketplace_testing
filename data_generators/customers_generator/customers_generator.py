from helpers.users_helpers import *
from data_generators.customers_generator.customers_test_data import *


REGISTRETION_URI = '/users'


def customers_generator():
    url = BASE_URL + REGISTRETION_URI
    for el in customers:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_customers = customers_generator()
