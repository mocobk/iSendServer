# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import qss, rc


class WindowUI(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_close = QPushButton('×')
        self.btn_close.setObjectName('btn_close')
        self.btn_close.setFixedSize(60, 30)
        # 仅设置点击聚焦，这样按tab就不会聚焦了
        self.btn_close.setFocusPolicy(Qt.ClickFocus)

        self.btn_min = QPushButton('—')
        self.btn_min.setFixedSize(60, 30)
        self.btn_min.setObjectName('btn_min')
        self.btn_min.setFocusPolicy(Qt.ClickFocus)

        self.hbox_1 = QHBoxLayout()
        self.hbox_1.addStretch(1)
        self.hbox_1.addWidget(self.btn_min)
        self.hbox_1.addWidget(self.btn_close)

        ######################################
        self.label_1 = QLabel('Host')
        self.combobox = QComboBox()
        self.combobox.setFixedSize(300, 30)
        self.label_2 = QLabel('Port')
        self.line_edit = QLineEdit()
        self.line_edit.setFixedHeight(30)
        self.btn_start = QPushButton('Start')
        self.btn_start.setObjectName('btn_start')
        self.btn_start.setFixedSize(100, 30)

        self.hbox_2 = QHBoxLayout()
        self.hbox_2.addWidget(self.label_1)
        self.hbox_2.addWidget(self.combobox)
        self.hbox_2.addWidget(self.label_2)
        self.hbox_2.addWidget(self.line_edit)
        self.hbox_2.addWidget(self.btn_start)
        self.hbox_2.setSpacing(10)
        self.hbox_2.setContentsMargins(10, 30, 10, 10)

        ######################################
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # 设置只读
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 设置不显示滚动条

        self.hbox_3 = QHBoxLayout()
        self.hbox_3.addWidget(self.text_edit)
        self.hbox_3.setContentsMargins(10, 0, 10, 10)

        ######################################
        self.grid = QGridLayout()
        self.grid.addItem(self.hbox_1, 0, 3, 1, 2)
        self.grid.addItem(self.hbox_2, 1, 0, 1, 5)
        self.grid.addItem(self.hbox_3, 2, 0, 1, 5)
        self.grid.setContentsMargins(0, 0, 0, 0)

        self.resize(600, 300)
        self.setWindowTitle('iSendServer')
        self.setWindowIcon(QIcon(':rc/icon.png'))
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.grid)

        self.setWindowFlags(Qt.FramelessWindowHint)

        style_qss = qss.ui_style
        self.setStyleSheet(style_qss)

        self.btn_close.clicked.connect(self.close)
        self.btn_min.clicked.connect(self.showMinimized)

        self.show()
        # 在show后使用setFocus()设置默认第一个focus
        self.btn_start.setFocus()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()  # 记录点击坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = WindowUI()
    sys.exit(app.exec_())
