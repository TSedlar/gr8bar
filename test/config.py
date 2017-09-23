from subprocess import PIPE, run
import math
import time

text_props = {
    'color': '#c2c2c2',
    'font-size': '14px',
    'font-family': 'Hack, FontAwesome'
}

panel_bg = '#282936' # 'transparent'
signal_levels = ['#c42f2f', '#9e3a3a', '#bc5b40', '#7f8432',
                 '#658432', '#33874c'] # low to high
battery_icons = ['&#xf243;', '&#xf242;', '&#xf241;', '&#xf240;'] # 25-100%
battery_levels = ['#9e3a3a', '#595959', '#33874c'] # low, med, high

def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def init(props):
    pass


def config(panel, layout, ui, props):
    panel.set_bg(panel_bg)
    panel.set_border('none')
    append_network(layout, ui)
    layout.addStretch(1)
    append_date_time(layout, ui)
    layout.addStretch(1)
    append_battery(layout, ui)
    append_power(layout, ui)


def append_network(layout, ui):
    # parse dbm for network strength color
    netcard = term("iwgetid | awk '{print $1}'")
    dbm = int(term(("iw %s station dump | grep 'signal avg:'" +
                    " | grep -o -E '[0-9]+' | head -1") % (netcard)))
    strength = int(round(min(100, math.floor(((-dbm + 100) * 2))) / 20))
    # render wifi symbol
    ui.add_center_label(layout, ' &#xf1eb; ', {
        'width': 30,
        'css': {**text_props, 'background-color': signal_levels[strength]}
    })
    # render SSID
    ssid = term("iwgetid -r")
    ui.add_center_label(layout, " %s " % (ssid), {
        'width': 80,
        'css': {**text_props, 'background-color': '#3b7389'}
    })


def append_date_time(layout, ui):
    # render date & time
    _date = time.strftime('%m/%d/%Y')
    _time = time.strftime('%I:%M %p')
    text = '   %s &#xf07e; %s   ' % (_date, _time)
    hover_text = '  Today is %s  ' % (time.strftime('%A'))
    label = ui.add_center_label(layout, text, {
        'css': {**text_props, 'background-color': '#684c70'}
    })
    ui.set_hover_text(label, hover_text)


def append_battery(layout, ui):
    # render bolt if charging
    if term('cat /sys/class/power_supply/BAT0/status') == 'Charging': # charging
        ui.add_center_label(layout, '  &#xf0e7;', {
            'css': {**text_props, 'background-color': '#33874c'}
        })
    cap = int(term('cat /sys/class/power_supply/BAT0/capacity'))
    level = (2 if cap >= 60 else (1 if cap >= 30 else 0))
    icon = (3 if cap > 75 else (2 if cap > 50 else (1 if cap > 25 else 0)))
    # render battery symbol
    ui.add_center_label(layout, '  %s ' % (battery_icons[icon]), {
        'css': {**text_props, 'background-color': battery_levels[level]}
    })
    # render battery %
    label = ui.add_center_label(layout, "%s%% " % (cap), {
        'css': {**text_props, 'background-color': '#33874c'}
    })

    full = int(term('cat /sys/class/power_supply/BAT0/charge_full'))
    now = int(term('cat /sys/class/power_supply/BAT0/charge_now'))
    amps = int(term('cat /sys/class/power_supply/BAT0/current_now'))

    full_time = float(full) / amps
    now_time = float(now) / amps

    remaining = (now_time - (full_time - now_time))
    hours = int(remaining)
    mins = int(((remaining - hours)) * 60)

    ui.set_hover_text(label, '%s:%s &#xf017; ' % (hours, mins))


def append_power(layout, ui):
    # render power-off symbol
    ui.add_center_label(layout, '  &#xf011;  ', {
        'css': {**text_props, 'background-color': '#9e3a3a'}
    })


def term(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout.strip()
