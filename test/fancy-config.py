panel_bg = 'transparent'
panel_border = 'none'
real_panel_bg = '#232631'
icon_color = '#e6e6e6'

text_props = {
    'color': icon_color,
    'background-color': real_panel_bg,
    'font-size': '14px',
    'font-family': 'Hack, FontAwesome'
}


def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def config(panel, layout, ui):
    ui.set_bg(panel, panel_bg)
    ui.set_border(panel, panel_border)
    render_logo(layout, ui)
    layout.addStretch(1)
    render_cpu(layout, ui)
    render_mem(layout, ui)
    layout.addStretch(1)
    render_time(layout, ui)
    render_weather(layout, ui)
    layout.addStretch(1)
    render_network(layout, ui)
    render_volume(layout, ui)
    render_battery(layout, ui)
    layout.addStretch(1)
    render_power(layout, ui)


def render_logo(layout, ui):
    ui.add_slant(layout, 'ld', real_panel_bg)
    lbl = ui.add_image(layout, './res/ubuntu-logo.svg', 4)
    ui.recolor_pixmap(lbl.pixmap(), icon_color)
    ui.set_bg(lbl, real_panel_bg)
    ui.add_slant(layout, 'ru', real_panel_bg)


def render_cpu(layout, ui):
    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf200;', { # cpu
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 3% ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf2db;', { # temp
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'lu', real_panel_bg)
    ui.add_center_label(layout, ' 20C ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)



def render_mem(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf085;', { # mem
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 786mb ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)

def render_time(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf073;', { # calendar
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 9/23/2017 ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)
    
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf017;', { # clock
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 12:33 AM ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)


def render_weather(layout, ui):
    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf0c2;', { # wifi
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 82F ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)


def render_network(layout, ui):
    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, '&#xf1eb;', { # wifi
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' CentHub ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)



def render_volume(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf028;', { # volume
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, ' 100% ', {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)


def render_battery(layout, ui):
    battery_text = '100%'
    if True: # charging
        battery_text += ' [&#xf0e7;]' # bolt

    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, '&#xf240;', { # battery
        'css': {**text_props}
    })
    ui.add_slant(layout, 'ru', real_panel_bg)

    ui.add_slant(layout, 'ld', real_panel_bg)
    ui.add_center_label(layout, battery_text, {
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)


def render_power(layout, ui):
    ui.add_slant(layout, 'lui', real_panel_bg)
    ui.add_center_label(layout, ' &#xf011; ', { # power
        'css': {**text_props}
    })
    ui.add_slant(layout, 'rd', real_panel_bg)
