# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PyQt5\source_code_for_pyqt5_tutorials\PyQt565\widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(989, 520)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(Widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setOpaqueResize(False)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.messageBrowser.setObjectName("messageBrowser")
        self.verticalLayout.addWidget(self.messageBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fontComboBox = QtWidgets.QFontComboBox(self.layoutWidget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_2.addWidget(self.fontComboBox)
        self.SizeComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.SizeComboBox.setObjectName("SizeComboBox")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.SizeComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.SizeComboBox)
        self.boldToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.boldToolBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldToolBtn.setIcon(icon)
        self.boldToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.boldToolBtn.setCheckable(True)
        self.boldToolBtn.setAutoRaise(True)
        self.boldToolBtn.setObjectName("boldToolBtn")
        self.horizontalLayout_2.addWidget(self.boldToolBtn)
        self.italicToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italicToolBtn.setIcon(icon1)
        self.italicToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.italicToolBtn.setCheckable(True)
        self.italicToolBtn.setAutoRaise(True)
        self.italicToolBtn.setObjectName("italicToolBtn")
        self.horizontalLayout_2.addWidget(self.italicToolBtn)
        self.underlineToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/under.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlineToolBtn.setIcon(icon2)
        self.underlineToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.underlineToolBtn.setCheckable(True)
        self.underlineToolBtn.setAutoRaise(True)
        self.underlineToolBtn.setObjectName("underlineToolBtn")
        self.horizontalLayout_2.addWidget(self.underlineToolBtn)
        self.colorToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorToolBtn.setIcon(icon3)
        self.colorToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.colorToolBtn.setAutoRaise(True)
        self.colorToolBtn.setObjectName("colorToolBtn")
        self.horizontalLayout_2.addWidget(self.colorToolBtn)
        self.saveToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToolBtn.setIcon(icon4)
        self.saveToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.saveToolBtn.setAutoRaise(True)
        self.saveToolBtn.setObjectName("saveToolBtn")
        self.horizontalLayout_2.addWidget(self.saveToolBtn)
        self.clearToolBtn = QtWidgets.QToolButton(self.layoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearToolBtn.setIcon(icon5)
        self.clearToolBtn.setIconSize(QtCore.QSize(22, 22))
        self.clearToolBtn.setAutoRaise(True)
        self.clearToolBtn.setObjectName("clearToolBtn")
        self.horizontalLayout_2.addWidget(self.clearToolBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.messageTextEdit = QtWidgets.QTextEdit(self.splitter)
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.userTableWidget = QtWidgets.QTableWidget(self.splitter_2)
        self.userTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.userTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.userTableWidget.setShowGrid(False)
        self.userTableWidget.setObjectName("userTableWidget")
        self.userTableWidget.setColumnCount(3)
        self.userTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sendButton = QtWidgets.QPushButton(Widget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.userNumLabel = QtWidgets.QLabel(Widget)
        self.userNumLabel.setObjectName("userNumLabel")
        self.horizontalLayout.addWidget(self.userNumLabel)
        spacerItem2 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.exitButton = QtWidgets.QPushButton(Widget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Widget)
        self.SizeComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "微信公众号：局域网聊天小工具"))
        self.SizeComboBox.setCurrentText(_translate("Widget", "9"))
        self.SizeComboBox.setItemText(0, _translate("Widget", "9"))
        self.SizeComboBox.setItemText(1, _translate("Widget", "10"))
        self.SizeComboBox.setItemText(2, _translate("Widget", "11"))
        self.SizeComboBox.setItemText(3, _translate("Widget", "12"))
        self.SizeComboBox.setItemText(4, _translate("Widget", "13"))
        self.SizeComboBox.setItemText(5, _translate("Widget", "14"))
        self.SizeComboBox.setItemText(6, _translate("Widget", "15"))
        self.SizeComboBox.setItemText(7, _translate("Widget", "16"))
        self.SizeComboBox.setItemText(8, _translate("Widget", "17"))
        self.SizeComboBox.setItemText(9, _translate("Widget", "18"))
        self.SizeComboBox.setItemText(10, _translate("Widget", "19"))
        self.SizeComboBox.setItemText(11, _translate("Widget", "20"))
        self.SizeComboBox.setItemText(12, _translate("Widget", "21"))
        self.SizeComboBox.setItemText(13, _translate("Widget", "22"))
        self.boldToolBtn.setToolTip(_translate("Widget", "加粗"))
        self.boldToolBtn.setText(_translate("Widget", "..."))
        self.italicToolBtn.setToolTip(_translate("Widget", "倾斜"))
        self.italicToolBtn.setText(_translate("Widget", "..."))
        self.underlineToolBtn.setToolTip(_translate("Widget", "下划线"))
        self.underlineToolBtn.setText(_translate("Widget", "..."))
        self.colorToolBtn.setToolTip(_translate("Widget", "更改字体颜色"))
        self.colorToolBtn.setText(_translate("Widget", "..."))
        self.saveToolBtn.setToolTip(_translate("Widget", "保存聊天记录"))
        self.saveToolBtn.setText(_translate("Widget", "..."))
        self.clearToolBtn.setToolTip(_translate("Widget", "清空聊天记录"))
        self.clearToolBtn.setText(_translate("Widget", "..."))
        item = self.userTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "用户名"))
        item = self.userTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "主机名"))
        item = self.userTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Widget", "IP地址"))
        self.sendButton.setText(_translate("Widget", "发送"))
        self.userNumLabel.setText(_translate("Widget", "在线用户：0人"))
        self.exitButton.setText(_translate("Widget", "退出"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

