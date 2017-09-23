from subprocess import PIPE, run
import os
import threading
import json
import time

cdir = os.path.dirname(__file__)

zip_code = 85224
panel_bg = 'transparent'
panel_border = 'none'
real_panel_bg = '#2c3e50' # '#232631'
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

def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def init(props):
    def weather_proc(props):
        while True:
            update_weather(props)
            time.sleep(60 * 10) # update every 10 mins
    threading.Thread(target=weather_proc, args=(props,)).start()

def config(panel, layout, ui, props):
    ui.set_bg(panel, panel_bg)
    ui.set_border(panel, panel_border)
    render_logo(layout, ui)
    layout.addStretch(1)
    render_cpu(layout, ui)
    render_mem(layout, ui)
    layout.addStretch(1)
    render_time(layout, ui, props)
    render_weather(layout, ui, props)
    layout.addStretch(1)
    render_network(layout, ui)
    render_volume(layout, ui)
    render_battery(layout, ui)
    layout.addStretch(1)
    render_power(layout, ui)


def render_logo(layout, ui):
    ui.add_slant(layout, 'ld', real_panel_bg)
    lbl = ui.add_image(layout, res('../res/ubuntu-logo.svg'), 10)
    ui.recolor_pixmap(lbl.pixmap(), icon_color)
    ui.set_bg(lbl, real_panel_bg)
    ui.add_slant(layout, 'ru', real_panel_bg)


def render_cpu(layout, ui):
    percent = term("uptime | awk '{print $12 / $(nproc) * 100}'")
    temp = int(int(term("cat /sys/class/thermal/thermal_zone0/temp")) / 1000)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf200;', text_css) # cpu
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' %s%% ' % (percent), text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf2db;', text_css) # temp
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'lu', real_panel_bg)
    ui.add_center_label(layout, ' %s° C ' % (temp), text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)


def render_mem(layout, ui):
    mem = term("free -m | grep 'Mem:' | awk '{print $6}'")

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf085;', text_css) # mem
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' %sMB ' % (mem), text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)

def render_time(layout, ui, props):
    _date = time.strftime('%m/%d/%Y')
    _time = time.strftime('%I:%M %p')
    date_txt = ' %s ' % (_date)
    def date_hov_txt():
        return ' %s ' % (time.strftime('%A'))

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf073;', text_css) # calendar
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    date_label = ui.add_center_label(layout, None, text_css)
    ui.add_label_hover(date_label, date_txt, date_hov_txt, props, key_date_text)
    ui.add_slant(layout, 'rd', real_panel_bg)

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf017;', text_css) # clock
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' %s ' % (_time), text_css)
    ui.add_slant(layout, 'ru', real_panel_bg)


def update_weather(props):
    yql_api = 'https://query.yahooapis.com/v1/public/yql?'
    query = 'q=select wind.chill from weather.forecast where woeid in ' \
            '(select woeid from geo.places(1) where text="%s")&format=json'
    query_url = yql_api + (query % (zip_code)).replace(' ', '%20')
    result = json.loads(term('curl "%s"' % (query_url)))

    temp = result['query']['results']['channel']['wind']['chill']
    props[key_weather_temp] = temp


def render_weather(layout, ui, props):
    temp = props.get(key_weather_temp, '*')

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf0c2;', text_css) # cloud
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' %sF ' % (temp), text_css)
    ui.add_slant(layout, 'ru', real_panel_bg)


def render_network(layout, ui):
    ssid = term("iwgetid -r")

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf1eb;', text_css) # wifi
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' %s ' % (ssid), text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)



def render_volume(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf028;', text_css) # volume
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 100% ', text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)


def render_battery(layout, ui):
    cap = int(term('cat /sys/class/power_supply/BAT0/capacity'))
    battery_text = '%s%%' % (cap)
    if term('cat /sys/class/power_supply/BAT0/status') == 'Charging':
        battery_text += ' [&#xf0e7;]' # bolt

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf240;', text_css) # battery
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, battery_text, text_css)
    ui.add_slant(layout, 'rd', real_panel_bg)


def render_power(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, ' &#xf011; ', text_css) # power
    ui.add_slant(layout, 'rd', real_panel_bg)


def res(file):
    return os.path.join(cdir, file)


def term(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout.strip()
