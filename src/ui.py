import os
import html

from PyQt5 import QtCore, QtGui, QtWidgets

def res(py_file, file):
    '''
    Fetches a resource relative to the given file path
    :param py_file: The relative path file, usually __file__
    :param file: The resource file to obtain
    '''
    return os.path.join(os.path.dirname(py_file), file)


def toggle(widget):
    '''
    Toggles widget visibilitiy
    :param widget: The widget to hide or show
    '''
    if widget.isVisible():
        widget.hide()
    else:
        widget.show()


def create_popup(width, height, hex_bg):
    '''
    Creates a blank popup window with the given arguments
    :param width: The width of the popup
    :param height: The height of the popup
    :param hex_bg: The background color of the popup
    '''
    window = QtWidgets.QWidget()
    window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint |
                          QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool |
                          QtCore.Qt.X11BypassWindowManagerHint)
    window.setFixedSize(width, height)

    set_bg(window, hex_bg)
    set_border(window, hex_bg)
    if hex_bg == 'transparent':
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        window.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
    window_layout = QtWidgets.QHBoxLayout(window)
    window_layout.setContentsMargins(0, 0, 0, 0)
    window_layout.setSpacing(0)
    return window


def add_click_popup(parent, popup, alignment='center', offset=(0, 15)):
    '''
    Makes the given popup appear near the parent when the parent is clicked
    :param parent: The parent widget that the popup should be paired with
    :param popup: The popup to use
    :param alignment: The alignment of the popup (left, center, right)
    :param offset: An (x, y) tuple used for popup offset -- (0, 30) default
    '''
    def callback(_):
        toggle(popup)
        pt = parent.mapToGlobal(QtCore.QPoint(0, 0)) # absolute position
        x = pt.x()
        if alignment == 'center':
            x += (parent.width() / 2) - (popup.width() / 2)
        elif alignment == 'right':
            x -= (popup.width() - parent.width())
        x += offset[0]
        y = (pt.y() + parent.height() + offset[1])
        popup.move(x, y)
    add_click_event(parent, callback)


def add_image(layout, file_path, image_path, padding_width=0, overlay=None):
    '''
    Appends an image to the layout
    :param layout: The layout to append to
    :param file_path: The path to the file dir
    :param image_path: The path to the image
    :param padding_width: The amount of extra space on each side of the image
    '''
    label = QtWidgets.QLabel()
    pixmap = QtGui.QPixmap(res(file_path, image_path))
    if overlay is not None:
        recolor_pixmap(pixmap, overlay)
    label.setPixmap(pixmap)
    label.setFixedWidth(pixmap.width() + padding_width)
    label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(label)
    return label


def add_slant(layout, slant_type, color):
    '''
    Appends a slant to the bar
    :param layout: The layout to append to
    :param slant_type: The type of slant (lu = left-up, ld = left-down,
                 lui = left-up-inverted, ru = right-up, etc.)
    :param color: The hex-color that this slant should render as
    '''
    label = QtWidgets.QLabel()
    pixmap = QtGui.QPixmap(res(__file__, '../res/slant-%s.svg') % (slant_type))
    recolor_pixmap(pixmap, color)
    label.setPixmap(pixmap)
    label.setFixedWidth(pixmap.width())
    label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(label)
    return label


def add_center_label(layout, text, props={}):
    '''
    Appends a label with centered text to the bar
    :param layout: The layout to append to
    :param text: The text to render
    :param props: The properties or css values to use while rendering
    '''
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
    '''
    Adds a click event to the given widget
    :param widget: The widget to add a click event to
    :param callback: The callback to execute upon the event firing
    '''
    widget.mousePressEvent = callback


def add_hover_event(widget, enter_callback, leave_callback):
    '''
    Adds a hover event to the given widget
    :param widget: The widget to add a click event to
    :param enter_callback: The callback to execute upon the the hover start
    :param leave_callback: The callback to execute upon the the hover end
    '''
    widget.setMouseTracking(True)
    widget.enterEvent = enter_callback
    widget.leaveEvent = leave_callback

def show_hover(label, off_bg, on_bg, props, key):
    if key in props:
        set_bg(label, props[key])
    def enter_func(_):
        set_bg(label, on_bg)
        props[key] = on_bg
    def exit_func(_):
        set_bg(label, off_bg)
        props[key] = off_bg
    add_hover_event(label, enter_func, exit_func)


def add_label_hover(label, text, hover_callable, props, key):
    '''
    Adds a label hover event to the given label
    :param label: The label to add an event to
    :param hover_callable: A function/lambda that returns the text to use
                           upon hovering the label
    :param props: The properties associated with this label
    :param key: The key associated with the label text
    '''
    set_text(label, props[key] if key in props else text)
    def enter_func(_):
        hover_text = hover_callable()
        set_text(label, hover_text)
        props[key] = hover_text
    def exit_func(_):
        set_text(label, text)
        props[key] = text
    add_hover_event(label, enter_func, exit_func)


def set_text(label, text):
    '''
    Sets the text of the given label
    :param label: The label to use
    :param text: The text to use
    '''
    if text is None:
        text = ''
    label.setText(html.unescape(text))


def set_bg(widget, hex):
    '''
    Sets the background color of the given widget
    :param widget: The widget to use
    :param hex: The hex color to use
    '''
    append_css(widget, 'background-color: %s;' % hex)


def set_border(widget, border):
    '''
    Sets the border color of the given widget
    :param widget: The widget to use
    :param border: The hex color to use (or css value)
    '''
    append_css(widget, 'border: %s;' % border)


def recolor_pixmap(pixmap, hex):
    '''
    Recolors a pixmap to a hex color
    :param pixmap: The pixmap to recolor
    :param hex: The hex color to use
    '''
    painter = QtGui.QPainter(pixmap)
    painter.setCompositionMode(painter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), _to_qcol(hex))
    painter.end()


def add_paint_event(widget, new_event, include_old=True):
    '''
    Overrides the QWidget#paintEvent method to append the given event
    :param widget: The widget to paint on
    :param new_event: The new event to render, includes one event parameter
    :param include_old: Also pre-render the old paintEvent, true by default
    '''
    old_event = widget.paintEvent
    def override_paint_event(evt):
        if include_old:
            old_event(evt)
        new_event(evt)
    widget.paintEvent = override_paint_event


def add_border_line(widget, hex, height, bottom=True):
    '''
    Renders a border with the given arguments
    :param widget: The widget to add a border to
    :param hex: The color to render the border as
    :param height: The height of the border
    :param bottom: True to render at the bottom, False to render at the top.
    '''
    def paint_border_line(_):
        y_pos = widget.height() - height if bottom else 0
        painter = QtGui.QPainter(widget)
        painter.setCompositionMode(painter.CompositionMode_SourceIn)
        painter.fillRect(0, y_pos, widget.width(), height, _to_qcol(hex))
    add_paint_event(widget, paint_border_line)

def append_css(widget, css):
    '''
    Appends css to the given widget
    :param widget: The widget to style
    :param css: The css to append
    '''
    widget.setStyleSheet(widget.styleSheet() + css)


def _to_sheet(dictionary):
    '''
    Converts the given dictionary to a style sheet
    :param dictionary: The python dict object to use
    '''
    src = ''
    for key, value in dictionary.items():
        if len(src):
            src += '\n'
        src += '%s: %s;' % (key, value)
    return src


def _to_qcol(hex):
    '''
    Converts the given hex color to a Qt QColor object
    :param hex: The hex color to use
    '''
    rgb = _hex_to_rgb(hex)
    return QtGui.QColor(rgb[0], rgb[1], rgb[2])


def _hex_to_rgb(hex):
    '''
    Converts the given hex value to an rgb tuple
    :param hex: The hex color to convert
    '''
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
