import os

panel_bg = 'transparent'
panel_border = 'none'

real_panel_bg = '#282936' # '#2c3e50'
active_panel_bg = '#2c3e50' # '#1e4a59'

icon_color = '#e6e6e6'

text_css = {
    'css': {
        'color': icon_color,
        'background-color': real_panel_bg,
        'font-size': '14px',
        'font-family': 'Hack, FontAwesome'
    }
}

key_window_title = 'window_title'
key_user = 'sys_user'

def bounds():
    return {'x': 65, 'y': 1032, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000


def init_prop_updaters():
    return [(update_window_title, 1.5), (update_welcome, 60)]


def config(data):
    data.ui.set_bg(data.panel, panel_bg)
    data.ui.set_border(data.panel, panel_border)
    render_workspace(data)
    data.layout.addStretch(1)
    render_window_title(data)
    data.layout.addStretch(1)
    render_welcome(data)

def render_workspace(data):
    workspace = data.tools.x_workspace()
    #                     code         term       notes       busy
    workspace_labels = ['&#xf121;', '&#xf120;', '&#xf040;', '&#xf009;']
    # render all workspaces with their respective labels
    for idx, lbl in enumerate(workspace_labels):
        first_type = None
        last_type = None
        if idx == 0:
            first_type = 'lui'
            last_type = 'rd'
        elif idx == len(workspace_labels) - 1:
            first_type = 'lui'
            last_type = 'rd'
        elif idx % 2 == 0:
            first_type = 'lu'
            last_type = 'rd'
        else:
            first_type = 'lui'
            last_type = 'ru'
        bg_color = active_panel_bg if idx == workspace else real_panel_bg
        data.ui.add_slant(data.layout, first_type, bg_color)
        label = data.ui.add_center_label(data.layout, ' %s ' % (lbl), text_css)
        data.ui.set_bg(label, bg_color)
        data.ui.add_slant(data.layout, last_type, bg_color)


def render_window_title(data):
    window_title = data.props.get(key_window_title, os.name)
    if len(window_title) > 130:
        window_title = window_title[:130] + '...'

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s ' % (window_title), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

def render_welcome(data):
    user = data.props.get(key_user, '?')

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf2bd;', text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' %s ' % (user), text_css)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

# Update functions below

def update_window_title(tools, props):
    props[key_window_title] = tools.term('xdotool getwindowfocus getwindowname')


def update_welcome(tools, props):
    props[key_user] = tools.term('id -u -n')
