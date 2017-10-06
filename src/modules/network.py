import re
from collections import namedtuple

import tools


Network = namedtuple('Network', ['ssid', 'signal'])

nmcli_table_regex = str.join('', (
    '(.*)\s+(\w+)\s+([0-9]+)\s+([0-9]+)\s+Mbit\/s',
    '\s+([0-9]+)\s+[^a-zA-Z0-9\s:]+\s+(\w+)'
))


def listing():
    return parse_listing(tools.term('nmcli dev wifi'))


def parse_listing(output):
    listing = []
    if len(output):
        lines = output.split('\n')
        for line in lines:
            line = line.strip()
            if not line.startswith('*'):
                matches = re.match(nmcli_table_regex, line)
                if matches:
                    ssid = matches.group(1).strip()
                    signal = matches.group(5)
                    listing.append(Network(ssid, signal))
    return listing
