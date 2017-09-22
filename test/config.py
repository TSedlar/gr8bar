from subprocess import PIPE, run
import math
import time

text_props = {
    'font-size': '14px',
    'color': '#c2c2c2'
}

text_hack_props = {**text_props, 'font-family': 'Hack'}
text_fa_props = {**text_props, 'font-family': 'FontAwesome'}

panel_bg = '#2c3e50' # transparent
signal_levels = ['#c42f2f', '#9e3a3a', '#bc5b40', '#7f8432',
                 '#658432', '#33874c'] # low to high
battery_icons = ['&#xf243;', '&#xf242;', '&#xf241;', '&#xf240;'] # 25-100%
battery_levels = ['#9e3a3a', '#595959', '#33874c'] # low, med, high

def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}

def render_loop_delay():
    return 1000

def config(panel, layout, ui):
    panel.setStyleSheet('background-color: %s; border: none;' % (panel_bg))
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
        'css': {**text_fa_props, 'background-color': signal_levels[strength]}
    })
    # render SSID
    ssid = term("iwgetid -r")
    ui.add_center_label(layout, " %s " % (ssid), {
        'width': 80,
        'css': {**text_hack_props, 'background-color': '#3b7389'}
    })

def append_date_time(layout, ui):
    # render date & time
    _date = time.strftime('%m/%d/%Y')
    _time = time.strftime('%H:%M %p')
    ui.add_center_label(layout, '   %s &#xf07e; %s   ' % (_date, _time), {
        'css': {**text_hack_props, 'background-color': '#684c70'}
    })

def append_battery(layout, ui):
    # render bolt if charging
    if term('cat /sys/class/power_supply/BAT0/status') == 'Charging': # charging
        ui.add_center_label(layout, '  &#xf0e7;', {
            'css': {**text_fa_props, 'background-color': '#33874c'}
        })
    cap = int(term('cat /sys/class/power_supply/BAT0/capacity'))
    level = (2 if cap >= 60 else (1 if cap >= 30 else 0))
    icon = (3 if cap > 75 else (2 if cap > 50 else (1 if cap > 25 else 0)))
    # render battery symbol
    ui.add_center_label(layout, '  %s ' % (battery_icons[icon]), {
        'css': {**text_fa_props, 'background-color': battery_levels[level]}
    })
    # render battery %
    ui.add_center_label(layout, "%s%% " % (cap), {
        'css': {**text_hack_props, 'background-color': '#33874c'}
    })

def append_power(layout, ui):
    # render power-off symbol
    ui.add_center_label(layout, '  &#xf011;  ', {
        'css': {**text_fa_props, 'background-color': '#9e3a3a'}
    })

def term(command):
    result = run(command, stdout=PIPE, stderr=PIPE, 
                 universal_newlines=True, shell=True)
    return result.stdout.strip()
