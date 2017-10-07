panel_bg = 'transparent'
panel_border = 'none'
real_panel_bg = '#232631'
icon_color = '#e6e6e6'

text_css = {
    'css': {
        'color': icon_color,
        'background-color': real_panel_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}


def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def init_prop_updaters():
    return []


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
    lbl = data.ui.add_image(data.layout, __file__, '../res/ubuntu-logo.svg', 4)
    data.ui.recolor_pixmap(lbl.pixmap(), icon_color)
    data.ui.set_bg(lbl, real_panel_bg)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_cpu(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf200;', text_css) # cpu
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 3% ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf2db;', text_css) # temp
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'lu', real_panel_bg)
    data.ui.add_label(data.layout, ' 20C ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)



def render_mem(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf085;', text_css) # mem
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 786mb ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

def render_time(data):
    # if not 'cal_window' in data.props:
    #     window = data.ui.create_popup(300, 100, '#ff0000')
    #     data.props['cal_window'] = window
    # data.tools.multi_apply(lambda x: data.ui.add_border_line(x, '#FFFFFF', 4), (
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    cal = data.ui.add_label(data.layout, '&#xf073;', text_css) # calendar
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)
    # data.ui.add_click_popup(cal, data.props['cal_window'], 'right')
    # ))

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 9/23/2017 ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf017;', text_css) # clock
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 12:33 AM ', text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_weather(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf0c2;', text_css) # wifi
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 82° F ', text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_network(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf1eb;', text_css) # wifi
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' CentHub ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_volume(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf028;', text_css) # volume
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, ' 100% ', text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_battery(data):
    battery_text = '100%'

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, '&#xf240;', text_css) # battery
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_label(data.layout, battery_text, text_css)
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    if True: #charging
        data.ui.add_slant(data.layout, 'lui', real_panel_bg)
        data.ui.add_label(data.layout, '&#xf0e7;', text_css) # bolt
        data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_power(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_label(data.layout, ' &#xf011; ', text_css) # power
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)
