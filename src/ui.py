from PyQt5 import QtCore, QtWidgets, QtGui
import html

def add_center_label(layout, text, props={}):
    txt = QtWidgets.QLabel(html.unescape(text))
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

def add_hover_event(widget, callback):
    widget.setMouseTracking(True)
    widget.mouseMoveEvent = callback

def to_sheet(dict):
    src = ''
    for key, value in dict.items():
        if len(src) > 0:
            src += '\n'
        src += (key + ': ' + value + ';')
    return src