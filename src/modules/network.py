import re
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import namedtuple

import tools


Network = namedtuple('Network', ['ssid', 'signal', 'security'])
NetPopup = namedtuple('NetPopup', ['window', 'layout', 'prompt'])

default_bg = '#343f5a'
default_bg_hover = '#232a3d'

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


def create_prompt(data, props):
    width = props['item_width'] if 'item_width' in props else 300
    bg = props['bg_hover'] if 'bg_hover' in props else default_bg_hover
    popup = data.ui.create_popup(width, 0, bg)
    popup_layout = data.ui.vbox_layout(popup)

    frame = QtWidgets.QFrame()
    f_layout = data.ui.hbox_layout(frame)
    f_layout.setContentsMargins(10, 10, 10, 10)

    label = props['chosen_ssid'] if 'chosen_ssid' in props else 'Password'

    data.ui.add_label(f_layout, '%s: ' % (label), {
        **props, **{'alignment': 'left'}
    })

    pass_input = QtWidgets.QLineEdit()
    pass_input.setStyleSheet(data.ui.dict_to_sheet(props['css']))

    data.ui.apply_tree_callback(frame, lambda x: data.ui.set_bg(x, bg))

    def reset_input(_):
        pass_input.setText('')
        pass_input.setFocus()

    data.ui.add_show_event(popup, reset_input)

    f_layout.addWidget(pass_input)
    popup_layout.addWidget(frame)
    return popup

def create_popup(data, props):
    width = props['item_width'] if 'item_width' in props else 300
    bg = props['bg'] if 'bg' in props else default_bg
    popup = data.ui.create_popup(width, 0, bg)
    popup_layout = data.ui.vbox_layout(popup)
    prompt = create_prompt(data, props)
    update_popup_layout(data, props, popup_layout, prompt)
    data.ui.add_show_event(prompt, lambda _: prompt.activateWindow())
    data.ui.add_hide_event(popup, lambda _: prompt.hide())
    return NetPopup(popup, popup_layout, prompt)


def update_popup_layout(data, props, popup_layout, prompt):
    data.ui.clear_layout(popup_layout)
    output_file = data.ui.res(__file__, '../../res/test/nmcli-output.txt')
    output_text = data.tools.term('cat ' + output_file)
    networks = data.modules.network.parse_listing(output_text)
    for network in networks:
        _add_network_entry(data.ui, network, popup_layout, prompt, props)


def _add_network_entry(ui, network, popup_layout, prompt, props):
    frame = QtWidgets.QFrame()
    width = props['item_width'] if 'item_width' in props else 300
    height = props['item_height'] if 'item_height' in props else 34
    bg = props['bg'] if 'bg' in props else default_bg
    bg_hover = props['bg_hover'] if 'bg_hover' in props else default_bg_hover
    frame.setFixedSize(width, height)
    f_layout = ui.hbox_layout(frame)
    f_layout.setContentsMargins(10, 10, 10, 10)
    ui.add_label(f_layout, network.ssid, {
        **props, **{'alignment': 'left'}
    })
    f_layout.addStretch(1)
    lock = '&#xf023;' if network.security is not None else '&#xf13e;'
    ui.add_label(f_layout, ' &#xf1eb; ', props)
    ui.add_label(f_layout, ' %s' % (lock), props)
    def handle_enter(_):
        props['chosen_ssid'] = network.ssid
        ui.apply_tree_callback(frame, lambda x: ui.set_bg(x, bg_hover))
    def handle_exit(_):
        ui.apply_tree_callback(frame, lambda x: ui.set_bg(x, bg))
    ui.add_hover_event(frame, handle_enter, handle_exit)
    ui.add_click_popup(frame, prompt, 'center', (0, -height))
    popup_layout.addWidget(frame)