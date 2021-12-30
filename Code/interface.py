import sys
from PyQt5 import QtWidgets

app: QtWidgets.QApplication = None
window: QtWidgets.QWidget = None


def create_window():
    global window
    window = QtWidgets.QWidget()
    window.setWindowTitle("Instagram Reel Creator")
    window.setGeometry(0, 0, 800, 600)

    screen = QtWidgets.QApplication.desktop().screenNumber(
        QtWidgets.QApplication.desktop().cursor().pos())
    window.move(
        # X-Axis Position
        QtWidgets.QDesktopWidget().screenGeometry(screen).center().x() -
        window.frameGeometry().center().x(),
        # Y-Axis Position
        QtWidgets.QDesktopWidget().screenGeometry(screen).center().y() -
        window.frameGeometry().center().y())
    window.show()


def start_gui():
    global app
    app = QtWidgets.QApplication(sys.argv)
    create_window()
    sys.exit(app.exec_())
