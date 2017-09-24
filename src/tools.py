from subprocess import PIPE, run
import json
import time


def time_fmt(fmt):
    return time.strftime(fmt)


def load_json(json_data):
    return json.loads(json_data)


def x_workspace():
    return int(term('xprop -root _NET_CURRENT_DESKTOP | grep -o "[0-9]*"'))


def term(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout.strip()
