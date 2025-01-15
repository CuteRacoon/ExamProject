# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'static/ui/Calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Calendar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 800)
        Dialog.setStyleSheet("background-color: #fadccb;\n"
                             "font-family: Roboto;")
        self.eventsBtn = QtWidgets.QPushButton(Dialog)
        self.eventsBtn.setGeometry(QtCore.QRect(0, 110, 109, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventsBtn.sizePolicy().hasHeightForWidth())
        self.eventsBtn.setSizePolicy(sizePolicy)
        self.eventsBtn.setMaximumSize(QtCore.QSize(16777215, 110))
        self.eventsBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.eventsBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.eventsBtn.setAutoFillBackground(False)
        self.eventsBtn.setStyleSheet("QPushButton{padding: 12px 0px 16px 0px;\n"
                                     "  justify-content: center;\n"
                                     "  align-items: center;\n"
                                     "  gap: 4px;}\n"
                                     "QPushButton:hover {\n"
                                     "background: #FFFFFF;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background: #FFEAE5;\n"
                                     "}\n"
                                     "")
        self.eventsBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/ui\\../img/events_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eventsBtn.setIcon(icon)
        self.eventsBtn.setIconSize(QtCore.QSize(85, 100))
        self.eventsBtn.setCheckable(False)
        self.eventsBtn.setAutoDefault(False)
        self.eventsBtn.setDefault(False)
        self.eventsBtn.setFlat(True)
        self.eventsBtn.setObjectName("eventsBtn")
        self.calendarBtn = QtWidgets.QPushButton(Dialog)
        self.calendarBtn.setGeometry(QtCore.QRect(0, 220, 109, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarBtn.sizePolicy().hasHeightForWidth())
        self.calendarBtn.setSizePolicy(sizePolicy)
        self.calendarBtn.setMaximumSize(QtCore.QSize(16777215, 110))
        self.calendarBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calendarBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.calendarBtn.setAutoFillBackground(False)
        self.calendarBtn.setStyleSheet("QPushButton{padding: 12px 0px 16px 0px;\n"
                                       "  justify-content: center;\n"
                                       "  align-items: center;\n"
                                       "  gap: 4px;}\n"
                                       "QPushButton:hover {\n"
                                       "background: #FFF1ED;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background: #FFEAE5;\n"
                                       "}")
        self.calendarBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/ui\\../img/calendar_selected_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendarBtn.setIcon(icon1)
        self.calendarBtn.setIconSize(QtCore.QSize(85, 100))
        self.calendarBtn.setAutoDefault(False)
        self.calendarBtn.setDefault(False)
        self.calendarBtn.setFlat(True)
        self.calendarBtn.setObjectName("calendarBtn")
        self.topMenu = QtWidgets.QFrame(Dialog)
        self.topMenu.setGeometry(QtCore.QRect(110, 0, 971, 71))
        self.topMenu.setStyleSheet("padding: 0  50 0 0px;")
        self.topMenu.setObjectName("topMenu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topMenu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.categoryText = QtWidgets.QLabel(self.topMenu)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.categoryText.setFont(font)
        self.categoryText.setStyleSheet("color: #281401;\n"
                                        "padding-left: 50px;\n"
                                        "")
        self.categoryText.setObjectName("categoryText")
        self.horizontalLayout.addWidget(self.categoryText)
        self.Background = QtWidgets.QLabel(Dialog)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(110, 80, 991, 701))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.Background.setFont(font)
        self.Background.setStyleSheet("background-color: white;\n"
                                      "    border-top-left-radius: 20px;")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.accountBtn = QtWidgets.QPushButton(Dialog)
        self.accountBtn.setGeometry(QtCore.QRect(0, 340, 109, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountBtn.sizePolicy().hasHeightForWidth())
        self.accountBtn.setSizePolicy(sizePolicy)
        self.accountBtn.setMaximumSize(QtCore.QSize(16777215, 110))
        self.accountBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.accountBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.accountBtn.setAutoFillBackground(False)
        self.accountBtn.setStyleSheet("QPushButton{padding: 12px 0px 16px 0px;\n"
                                      "  justify-content: center;\n"
                                      "  align-items: center;\n"
                                      "  gap: 4px;}\n"
                                      "QPushButton:hover {\n"
                                      "background: #FFF1ED;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background: #FFEAE5;\n"
                                      "}")
        self.accountBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/ui\\../img/account_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon2)
        self.accountBtn.setIconSize(QtCore.QSize(85, 100))
        self.accountBtn.setAutoDefault(False)
        self.accountBtn.setDefault(False)
        self.accountBtn.setFlat(True)
        self.accountBtn.setObjectName("accountBtn")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(160, 110, 481, 461))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("selection-background-color: #e77d66;\n"
                                          "selection-gap: 10px;")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksBackground = QtWidgets.QLabel(Dialog)
        self.tasksBackground.setGeometry(QtCore.QRect(700, 110, 371, 641))
        self.tasksBackground.setStyleSheet(" border-radius: 15px;\n"
                                           "")
        self.tasksBackground.setText("")
        self.tasksBackground.setObjectName("tasksBackground")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(750, 130, 282, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChosenDate = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChosenDate.sizePolicy().hasHeightForWidth())
        self.ChosenDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ChosenDate.setFont(font)
        self.ChosenDate.setAlignment(QtCore.Qt.AlignCenter)
        self.ChosenDate.setObjectName("ChosenDate")
        self.verticalLayout.addWidget(self.ChosenDate)
        self.ToDoListLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToDoListLabel.sizePolicy().hasHeightForWidth())
        self.ToDoListLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.ToDoListLabel.setFont(font)
        self.ToDoListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ToDoListLabel.setObjectName("ToDoListLabel")
        self.verticalLayout.addWidget(self.ToDoListLabel)
        self.NoEventsLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoEventsLabel.sizePolicy().hasHeightForWidth())
        self.NoEventsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.NoEventsLabel.setFont(font)
        self.NoEventsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NoEventsLabel.setObjectName("NoEventsLabel")
        self.verticalLayout.addWidget(self.NoEventsLabel)
        self.tasksFrame = QtWidgets.QFrame(Dialog)
        self.tasksFrame.setStyleSheet("background-color: None")
        self.tasksFrame.setGeometry(QtCore.QRect(740, 220, 301, 381))
        self.tasksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tasksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tasksFrame.setObjectName("tasksFrame")
        self.showEventButton1 = QtWidgets.QPushButton(self.tasksFrame)
        self.showEventButton1.setGeometry(QtCore.QRect(10, 10, 280, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showEventButton1.sizePolicy().hasHeightForWidth())
        self.showEventButton1.setSizePolicy(sizePolicy)
        self.showEventButton1.setMinimumSize(QtCore.QSize(280, 50))
        self.showEventButton1.setMaximumSize(QtCore.QSize(280, 50))
        self.showEventButton1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.showEventButton1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 20%;")
        self.showEventButton1.setCheckable(False)
        self.showEventButton1.setAutoRepeat(False)
        self.showEventButton1.setAutoExclusive(False)
        self.showEventButton1.setAutoRepeatDelay(0)
        self.showEventButton1.setAutoRepeatInterval(0)
        self.showEventButton1.setAutoDefault(True)
        self.showEventButton1.setDefault(False)
        self.showEventButton1.setFlat(False)
        self.showEventButton1.setObjectName("showEventButton")
        self.showEventButton2 = QtWidgets.QPushButton(self.tasksFrame)
        self.showEventButton2.setGeometry(QtCore.QRect(10, 75, 280, 50))
        self.showEventButton2.setMinimumSize(QtCore.QSize(280, 50))
        self.showEventButton2.setMaximumSize(QtCore.QSize(280, 50))
        self.showEventButton2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 20%;")
        self.showEventButton2.setObjectName("showEventButton2")
        self.showEventButton3 = QtWidgets.QPushButton(self.tasksFrame)
        self.showEventButton3.setGeometry(QtCore.QRect(10, 140, 280, 50))
        self.showEventButton3.setMinimumSize(QtCore.QSize(280, 50))
        self.showEventButton3.setMaximumSize(QtCore.QSize(280, 50))
        self.showEventButton3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 20%;")
        self.showEventButton3.setObjectName("showEventButton3")
        self.showEventButton4 = QtWidgets.QPushButton(self.tasksFrame)
        self.showEventButton4.setGeometry(QtCore.QRect(10, 205, 280, 50))
        self.showEventButton4.setMinimumSize(QtCore.QSize(280, 50))
        self.showEventButton4.setMaximumSize(QtCore.QSize(280, 50))
        self.showEventButton4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 20%;")
        self.showEventButton4.setObjectName("showEventButton4")
        self.showEventButton5 = QtWidgets.QPushButton(self.tasksFrame)
        self.showEventButton5.setGeometry(QtCore.QRect(10, 270, 280, 50))
        self.showEventButton5.setMinimumSize(QtCore.QSize(280, 50))
        self.showEventButton5.setMaximumSize(QtCore.QSize(280, 50))
        self.showEventButton5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 20%;")
        self.showEventButton5.setObjectName("showEventButton5")
        self.addEventBtn = QtWidgets.QPushButton(Dialog)
        self.addEventBtn.setGeometry(QtCore.QRect(470, 590, 170, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addEventBtn.sizePolicy().hasHeightForWidth())
        self.addEventBtn.setSizePolicy(sizePolicy)
        self.addEventBtn.setMaximumSize(QtCore.QSize(170, 50))
        self.addEventBtn.setBaseSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.addEventBtn.setFont(font)
        self.addEventBtn.setStyleSheet("QPushButton{color: #281401;\n"
                                       "  position: relative;\n"
                                       "  width: 100%;\n"
                                       "  height: 100%;\n"
                                       "  background-color: #ffffff;\n"
                                       "  justify-content: center;\n"
                                       "  align-items: center;\n"
                                       "  border-radius: 10px;\n"
                                       "  border: 3px solid #fadccb;\n"
                                       "  gap: 20px;\n"
                                       "  display: flex;\n"
                                       "  padding: 5px 20px 5px 20px;\n"
                                       "  border-radius: 20px;}\n"
                                       "QPushButton:hover {\n"
                                       "background: #FFF1ED;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background: #FFEAE5;\n"
                                       "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("static/ui\\../img/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEventBtn.setIcon(icon3)
        self.addEventBtn.setIconSize(QtCore.QSize(28, 28))
        self.addEventBtn.setAutoRepeatInterval(100)
        self.addEventBtn.setObjectName("addEventBtn")
        self.Background.raise_()
        self.tasksBackground.raise_()
        self.layoutWidget.raise_()
        self.eventsBtn.raise_()
        self.calendarBtn.raise_()
        self.topMenu.raise_()
        self.accountBtn.raise_()
        self.calendarWidget.raise_()
        self.tasksFrame.raise_()
        self.addEventBtn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.categoryText.setText(_translate("Dialog", "Календарь"))
        self.ChosenDate.setText(_translate("Dialog", "dd/mm/yyyy"))
        self.ToDoListLabel.setText(_translate("Dialog", "Мероприятия:"))
        self.NoEventsLabel.setText(_translate("Dialog", "Текст"))
        self.showEventButton1.setText(_translate("Dialog", "Задача"))
        self.showEventButton2.setText(_translate("Dialog", "Задача"))
        self.showEventButton3.setText(_translate("Dialog", "Задача"))
        self.showEventButton4.setText(_translate("Dialog", "Задача"))
        self.showEventButton5.setText(_translate("Dialog", "Задача"))
        self.addEventBtn.setText(_translate("Dialog", "Добавить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI_Calendar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
