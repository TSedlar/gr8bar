from PyQt5 import QtCore, QtWidgets, QtGui
import ui
import sys
import os

sys.path.append(os.path.dirname(sys.argv[1]))
cfg = __import__(os.path.basename(sys.argv[1].replace('.py', '')))

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint |
        QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.X11BypassWindowManagerHint |
        QtCore.Qt.Tool)

bounds = cfg.bounds()
window.move(bounds['x'], bounds['y'])
window.setFixedSize(bounds['w'] if 'w' in bounds else bounds['width'], 
        bounds['h'] if 'h' in bounds else bounds['height'])

layout = QtWidgets.QHBoxLayout(window)
layout.setContentsMargins(0, 0, 0, 0)
layout.setSpacing(0)

cfg.config(window, layout, ui)

window.ensurePolished()

bg = window.palette().color(window.backgroundRole())
if bg == QtCore.Qt.transparent:
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    window.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

window.show()
app.exec_()