
import requests
from robot.libraries.BuiltIn import BuiltIn

def hello(param):
    url = f'http://app:8080/{param}' #todo:get url from env
    return requests.get(url).text

def test_hello(param, expected_message):
    try:
        assert hello(param)==expected_message
    except AssertionError:
        BuiltIn.fail(f'received message: {hello(param)}, expected message: {expected_message}')


