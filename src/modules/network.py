import re
from collections import namedtuple

import tools


Network = namedtuple('Network', ['ssid', 'signal', 'security'])

nmcli_table_regex = str.join('', (
    '(.*)\s+(\w+)\s+([0-9]+)\s+([0-9]+)\s+Mbit\/s',
    '\s+([0-9]+)\s+[^a-zA-Z0-9\s:]+\s+([\w\s]+)'
))


def listing():
    return parse_listing(tools.term('nmcli dev wifi'))


def parse_listing(output):
    listing = []
    if len(output):
        lines = output.split('\n') # non-secure networks end with lines..
                                   # don't #strip() it, #strip() matches.
        for line in lines:
            if not line.strip().startswith('*'):
                matches = re.match(nmcli_table_regex, line)
                if matches:
                    ssid = matches.group(1).strip()
                    signal = matches.group(5).strip()
                    security = matches.group(6).strip()
                    if not len(security):
                        security = None
                    listing.append(Network(ssid, signal, security))
    return listing
