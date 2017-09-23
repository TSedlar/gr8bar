import html

from PyQt5 import QtCore, QtGui, QtWidgets


def add_image(layout, image, padding_width=0):
    label = QtWidgets.QLabel()
    pixmap = QtGui.QPixmap(image)
    label.setPixmap(pixmap)
    label.setFixedWidth(pixmap.width() + padding_width)
    label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(label)
    return label


def add_slant(layout, type, color):
    label = QtWidgets.QLabel()
    pixmap = QtGui.QPixmap('./res/slant-%s.svg' % (type))
    recolor_pixmap(pixmap, color)
    label.setPixmap(pixmap)
    label.setFixedWidth(pixmap.width())
    label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(label)
    return label

def add_center_label(layout, text, props={}):
    txt = QtWidgets.QLabel()
    set_text(txt, text)
    if 'width' in props:
        txt.setFixedWidth(props['width'])
    if 'css' in props:
        txt.setStyleSheet(_to_sheet(props['css']))
        if 'font-family' in props['css'] and 'font-size' in props['css']:
            family = props['css']['font-family']
            size = int(props['css']['font-size'].replace('px', ''))
            txt.setFont(QtGui.QFont(family, size))
    txt.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(txt)
    return txt


def add_click_event(widget, callback):
    widget.mousePressEvent = callback


def add_hover_event(widget, enter_callback, leave_callback):
    widget.setMouseTracking(True)
    widget.enterEvent = enter_callback
    widget.leaveEvent = leave_callback


def set_hover_text(label, hover_text):
    text = label.text()
    enter_func = lambda _: set_text(label, hover_text)
    exit_func = lambda _: set_text(label, text)
    add_hover_event(label, enter_func, exit_func)


def set_text(label, text):
    label.setText(html.unescape(text))


def set_bg(widget, hex):
    append_css(widget, 'background-color: %s;' % hex)


def set_border(widget, border):
    append_css(widget, 'border: %s;' % border)


def recolor_pixmap(pixmap, hex):
    painter = QtGui.QPainter(pixmap)
    painter.setCompositionMode(painter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), _to_qcol(hex))
    painter.end()


def append_css(widget, css):
    widget.setStyleSheet(widget.styleSheet() + css)

def _to_sheet(dictionary):
    src = ''
    for key, value in dictionary.items():
        if len(src):
            src += '\n'
        src += (key + ': ' + value + ';')
    return src


def _to_qcol(hex):
    rgb = _hex_to_rgb(hex)
    return QtGui.QColor(rgb[0], rgb[1], rgb[2])


def _hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2 ,4))
