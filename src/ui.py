import html

from PyQt5 import QtCore, QtGui, QtWidgets


def add_center_label(layout, text, props={}):
    txt = QtWidgets.QLabel()
    set_text(txt, text)
    if 'width' in props:
        txt.setFixedWidth(props['width'])
    if 'css' in props:
        txt.setStyleSheet(to_sheet(props['css']))
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


def to_sheet(dictionary):
    src = ''
    for key, value in dictionary.items():
        if len(src):
            src += '\n'
        src += (key + ': ' + value + ';')
    return src
