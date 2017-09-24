from subprocess import PIPE, run
import json
import time

def time_fmt(fmt):
    return time.strftime(fmt)

def load_json(json_data):
    return json.loads(json_data)


def term(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout.strip()
