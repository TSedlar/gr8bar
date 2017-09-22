import os
import sys

from PyQt5 import QtCore, QtWidgets

import ui

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


def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def render():
    clearLayout(window_layout)
    cfg.config(window, window_layout, ui)

    window.ensurePolished()

    bg = window.palette().color(window.backgroundRole())
    if bg == QtCore.Qt.transparent:
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        window.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)


if __name__ == "__main__":
    timer = QtCore.QTimer()
    timer.timeout.connect(render)
    timer.start(cfg.render_loop_delay())
    render()
    window.show()
    app.exec_()
