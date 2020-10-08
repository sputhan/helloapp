
import os
import sys
import requests

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

#print(get_env_variable("ADDR"))

def main():
    #print(sys.argv)
    url = f'http://{get_env_variable("ADDR")}/{sys.argv[1]}'
    #print(url)
    res = requests.get(url)
    print(res.text)


if __name__ == '__main__':
    main()