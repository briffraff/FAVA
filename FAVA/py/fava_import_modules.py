# PYTHON MODULES
import os
import sys
# import configparser
# import uuid
# import datetime
# import platform


networkPath = r"C:\Users\riffraff\Dropbox\Scripting"

myPaths = [
    os.path.join(networkPath, ("maxscript\\4_Final stage\\Config\\modules")),
    os.path.join(networkPath, ("Blender\\FAVA\\py")),
    # os.path.join(os.path.dirname(__file__), "venv_py3", "Lib", "site-packages")
]

for path in myPaths:
    if path not in sys.path:
        sys.path.append(path)


# for i in sys.path:
#     print(i)

# IMPORT RESOURCES
import fava_resource_rc

# from PySide2 import QtCore, QtGui, QtWidgets

# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QEasingCurve, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)

# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

# from PySide2.QtWidgets import *

# from PySide2.QtWidgets import (QApplication, QMainWindow, QSizeGrip)