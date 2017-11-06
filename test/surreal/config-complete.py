import math

zip_code = 85224

panel_bg = 'transparent'
panel_border = 'none'

real_panel_bg = '#383c4a'
real_panel_bg_hover = '#555a6d'

icon_color = '#e6e6e6'

text_css = {
    'css': {
        'color': icon_color,
        'background-color': real_panel_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}

popup_props = {
    'bg': real_panel_bg,
    'bg_hover': real_panel_bg_hover,
    **text_css
}

net_popup_props = {
    'item_width': 300,
    'item_height': 34,
    **popup_props
}

vol_popup_props = {
    'item_width': 40,
    'item_height': 130,
    **popup_props
}


key_date_text = 'date_text'
key_weather_temp = 'weather_temp'
key_cpu_percent = 'cpu_percent'
key_cpu_temp = 'cpu_temp'
key_mem_used = 'mem_used'
key_network_ssid = 'network_ssid'
key_volume = 'volume'
key_battery_cap = 'battery_cap'
key_battery_state = 'battery_state'
key_battery1_cap = 'battery1_cap'
key_battery1_state = 'battery1_state'
key_net_popup = 'net_popup'
key_vol_popup = 'vol_popup'

def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def init_prop_updaters():
    return [(update_cpu, 5), (update_mem, 5), (update_battery, 30),
            (update_weather, 60 * 10), (update_network, 30), (update_volume, 1)]


def config(data):
    data.ui.set_bg(data.panel, panel_bg)
    data.ui.set_border(data.panel, panel_border)
    render_logo(data)
    data.layout.addStretch(1)
    render_cpu(data)
    render_mem(data)
    data.layout.addStretch(1)
    render_time(data)
    render_weather(data)
    data.layout.addStretch(1)
    render_network(data)
    render_volume(data)
    render_battery(data)
    data.layout.addStretch(1)
    render_power(data)


def render_logo(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    lbl = data.ui.add_image(data.layout, __file__, '../../res/arch-logo.svg', 10)
    data.ui.recolor_pixmap(lbl.pixmap(), icon_color)
    data.ui.set_bg(lbl, real_panel_bg)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_cpu(data):
    cpu_percent = data.props.get(key_cpu_percent, '*')
    cpu_temp = data.props.get(key_cpu_temp, '*')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf200;', text_css) # cpu
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' %s%% ' % (cpu_percent), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf2db;', text_css) # temp
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'lu', real_panel_bg)
    data.ui.add_label(data.layout, ' %s° C ' % (cpu_temp), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_mem(data):
    mem = data.props.get(key_mem_used, '*')

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf085;', text_css) # mem
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' %sMB ' % (mem), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_time(data):
    _date = data.tools.time_fmt('%m/%d/%Y')
    _time = data.tools.time_fmt('%I:%M %p')
    date_txt = ' %s ' % (_date)
    def date_hov_txt():
        return ' %s ' % (data.tools.time_fmt('%A'))

    data.ui.add_slant(data.layout, 'lui', real_panel_bg),
    data.ui.add_label(data.layout, '&#xf073;', text_css), # calendar
    data.ui.add_slant(data.layout, 'ru', real_panel_bg),

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    date_label = data.ui.add_label(data.layout, None, text_css)
    data.ui.add_label_hover(date_label, date_txt, date_hov_txt,
                            data.props, key_date_text)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf017;', text_css) # clock
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' %s ' % (_time), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_weather(data):
    temp = data.props.get(key_weather_temp, '*')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf0c2;', text_css) # cloud
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' %s° F ' % (temp), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_network(data):
    ssid = data.props.get(key_network_ssid, '?')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf1eb;', text_css) # wifi
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    ssl = data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    ssid_label = data.ui.add_label(data.layout, ' %s ' % (ssid), text_css)
    slr = data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    comps = (ssl, ssid_label, slr)

    if not key_net_popup in data.props:
        popup = data.modules.network.create_popup(data, net_popup_props)
        data.props[key_net_popup] = popup

    popup = data.props[key_net_popup]
    data.ui.add_click_popup(ssid_label, popup.window, 'center', (0, 0))



def render_volume(data):
    volume = data.props.get(key_volume, '0%')

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf028;', text_css) # volume
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    vol_label = data.ui.add_label(data.layout, ' %s%% ' % (volume), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    if not key_vol_popup in data.props:
        set_vol = lambda v: data.modules.linux.set_alsa_volume(v)
        popup = data.modules.sound.create_popup(data, vol_popup_props,
                                                key_volume, set_vol)
        data.props[key_vol_popup] = popup

    popup = data.props[key_vol_popup]
    data.ui.add_click_popup(vol_label, popup, 'center', (0, 0))


def render_battery(data):
    cap = data.props.get(key_battery_cap, -1)
    cap1 = data.props.get(key_battery1_cap, -1)
    state = data.props.get(key_battery_state, 'Invalid')
    state1 = data.props.get(key_battery1_state, 'Invalid')

    #                    0%        1-25%       26-50%      51-75%     76-100%
    battery_icons = ['&#xf244;', '&#xf243;', '&#xf242;', '&#xf241;', '&#xf240;']
    battery_icon = battery_icons[int(math.ceil(float(cap) / 25))]
    battery1_icon = battery_icons[int(math.ceil(float(cap1) / 25))]

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, battery_icon, text_css) # battery
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, 'E:%s%%' % (cap1), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, 'I:%s%%' % (cap), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    if state == 'Charging' or state1 == 'Charging':
        data.ui.add_slant(data.layout, 'lui', real_panel_bg)
        data.ui.add_label(data.layout, '&#xf0e7;', text_css) # bolt
        data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_power(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    lbl = data.ui.add_label(data.layout, ' &#xf011; ', text_css) # power
    data.ui.add_click_event(lbl, lambda _: data.modules.linux.logout())
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

# Update functions below

def update_cpu(tools, modules, props):
    props[key_cpu_percent] = modules.linux.get_cpu_percent()
    props[key_cpu_temp] = modules.linux.get_cpu_temp()


def update_mem(tools, modules, props):
    props[key_mem_used] = modules.linux.get_mem_used()


def update_weather(tools, modules, props):
    props[key_weather_temp] = tools.get_weather(zip_code)


def update_network(tools, modules, props):
    props[key_network_ssid] = modules.linux.get_network_ssid()


def update_volume(tools, modules, props):
    props[key_volume] = modules.linux.get_alsa_volume()


def update_battery(tools, modules, props):
    bat1 = tools.term('cat /sys/class/power_supply/BAT1/capacity')
    bat1_state = tools.term('cat /sys/class/power_supply/BAT1/status')
    props[key_battery_cap] = modules.linux.get_battery_capacity()
    props[key_battery_state] = modules.linux.get_battery_state()
    props[key_battery1_cap] = int(bat1)
    props[key_battery1_state] = bat1_state
