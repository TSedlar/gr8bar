import math

zip_code = 85224

panel_bg = 'transparent'
panel_border = 'none'

real_panel_bg = '#282936' # '#2c3e50'

icon_color = '#e6e6e6'

text_css = {
    'css': {
        'color': icon_color,
        'background-color': real_panel_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
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
    lbl = data.ui.add_image(data.layout, __file__, '../../res/ubuntu-logo.svg', 10)
    data.ui.recolor_pixmap(lbl.pixmap(), icon_color)
    data.ui.set_bg(lbl, real_panel_bg)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_cpu(data):
    cpu_percent = data.props.get(key_cpu_percent, '*')
    cpu_temp = data.props.get(key_cpu_temp, '*')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf200;', text_css) # cpu
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s%% ' % (cpu_percent), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf2db;', text_css) # temp
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'lu', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s° C ' % (cpu_temp), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_mem(data):
    mem = data.props.get(key_mem_used, '*')

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf085;', text_css) # mem
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %sMB ' % (mem), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

def render_time(data):
    _date = data.tools.time_fmt('%m/%d/%Y')
    _time = data.tools.time_fmt('%I:%M %p')
    date_txt = ' %s ' % (_date)
    def date_hov_txt():
        return ' %s ' % (data.tools.time_fmt('%A'))

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf073;', text_css) # calendar
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    date_label = data.ui.add_center_label(data.layout, None, text_css)
    data.ui.add_label_hover(date_label, date_txt, date_hov_txt,
                            data.props, key_date_text)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf017;', text_css) # clock
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s ' % (_time), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_weather(data):
    temp = data.props.get(key_weather_temp, '*')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf0c2;', text_css) # cloud
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s° F ' % (temp), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_network(data):
    ssid = data.props.get(key_network_ssid, '?')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf1eb;', text_css) # wifi
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s ' % (ssid), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)



def render_volume(data):
    volume = data.props.get(key_volume, '0%')

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf028;', text_css) # volume
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s ' % (volume), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_battery(data):
    cap = data.props.get(key_battery_cap, -1)
    state = data.props.get(key_battery_state, 'Invalid')

    #                    0%        1-25%       26-50%      51-75%     76-100%
    battery_icons = ['&#xf244;', '&#xf243;', '&#xf242;', '&#xf241;', '&#xf240;']
    battery_icon = battery_icons[int(math.ceil(float(cap) / 25))]

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, battery_icon, text_css) # battery
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '%s%%' % (cap), text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    if state == 'Charging':
        data.ui.add_slant(data.layout, 'lui', real_panel_bg)
        data.ui.add_center_label(data.layout, '&#xf0e7;', text_css) # bolt
        data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_power(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    lbl = data.ui.add_center_label(data.layout, ' &#xf011; ', text_css) # power
    data.ui.add_click_event(lbl, lambda _: data.tools.term('pkill -u $USER'))
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

# Update functions below

def update_cpu(tools, props):
    cpu_percent = tools.term("vmstat 1 2 | tail -1 | awk '{print 100-$15}'")
    temp_str = tools.term('cat /sys/class/thermal/thermal_zone0/temp')
    cpu_temp = int((int(temp_str) if len(temp_str) else -1000) / 1000)

    props[key_cpu_percent] = cpu_percent
    props[key_cpu_temp] = cpu_temp


def update_mem(tools, props):
    mem = tools.term("free -m | grep 'Mem:' | awk '{print $6}'")

    props[key_mem_used] = mem


def update_weather(tools, props):
    yql_api = 'https://query.yahooapis.com/v1/public/yql?'
    query = 'q=select wind.chill from weather.forecast where woeid in ' \
            '(select woeid from geo.places(1) where text="%s")&format=json'
    query_url = yql_api + (query % (zip_code)).replace(' ', '%20')
    json = tools.load_json(tools.term('curl "%s"' % (query_url)))

    props[key_weather_temp] = json['query']['results']['channel']['wind']['chill']


def update_network(tools, props):
    ssid = tools.term("iwgetid -r")

    props[key_network_ssid] = ssid


def update_volume(tools, props):
    vol = tools.term("amixer get Master | grep % | awk '{print $4}'" +
                     " | sed -e 's/\[//' -e 's/\]//'")

    props[key_volume] = vol


def update_battery(tools, props):
    cap_str = tools.term('cat /sys/class/power_supply/BAT0/capacity')
    cap = int(cap_str) if len(cap_str) else -1
    state = tools.term('cat /sys/class/power_supply/BAT0/status')

    props[key_battery_cap] = cap
    props[key_battery_state] = state
