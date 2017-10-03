from subprocess import PIPE, run
import json
import time


def time_fmt(fmt):
    '''
    Formats the current time with the given format
    :param fmt: The format to use
    '''
    return time.strftime(fmt)


def load_json(json_data):
    '''
    A json.loads alias
    :param json_data: The json string to load
    '''
    return json.loads(json_data)


def x_workspace():
    '''
    Retrieves the current workspace number using xprop
    '''
    return int(term('xprop -root _NET_CURRENT_DESKTOP | grep -o "[0-9]*"'))


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
