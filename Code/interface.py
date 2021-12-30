import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app: QtWidgets.QApplication = None
window: QtWidgets.QWidget = None


def create_interface():
    layout = QtWidgets.QHBoxLayout()

    # ---------------------------------------------------------------------------------------
    # Left Side Layout
    # ---------------------------------------------------------------------------------------
    left_side_layout = QtWidgets.QVBoxLayout()
    left_side_layout.setAlignment(QtCore.Qt.AlignTop)
    # ---- Elements
    left_side_layout.addWidget(QtWidgets.QPushButton("Hello World"))
    left_side_layout.addWidget(QtWidgets.QLineEdit())

    # ---------------------------------------------------------------------------------------
    # Right Side Layout
    # ---------------------------------------------------------------------------------------
    right_side_layout = QtWidgets.QVBoxLayout()
    right_side_layout.addWidget(QtWidgets.QPushButton("Hello World"))
    # ---- Elements
    right_side_layout.setAlignment(QtCore.Qt.AlignTop)

    # ---------------------------------------------------------------------------------------
    # Final Layout
    # ---------------------------------------------------------------------------------------
    layout.addLayout(left_side_layout)
    layout.addLayout(right_side_layout)

    window.setLayout(layout)


def create_window():
    global window
    window = QtWidgets.QWidget()
    window.setWindowTitle("Instagram Reel Creator")
    window.setGeometry(0, 0, 800, 600)
    window.setWindowIcon(QtGui.QIcon("Assets/icon.png"))

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
    create_interface()
    sys.exit(app.exec_())
