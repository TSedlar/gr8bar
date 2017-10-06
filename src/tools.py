from subprocess import PIPE, run
import json
import time


def time_fmt(fmt):
    '''
    Formats the current time with the given format
    :param fmt: The format to use
    '''
    return time.strftime(fmt)


def get_weather(zip_code):
    '''
    Gets the current weather temperature for the given zip code
    :param zip_code: The zip code of the area to query at
    '''
    yql_api = 'https://query.yahooapis.com/v1/public/yql?'
    query = 'q=select wind.chill from weather.forecast where woeid in ' \
            '(select woeid from geo.places(1) where text="%s")&format=json'
    query_url = yql_api + (query % (zip_code)).replace(' ', '%20')
    json = load_json(term('curl "%s"' % (query_url)))
    return json['query']['results']['channel']['wind']['chill']


def load_json(json_data):
    '''
    A json.loads alias
    :param json_data: The json string to load
    '''
    return json.loads(json_data)


def term(command):
    '''
    Executes the given command and returns its output
    :param command: The command to run
    '''
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout.strip()


def multi_apply(func, args):
    '''
    Applies the given function over a tuple of arguments
    :param func: The function/lambda to execute
    :param args: The tuple of arguments to execute the function over
    '''
    for arg in args:
        func(arg)
