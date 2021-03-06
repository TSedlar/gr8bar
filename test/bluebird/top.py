from PyQt5 import QtCore, QtGui, QtWidgets

panel_bg = '#1a2740'
panel_border = 'none'
item_bg = '#343f5a'
item_bg_hover = '#232a3d'
icon_color = '#c1d281'
text_color = '#34a764'

icon_css = {
    'css': {
        'color': icon_color,
        'background-color': item_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}

text_css = {
    'css': {
        'color': text_color,
        'background-color': item_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}

popup_props = {
    'bg': item_bg,
    'bg_hover': item_bg_hover,
    'css': {
        'color': '#c1c1c1',
        'background-color': item_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}

network_popup_props = {
    'item_width': 300,
    'item_height': 34,
    **popup_props
}

volume_popup_props = {
    'item_width': 45,
    'item_height': 130,
    **popup_props
}


def bounds():
    return {'x': 0, 'y': 0, 'w': 1920, 'h': 26}


def render_loop_delay():
    return 1000


def init_prop_updaters():
    return []


def config(data):
    data.ui.set_bg(data.panel, panel_bg)
    data.ui.set_border(data.panel, panel_border)
    render_logo(data, data.tools, data.ui)
    render_cpu(data, data.tools, data.ui)
    render_mem(data, data.tools, data.ui)
    data.layout.addStretch(1)
    render_time(data, data.tools, data.ui)
    render_weather(data, data.tools, data.ui)
    data.layout.addStretch(1)
    render_network(data, data.tools, data.ui)
    render_battery(data, data.tools, data.ui)
    render_volume(data, data.tools, data.ui)
    render_power(data, data.tools, data.ui)


def show_hover(data, item, key):
    data.ui.show_hover(item, item_bg, item_bg_hover, data.props, key)


def render_logo(data, tools, ui):
    logo_path = '../../res/ubuntu-logo-sm.svg'
    logo = ui.add_image(data.layout, __file__, logo_path, 10, icon_color)
    ui.set_bg(logo, item_bg)
    ui.add_border_line(logo, '#ea822c', 2)


def render_cpu(data, tools, ui):
    tools.multi_apply(lambda x: ui.add_border_line(x, '#c9e3d3', 2), (
        ui.add_label(data.layout, ' &#xf200;', icon_css),
        ui.add_label(data.layout, ' 6%', text_css),
    ))
    tools.multi_apply(lambda x: ui.add_border_line(x, '#9579c6', 2), (
        ui.add_label(data.layout, ' &#xf2db;', icon_css),
        ui.add_label(data.layout, ' 23° C', text_css),
    ))


def render_mem(data, tools, ui):
    tools.multi_apply(lambda x: ui.add_border_line(x, '#50a05b', 2), (
        ui.add_label(data.layout, ' &#xf085;', icon_css),
        ui.add_label(data.layout, ' 419MB ', text_css),
    ))

def render_time(data, tools, ui):
    tools.multi_apply(lambda x: ui.add_border_line(x, '#228b97', 2), (
        ui.add_label(data.layout, ' &#xf073;', icon_css),
        ui.add_label(data.layout, ' 10/6/2017', text_css),
    ))
    tools.multi_apply(lambda x: ui.add_border_line(x, '#228b97', 2), (
        ui.add_label(data.layout, ' &#xf017;', icon_css),
        ui.add_label(data.layout, ' 5:12 AM', text_css),
    ))


def render_weather(data, tools, ui):
    tools.multi_apply(lambda x: ui.add_border_line(x, '#228b97', 2), (
        ui.add_label(data.layout, ' &#xf0c2;', icon_css),
        ui.add_label(data.layout, ' 84° F ', text_css),
    ))


def render_network(data, tools, ui):
    # connected = &#xf1eb;
    # disconnected = &#xf00d;
    comps = (
        ui.add_label(data.layout, ' &#xf1eb;', icon_css),
        ui.add_label(data.layout, ' CentHub ', text_css)
    )
    tools.multi_apply(lambda x: ui.add_border_line(x, '#50a05b', 2), comps)
    if not 'network_popup' in data.props:
        popup = data.modules.network.create_popup(data, network_popup_props)
        data.props['network_popup'] = popup
    popup = data.props['network_popup']
    ui.add_click_popup(comps[1], popup.window, 'right', (0, 0))


def render_battery(data, tools, ui):
    tools.multi_apply(lambda x: ui.add_border_line(x, '#9579c6', 2), (
        ui.add_label(data.layout, ' &#xf240;', icon_css),
        ui.add_label(data.layout, ' 100% ', text_css),
    ))


def render_volume(data, tools, ui):
    # high = &#xf028;
    # low-mid = &#xf027;
    # muted = &#xf026;
    volume = ui.add_label(data.layout, ' &#xf027; ', icon_css)
    ui.add_border_line(volume, '#c9e3d3', 2)
    show_hover(data, volume, 'vol_hover_bg')
    if not 'volume_popup' in data.props:
        popup = data.modules.sound.create_popup(data, volume_popup_props)
        data.props['volume_popup'] = popup
    popup = data.props['volume_popup']
    ui.add_click_popup(volume, popup, 'center', (0, 0))


def render_power(data, tools, ui):
    power = ui.add_label(data.layout, ' &#xf011; ', icon_css)
    ui.add_border_line(power, '#ea822c', 2)
    show_hover(data, power, 'power_hover_bg')
