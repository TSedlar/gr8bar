import os
import sys
import threading
import time
import types

from PyQt5 import QtCore, QtWidgets

from modules import network, linux, gallium_os
import ui
import tools


sys.path.append(os.path.dirname(sys.argv[1]))
cfg = __import__(os.path.basename(sys.argv[1].replace('.py', '')))

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint |
                      QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool |
                      QtCore.Qt.X11BypassWindowManagerHint)

bounds = cfg.bounds()
window.move(bounds['x'], bounds['y'])
window.setFixedSize(bounds['w'] if 'w' in bounds else bounds['width'],
                    bounds['h'] if 'h' in bounds else bounds['height'])

window_layout = QtWidgets.QHBoxLayout(window)
window_layout.setContentsMargins(0, 0, 0, 0)
window_layout.setSpacing(0)

properties = {}

modules = types.SimpleNamespace(network=network, linux=linux,
                                gallium_os=gallium_os)

data = types.SimpleNamespace(panel=window, layout=window_layout, ui=ui, os=os,
                             tools=tools, props=properties, modules=modules)


def clearLayout(layout):
    '''
    Removes the children from the given layout
    :param layout: The layout to remove from
    '''
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def render():
    '''
    Renders the bar from the given configuration file
    '''
    clearLayout(window_layout)
    cfg.config(data)

    window.ensurePolished()

    bg = window.palette().color(window.backgroundRole())
    if bg == QtCore.Qt.transparent:
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        window.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)


def run_updater(updater, tools, modules, properties):
    '''
    Runs an updater with the fed tools and properties
    :param updater: The updater to run
    :param tools: The tools api wrapper
    :param properties: The properties that the updater maintains
    '''
    while True:
        updater[0](tools, modules, properties)
        time.sleep(updater[1])


if __name__ == "__main__":
    updaters = cfg.init_prop_updaters()
    for updater in updaters:
        threading.Thread(target=run_updater,
                         args=(updater, tools, modules, properties,)).start()
    timer = QtCore.QTimer()
    timer.timeout.connect(render)
    timer.start(cfg.render_loop_delay())
    render()
    window.show()
    app.exec_()
