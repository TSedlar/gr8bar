from PyQt5 import QtCore, QtWidgets


default_bg = '#343f5a'
default_bg_hover = '#232a3d'


def create_popup(data, props, vol_key, set_vol):
    width = props['item_width'] if 'item_width' in props else 45
    height = props['item_height'] if 'item_height' in props else 130
    bg = props['bg'] if 'bg' in props else default_bg
    popup = data.ui.create_popup(width, 0, bg)
    popup_layout = data.ui.vbox_layout(popup)
    popup_layout.setContentsMargins(0, 10, 0, 10)

    data.ui.add_label(popup_layout, '100', props).setFixedHeight(25)

    slider_frame = QtWidgets.QFrame()
    slider_layout = data.ui.hbox_layout(slider_frame)
    slider_layout.setContentsMargins(10, 10, 10, 10)
    slider = QtWidgets.QSlider(QtCore.Qt.Vertical)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setFixedSize(10, height)
    slider_layout.addWidget(slider)
    popup_layout.addWidget(slider_frame)

    data.ui.add_label(popup_layout, '0', props).setFixedHeight(25)

    data.ui.add_show_event(popup, lambda _: slider.setValue(data.props[vol_key]))

    def handle_slider(_):
        data.props[vol_key] = slider.value()
        set_vol(data.props[vol_key])

    slider.mouseReleaseEvent = handle_slider

    return popup
