panel_bg = '#1a2740'
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
    return {'x': 0, 'y': 1054, 'w': 1920, 'h': 26}


def render_loop_delay():
    return 1000


def init_prop_updaters():
    return []


def config(data):
    data.ui.set_bg(data.panel, panel_bg)
    data.ui.set_border(data.panel, panel_border)
