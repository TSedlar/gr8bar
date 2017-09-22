text_props = {
    'font-size': '14px',
    'color': '#c2c2c2'
}

text_hack_props = { **text_props, 'font-family': 'Hack' }
text_fa_props = { **text_props, 'font-family': 'FontAwesome' }

def bounds():
    return { 'x': 0, 'y': 0, 'w': 1920, 'h': 28 }

def config(bar, layout, ui):
    bar.setStyleSheet('background-color: #323232; border: none;')
    # render wifi symbol
    ui.add_center_label(layout, ' &#xf1eb; ', {
        'width': 30,
        'css': { **text_fa_props, 'background-color': '#33874c' }
    })
    # render SSID
    ui.add_center_label(layout, ' CentHub ', {
        'width': 80,
        'css': { **text_hack_props, 'background-color': '#3b7389' }
    })
    layout.addStretch(1)
    # render date & time
    ui.add_center_label(layout, '   9/21/2017 &#xf07e; 11:04 PM   ', {
        'css': { **text_hack_props, 'background-color': '#684c70'}
    })
    layout.addStretch(1)
    # render bolt if charging
    if True: # charging
        ui.add_center_label(layout, '  &#xf0e7; ', {
            'css': { **text_fa_props, 'background-color': '#33874c'}
        })
    # render battery symbol
    ui.add_center_label(layout, ' &#xf240; ', {
        'css': { **text_fa_props, 'background-color': '#33874c'}
    })
    # render battery %
    ui.add_center_label(layout, '100% ', {
        'css': { **text_hack_props, 'background-color': '#33874c'}
    })
    # render power-off symbol
    ui.add_center_label(layout, '  &#xf011;  ', {
        'css': { **text_fa_props, 'background-color': '#9e3a3a' }
    })