# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hang/workspace/atomqq_py/src/Atom/UI/login.ui'
#
# Created: Thu Apr 26 06:00:08 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginWindow(object):
    defaultFacePath='Res/img/header.bmp'
    
    def setupUi(self, LoginWindow):
        self.facePath=str(self.defaultFacePath)
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.setWindowModality(QtCore.Qt.WindowModal)
        LoginWindow.setEnabled(True)
        LoginWindow.resize(386, 360)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(0, 0))
        LoginWindow.setMaximumSize(QtCore.QSize(9999, 9999))
        LoginWindow.setMouseTracking(False)
        LoginWindow.setWindowTitle(QtGui.QApplication.translate("LoginWindow", "AtomQQ", None, QtGui.QApplication.UnicodeUTF8))
        LoginWindow.setWindowFilePath(_fromUtf8(""))
        LoginWindow.setSizeGripEnabled(False)
        LoginWindow.setModal(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(LoginWindow)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(30, 15, 30, 30)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.logo = QtGui.QLabel(LoginWindow)
        self.logo.setText(QtGui.QApplication.translate("LoginWindow", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.verticalLayout_2.addWidget(self.logo)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.face = QtGui.QLabel(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.face.sizePolicy().hasHeightForWidth())
        self.face.setSizePolicy(sizePolicy)
        self.face.setText(_fromUtf8(""))
        self.face.setPixmap(QtGui.QPixmap(_fromUtf8(self.facePath)))
        self.face.setObjectName(_fromUtf8("face"))
        self.horizontalLayout_5.addWidget(self.face)
        self.line = QtGui.QFrame(LoginWindow)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gdlayout = QtGui.QGridLayout()
        self.gdlayout.setObjectName(_fromUtf8("gdlayout"))
        self.label = QtGui.QLabel(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setText(QtGui.QApplication.translate("LoginWindow", "帐   号", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gdlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(LoginWindow)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setText(QtGui.QApplication.translate("LoginWindow", "密   码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gdlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.qqnum = QtGui.QComboBox(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qqnum.sizePolicy().hasHeightForWidth())
        self.qqnum.setSizePolicy(sizePolicy)
        self.qqnum.setEditable(True)
        self.qqnum.setObjectName(_fromUtf8("qqnum"))
        self.qqnum.addItem(_fromUtf8(""))
        self.qqnum.setItemText(0, QtGui.QApplication.translate("LoginWindow", "287044581", None, QtGui.QApplication.UnicodeUTF8))
        self.qqnum.addItem(_fromUtf8(""))
        self.qqnum.setItemText(1, QtGui.QApplication.translate("LoginWindow", "1640228848", None, QtGui.QApplication.UnicodeUTF8))
        self.gdlayout.addWidget(self.qqnum, 0, 1, 1, 2)
        self.checkTxt = QtGui.QLabel(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTxt.sizePolicy().hasHeightForWidth())
        self.checkTxt.setSizePolicy(sizePolicy)
        self.checkTxt.setMinimumSize(QtCore.QSize(0, 0))
        self.checkTxt.setText(QtGui.QApplication.translate("LoginWindow", "验证码  ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checkTxt.setWordWrap(False)
        self.checkTxt.setObjectName(_fromUtf8("checkTxt"))
        self.gdlayout.addWidget(self.checkTxt, 3, 0, 1, 1)
        self.qqpasswd = QtGui.QLineEdit(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qqpasswd.sizePolicy().hasHeightForWidth())
        self.qqpasswd.setSizePolicy(sizePolicy)
        self.qqpasswd.setText(QtGui.QApplication.translate("LoginWindow", "123", None, QtGui.QApplication.UnicodeUTF8))
        self.qqpasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.qqpasswd.setObjectName(_fromUtf8("qqpasswd"))
        self.gdlayout.addWidget(self.qqpasswd, 2, 1, 1, 2)
        self.checkImg = QtGui.QLabel(LoginWindow)
        self.checkImg.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkImg.sizePolicy().hasHeightForWidth())
        self.checkImg.setSizePolicy(sizePolicy)
        self.checkImg.setMinimumSize(QtCore.QSize(0, 0))
        self.checkImg.setText(_fromUtf8(""))
        self.checkImg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checkImg.setObjectName(_fromUtf8("checkImg"))
        self.gdlayout.addWidget(self.checkImg, 4, 1, 1, 2)
        self.checkCode = QtGui.QLineEdit(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkCode.sizePolicy().hasHeightForWidth())
        self.checkCode.setSizePolicy(sizePolicy)
        self.checkCode.setObjectName(_fromUtf8("checkCode"))
        self.gdlayout.addWidget(self.checkCode, 3, 1, 1, 2)
        self.changeImg = QtGui.QLabel(LoginWindow)
        self.changeImg.setText(QtGui.QApplication.translate("LoginWindow", "<a href=\"http://w.w.w\">更 换</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.changeImg.setObjectName(_fromUtf8("changeImg"))
        self.gdlayout.addWidget(self.changeImg, 5, 1, 1, 2)
        self.verticalLayout.addLayout(self.gdlayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cbxRemeberPasswd = QtGui.QCheckBox(LoginWindow)
        self.cbxRemeberPasswd.setText(QtGui.QApplication.translate("LoginWindow", "记住密码", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxRemeberPasswd.setObjectName(_fromUtf8("cbxRemeberPasswd"))
        self.horizontalLayout.addWidget(self.cbxRemeberPasswd)
        self.cbxAutoLogin = QtGui.QCheckBox(LoginWindow)
        self.cbxAutoLogin.setText(QtGui.QApplication.translate("LoginWindow", "自动登录", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxAutoLogin.setObjectName(_fromUtf8("cbxAutoLogin"))
        self.horizontalLayout.addWidget(self.cbxAutoLogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.loginMsg = QtGui.QLabel(LoginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginMsg.sizePolicy().hasHeightForWidth())
        self.loginMsg.setSizePolicy(sizePolicy)
        self.loginMsg.setLineWidth(2)
        self.loginMsg.setMidLineWidth(0)
        self.loginMsg.setText(_fromUtf8(""))
        self.loginMsg.setTextFormat(QtCore.Qt.RichText)
        self.loginMsg.setWordWrap(True)
        self.loginMsg.setObjectName(_fromUtf8("loginMsg"))
        self.verticalLayout_2.addWidget(self.loginMsg)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.loginStatus = QtGui.QComboBox(LoginWindow)
        self.loginStatus.setObjectName(_fromUtf8("loginStatus"))
        self.loginStatus.addItem(_fromUtf8(""))
        self.loginStatus.setItemText(0, QtGui.QApplication.translate("LoginWindow", "我在线上", None, QtGui.QApplication.UnicodeUTF8))
        self.loginStatus.addItem(_fromUtf8(""))
        self.loginStatus.setItemText(1, QtGui.QApplication.translate("LoginWindow", "Q我吧", None, QtGui.QApplication.UnicodeUTF8))
        self.loginStatus.addItem(_fromUtf8(""))
        self.loginStatus.setItemText(2, QtGui.QApplication.translate("LoginWindow", "忙碌", None, QtGui.QApplication.UnicodeUTF8))
        self.loginStatus.addItem(_fromUtf8(""))
        self.loginStatus.setItemText(3, QtGui.QApplication.translate("LoginWindow", "隐身", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_7.addWidget(self.loginStatus)
        spacerItem1 = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btnLogin = QtGui.QPushButton(LoginWindow)
        self.btnLogin.setText(QtGui.QApplication.translate("LoginWindow", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.horizontalLayout_7.addWidget(self.btnLogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        pass
    
    def setCheckAreaVisibale(self,boolean):
        self.checkCode.setEnabled(boolean)
        self.checkImg.setVisible(boolean)
        self.changeImg.setVisible(boolean)
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginWindow = QtGui.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

