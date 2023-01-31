# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FAVA-ui.ui'
##
## Created by: qc.Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# IMPORT PYSIDE2 MODULES
import fava_import_modules as modules

import PySide2.QtWidgets as qw
import PySide2.QtGui as qg
import PySide2.QtCore as qc

_translate = qc.QCoreApplication.translate


class UI_Fava():
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.setWindowFlag(qc.Qt.FramelessWindowHint)
        MainWindow.setWindowModality(qc.Qt.NonModal)
        MainWindow.resize(400, 600)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Preferred, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(qc.QSize(450, 600))
        # MainWindow.setMaximumSize(qc.QSize(800, 600))
        MainWindow.setSizeIncrement(qc.QSize(0, 0))
        MainWindow.setBaseSize(qc.QSize(0, 0))
        MainWindow.setLayoutDirection(qc.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        MainWindow.setToolButtonStyle(qc.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(qw.QMainWindow.AllowTabbedDocks|qw.QMainWindow.AnimatedDocks|qw.QMainWindow.VerticalTabs)
        self.centralwidget = qw.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setBaseSize(qc.QSize(0, 0))
        self.verticalLayout = qw.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

##---FRAME TOP ------------------------------------------
        self.frame_top = qw.QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(qc.QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_top.setFrameShape(qw.QFrame.NoFrame)
        self.frame_top.setFrameShadow(qw.QFrame.Raised)
        self.frame_top.setLineWidth(0)
        self.horizontalLayout = qw.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)


        self.frame_sandwitch = qw.QFrame(self.frame_top)
        self.frame_sandwitch.setObjectName(u"frame_sandwitch")
        self.frame_sandwitch.setMinimumSize(qc.QSize(50, 40))
        self.frame_sandwitch.setMaximumSize(qc.QSize(50, 16777215))
        self.frame_sandwitch.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.frame_sandwitch.setFrameShape(qw.QFrame.NoFrame)
        self.frame_sandwitch.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_6 = qw.QHBoxLayout(self.frame_sandwitch)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 0)

        self.sandwitch_btn = qw.QPushButton(self.frame_sandwitch)
        self.sandwitch_btn.setObjectName(u"sandwitch_btn")
        self.sandwitch_btn.setMinimumSize(qc.QSize(32, 32))
        self.sandwitch_btn.setMaximumSize(qc.QSize(32, 32))
        self.sandwitch_btn.setStyleSheet(u"#sandwitch_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_sandwitch/images/sandwitch.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#sandwitch_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#sandwitch_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.sandwitch_btn.setAutoDefault(False)
        self.sandwitch_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.sandwitch_btn)


        self.horizontalLayout.addWidget(self.frame_sandwitch)

        self.frame_logo = qw.QFrame(self.frame_top)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
        "")
        self.frame_logo.setFrameShape(qw.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_3 = qw.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        
        self.horizontalSpacer = qw.QSpacerItem(0, 20, qw.QSizePolicy.Expanding, qw.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.fava_logo = qw.QFrame(self.frame_logo)
        self.fava_logo.setObjectName(u"fava_logo")
        self.fava_logo.setMinimumSize(qc.QSize(94, 56))
        self.fava_logo.setMaximumSize(qc.QSize(94, 56))
        # self.fava_logo.setFlat(True)

        self.horizontalLayout_3.addWidget(self.fava_logo)

        self.horizontalSpacer_2 = qw.QSpacerItem(0, 20, qw.QSizePolicy.Expanding , qw.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_logo)

        self.frame_top_buttons = qw.QFrame(self.frame_top)
        self.frame_top_buttons.setObjectName(u"frame_top_buttons")
        self.frame_top_buttons.setMinimumSize(qc.QSize(70, 0))
        self.frame_top_buttons.setMaximumSize(qc.QSize(70, 16777215))
        self.frame_top_buttons.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
        "")
        self.frame_top_buttons.setFrameShape(qw.QFrame.NoFrame)
        self.frame_top_buttons.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_7 = qw.QHBoxLayout(self.frame_top_buttons)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 5, 0)
        self.minimize = qw.QPushButton(self.frame_top_buttons)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setToolTip("Minimize")
        self.minimize.setMinimumSize(qc.QSize(14, 14))
        self.minimize.setMaximumSize(qc.QSize(14, 14))

        font = qg.QFont()
        font.setFamily(u"Bahnschrift")
        font.setBold(True)
        font.setWeight(75)
        self.minimize.setFont(font)
        self.minimize.setStyleSheet(u"#minimize {\n"
        "	color: rgb(255, 255, 255);\n"
        "	border-radius: 2px;\n"
        "	border: 1px solid   rgb(255, 255, 255);\n"
        "\n"
        "}\n"
        "\n"
        "#minimize:hover {\n"
        "	color:  rgb(211, 0, 4);\n"
        "}\n"
        "")
        self.minimize.setFlat(True)

        self.horizontalLayout_7.addWidget(self.minimize)

        self.maximize = qw.QPushButton(self.frame_top_buttons)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setToolTip("Maximize")
        self.maximize.setMinimumSize(qc.QSize(14, 14))
        self.maximize.setMaximumSize(qc.QSize(14, 14))
        self.maximize.setFont(font)
        self.maximize.setStyleSheet(u"#maximize {\n"
        "	color: rgb(255, 255, 255);\n"
        "	border-radius: 2px;\n"
        "	border: 1px solid rgb(255, 255, 255);\n"
        " 	padding-top:7px;\n"
        "}\n"
        "\n"
        "#maximize:hover {\n"
        "	color:  rgb(211, 0, 4);\n"
        "       border-radius: 2px;"
        "	border: 2px solid  rgb(211, 0, 4);\n"
        "}\n"
        "")
        self.maximize.setFlat(True)

        self.horizontalLayout_7.addWidget(self.maximize)

        self.exit = qw.QPushButton(self.frame_top_buttons)
        self.exit.setObjectName(u"exit")
        self.exit.setToolTip("Close FAVA")
        self.exit.setMinimumSize(qc.QSize(14, 15))
        self.exit.setMaximumSize(qc.QSize(14, 15))
        font1 = qg.QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(6)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.exit.setFont(font1)
        self.exit.setStyleSheet(u"#exit {\n"
        "  color: rgb(255, 255, 255);\n"
        "  border-radius: 2px;\n"
        "  background-color: rgb(211, 0, 4);\n"
        "  border: 2px solid rgb(211, 0, 4);\n"
        "}\n"
        "\n"
        "#exit:hover {\n"
        "  color: rgb(211, 0, 4);\n"
        "  border-radius: 2px;\n"
        "  background-color: rgb(255, 255, 255);\n"
        "}")
        self.exit.setFlat(True)

        self.horizontalLayout_7.addWidget(self.exit)


        self.horizontalLayout.addWidget(self.frame_top_buttons)


        self.verticalLayout.addWidget(self.frame_top)



##---FRAME MID ---------------------------------------
        self.frame_mid = qw.QFrame(self.centralwidget)
        self.frame_mid.setObjectName(u"frame_mid")
        self.frame_mid.setMaximumSize(qc.QSize(16777215, 16777215))
        self.frame_mid.setStyleSheet(u"")
        self.frame_mid.setFrameShape(qw.QFrame.NoFrame)
        self.frame_mid.setFrameShadow(qw.QFrame.Raised)
        self.frame_mid.setLineWidth(0)
        self.horizontalLayout_2 = qw.QHBoxLayout(self.frame_mid)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_leftmenu = qw.QFrame(self.frame_mid)
        self.frame_leftmenu.setObjectName(u"frame_leftmenu")
        self.frame_leftmenu.setEnabled(True)

        ## DEFAULT MENU - EXPANDED USER VALUE OF 200. FOR DEFAULT MENU - COLLAPSED USE VALUE OF 50
        self.frame_leftmenu.setMinimumSize(qc.QSize(200, 0))
        self.frame_leftmenu.setMaximumSize(qc.QSize(50, 16777215))
        self.frame_leftmenu.setBaseSize(qc.QSize(0, 0))
        self.frame_leftmenu.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
        "font: 63 10pt \"Bahnschrift SemiBold SemiConden\";")
        self.frame_leftmenu.setFrameShape(qw.QFrame.NoFrame)
        self.frame_leftmenu.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_5 = qw.QHBoxLayout(self.frame_leftmenu)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu_icons = qw.QFrame(self.frame_leftmenu)
        self.menu_icons.setObjectName(u"menu_icons")
        self.menu_icons.setMinimumSize(qc.QSize(160, 300))
        self.menu_icons.setMaximumSize(qc.QSize(50, 16777215))
        self.menu_icons.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "")
        self.menu_icons.setFrameShape(qw.QFrame.NoFrame)
        self.menu_icons.setFrameShadow(qw.QFrame.Raised)
        self.verticalLayout_4 = qw.QVBoxLayout(self.menu_icons)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftmenu_top = qw.QFrame(self.menu_icons)
        self.leftmenu_top.setObjectName(u"leftmenu_top")
        self.leftmenu_top.setMinimumSize(qc.QSize(0, 0))
        self.leftmenu_top.setMaximumSize(qc.QSize(16777215, 16777215))
        self.leftmenu_top.setStyleSheet(u"")
        self.leftmenu_top.setFrameShape(qw.QFrame.NoFrame)
        self.leftmenu_top.setFrameShadow(qw.QFrame.Raised)

        
        self.gridLayout_2 = qw.QGridLayout(self.leftmenu_top)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setContentsMargins(-1, 0, 0, -1)

        ## CREATE FOLDER
        self.createfolder_btn = qw.QPushButton(self.leftmenu_top)
        self.createfolder_btn.setObjectName(u"createfolder_btn")
        self.createfolder_btn.setMinimumSize(qc.QSize(32, 32))
        self.createfolder_btn.setMaximumSize(qc.QSize(32, 32))
        self.createfolder_btn.setStyleSheet(u"#createfolder_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_createfolder/images/folder_market.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#createfolder_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#createfolder_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.createfolder_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.createfolder_btn, 0, 0, 1, 1)


        self.createfolder_label = qw.QLabel(self.leftmenu_top)
        self.createfolder_label.setObjectName(u"createfolder_label")
        self.createfolder_label.setMinimumSize(qc.QSize(0, 32))
        self.createfolder_label.setMaximumSize(qc.QSize(16777215, 32))
        self.createfolder_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.createfolder_label.setMargin(0)

        self.gridLayout_2.addWidget(self.createfolder_label, 0, 1, 1, 1)


        ## IMPORTER
        self.importer_btn = qw.QPushButton(self.leftmenu_top)
        self.importer_btn.setObjectName(u"importer_btn")
        self.importer_btn.setMinimumSize(qc.QSize(32, 32))
        self.importer_btn.setMaximumSize(qc.QSize(32, 32))
        self.importer_btn.setStyleSheet(u"#importer_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_importer/images/importer.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#importer_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#importer_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "")
        self.importer_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.importer_btn, 1, 0, 1, 1)

        self.importer_label = qw.QLabel(self.leftmenu_top)
        self.importer_label.setObjectName(u"importer_label")
        self.importer_label.setMinimumSize(qc.QSize(0, 32))
        self.importer_label.setMaximumSize(qc.QSize(16777215, 32))
        font2 = qg.QFont()
        font2.setFamily(u"Bahnschrift SemiBold SemiConden")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(7)
        self.importer_label.setFont(font2)
        self.importer_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.importer_label.setMargin(0)

        self.gridLayout_2.addWidget(self.importer_label, 1, 1, 1, 1)


        ## SHELL
        self.shell_btn = qw.QPushButton(self.leftmenu_top)
        self.shell_btn.setObjectName(u"shell_btn")
        self.shell_btn.setMinimumSize(qc.QSize(32, 32))
        self.shell_btn.setMaximumSize(qc.QSize(32, 32))
        self.shell_btn.setStyleSheet(u"#shell_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_shell/images/shell.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#shell_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#shell_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "")
        self.shell_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.shell_btn, 2, 0, 1, 1)

        self.shell_label = qw.QLabel(self.leftmenu_top)
        self.shell_label.setObjectName(u"shell_label")
        self.shell_label.setMinimumSize(qc.QSize(0, 32))
        self.shell_label.setMaximumSize(qc.QSize(16777215, 32))
        self.shell_label.setFont(font2)
        self.shell_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.shell_label.setMargin(0)

        self.gridLayout_2.addWidget(self.shell_label, 2, 1, 1, 1)


        ## EXPORTER
        self.exporter_btn = qw.QPushButton(self.leftmenu_top)
        self.exporter_btn.setObjectName(u"exporter_btn")
        self.exporter_btn.setMinimumSize(qc.QSize(32, 32))
        self.exporter_btn.setMaximumSize(qc.QSize(32, 32))
        self.exporter_btn.setStyleSheet(u"#exporter_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_exporter/images/exporter.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#exporter_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#exporter_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "")
        self.exporter_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.exporter_btn, 3, 0, 1, 1)

        self.exporter_label = qw.QLabel(self.leftmenu_top)
        self.exporter_label.setObjectName(u"exporter_label")
        self.exporter_label.setMinimumSize(qc.QSize(0, 32))
        self.exporter_label.setMaximumSize(qc.QSize(16777215, 32))
        self.exporter_label.setFont(font2)
        self.exporter_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.exporter_label.setMargin(0)

        self.gridLayout_2.addWidget(self.exporter_label, 3, 1, 1, 1)


        ## UV PRINTER
        self.uvprinter_btn = qw.QPushButton(self.leftmenu_top)
        self.uvprinter_btn.setObjectName(u"uvprinter_btn")
        self.uvprinter_btn.setMinimumSize(qc.QSize(32, 32))
        self.uvprinter_btn.setMaximumSize(qc.QSize(32, 32))
        self.uvprinter_btn.setStyleSheet(u"#uvprinter_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_uvprint/images/uvprinter.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "\n"
        "#uvprinter_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#uvprinter_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.uvprinter_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.uvprinter_btn, 4, 0, 1, 1)

        self.uvprinter_label = qw.QLabel(self.leftmenu_top)
        self.uvprinter_label.setObjectName(u"uvprinter_label")
        self.uvprinter_label.setMinimumSize(qc.QSize(0, 32))
        self.uvprinter_label.setMaximumSize(qc.QSize(16777215, 32))
        self.uvprinter_label.setFont(font2)
        self.uvprinter_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.uvprinter_label.setMargin(0)

        self.gridLayout_2.addWidget(self.uvprinter_label, 4, 1, 1, 1)


        ## MATERIALS
        self.materials_btn = qw.QPushButton(self.leftmenu_top)
        self.materials_btn.setObjectName(u"materials_btn")
        self.materials_btn.setMinimumSize(qc.QSize(32, 32))
        self.materials_btn.setMaximumSize(qc.QSize(32, 32))
        self.materials_btn.setStyleSheet(u"#materials_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_materials/images/materials.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#materials_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#materials_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "")
        self.materials_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.materials_btn, 5, 0, 1, 1)

        self.materials_label = qw.QLabel(self.leftmenu_top)
        self.materials_label.setObjectName(u"materials_label")
        self.materials_label.setMinimumSize(qc.QSize(0, 32))
        self.materials_label.setMaximumSize(qc.QSize(16777215, 32))
        self.materials_label.setFont(font2)
        self.materials_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.materials_label.setMargin(0)

        self.gridLayout_2.addWidget(self.materials_label, 5, 1, 1, 1)


        ## RENDER THUMBS
        self.render_thumbs_btn = qw.QPushButton(self.leftmenu_top)
        self.render_thumbs_btn.setObjectName(u"render_thumbs_btn")
        self.render_thumbs_btn.setMinimumSize(qc.QSize(32, 32))
        self.render_thumbs_btn.setMaximumSize(qc.QSize(32, 32))
        self.render_thumbs_btn.setStyleSheet(u"#render_thumbs_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_thumbrender/images/t_render.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#render_thumbs_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#render_thumbs_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.render_thumbs_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.render_thumbs_btn, 6, 0, 1, 1)

        self.render_thumbs_label = qw.QLabel(self.leftmenu_top)
        self.render_thumbs_label.setObjectName(u"render_thumbs_label")
        self.render_thumbs_label.setMinimumSize(qc.QSize(0, 32))
        self.render_thumbs_label.setMaximumSize(qc.QSize(16777215, 32))
        self.render_thumbs_label.setFont(font2)
        self.render_thumbs_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.render_thumbs_label.setMargin(0)

        self.gridLayout_2.addWidget(self.render_thumbs_label, 6, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.leftmenu_top)

        ##### LEFT MENU MID
        self.leftmenu_middle = qw.QFrame(self.menu_icons)
        self.leftmenu_middle.setObjectName(u"leftmenu_middle")
        self.leftmenu_middle.setMinimumSize(qc.QSize(50, 100))
        self.leftmenu_middle.setMaximumSize(qc.QSize(16777215, 100))
        self.leftmenu_middle.setFrameShape(qw.QFrame.NoFrame)
        self.leftmenu_middle.setFrameShadow(qw.QFrame.Raised)

        self.gridLayout_4 = qw.QGridLayout(self.leftmenu_middle)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(15)


        ## APPS
        self.apps_btn = qw.QPushButton(self.leftmenu_middle)
        self.apps_btn.setObjectName(u"apps_btn")
        self.apps_btn.setMinimumSize(qc.QSize(32, 32))
        self.apps_btn.setMaximumSize(qc.QSize(32, 32))
        self.apps_btn.setStyleSheet(u"#apps_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_apps/images/apps.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#apps_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#apps_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "")
        self.apps_btn.setFlat(True)

        self.gridLayout_4.addWidget(self.apps_btn, 0, 0, 1, 1)

        self.apps_label = qw.QLabel(self.leftmenu_middle)
        self.apps_label.setObjectName(u"apps_label")
        self.apps_label.setMinimumSize(qc.QSize(0, 32))
        self.apps_label.setMaximumSize(qc.QSize(16777215, 32))
        self.apps_label.setFont(font2)
        self.apps_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.apps_label.setMargin(0)

        self.gridLayout_4.addWidget(self.apps_label, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.leftmenu_middle)


        ###### LEFT MENU BOTTOM
        self.leftmenu_bottom = qw.QFrame(self.menu_icons)
        self.leftmenu_bottom.setObjectName(u"leftmenu_bottom")
        self.leftmenu_bottom.setMinimumSize(qc.QSize(50, 100))
        self.leftmenu_bottom.setMaximumSize(qc.QSize(16777215, 100))
        self.leftmenu_bottom.setStyleSheet(u"")
        self.leftmenu_bottom.setFrameShape(qw.QFrame.NoFrame)
        self.leftmenu_bottom.setFrameShadow(qw.QFrame.Raised)
        self.gridLayout_3 = qw.QGridLayout(self.leftmenu_bottom)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)


        ## CONFIG BTN
        self.configuration_btn = qw.QPushButton(self.leftmenu_bottom)
        self.configuration_btn.setObjectName(u"configuration_btn")
        self.configuration_btn.setMinimumSize(qc.QSize(32, 32))
        self.configuration_btn.setMaximumSize(qc.QSize(32, 32))
        self.configuration_btn.setStyleSheet(u"#configuration_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_settings/images/settings.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#configuration_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#configuration_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "")
        self.configuration_btn.setFlat(True)

        self.gridLayout_3.addWidget(self.configuration_btn, 0, 0, 1, 1)

        self.configuration_label = qw.QLabel(self.leftmenu_bottom)
        self.configuration_label.setObjectName(u"configuration_label")
        self.configuration_label.setMinimumSize(qc.QSize(0, 32))
        self.configuration_label.setMaximumSize(qc.QSize(16777215, 32))
        self.configuration_label.setFont(font2)
        self.configuration_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.configuration_label.setMargin(0)

        self.gridLayout_3.addWidget(self.configuration_label, 0, 1, 1, 1)


        ## ADMIN PANEL BTN
        self.adminpanel_btn = qw.QPushButton(self.leftmenu_bottom)
        self.adminpanel_btn.setObjectName(u"adminpanel_btn")
        self.adminpanel_btn.setMinimumSize(qc.QSize(32, 32))
        self.adminpanel_btn.setMaximumSize(qc.QSize(32, 32))
        self.adminpanel_btn.setStyleSheet(u"#adminpanel_btn {\n"
        "  border-radius: 5px;\n"
        "  border-image: url(:/icon_adminpanel/images/adminpanel.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#adminpanel_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#adminpanel_btn:pressed {\n"
        "    border-radius: 10px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.adminpanel_btn.setFlat(True)

        self.gridLayout_3.addWidget(self.adminpanel_btn, 1, 0, 1, 1)

        self.adminpanel_label = qw.QLabel(self.leftmenu_bottom)
        self.adminpanel_label.setObjectName(u"adminpanel_label")
        self.adminpanel_label.setMinimumSize(qc.QSize(0, 32))
        self.adminpanel_label.setMaximumSize(qc.QSize(16777215, 32))
        self.adminpanel_label.setFont(font2)
        self.adminpanel_label.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.adminpanel_label.setMargin(0)

        self.gridLayout_3.addWidget(self.adminpanel_label, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.leftmenu_bottom)


        self.horizontalLayout_5.addWidget(self.menu_icons)


        self.horizontalLayout_2.addWidget(self.frame_leftmenu)


## FRAME CONTENT ----------------------------------------------
        self.frame_content = qw.QFrame(self.frame_mid)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.frame_content.setFrameShape(qw.QFrame.NoFrame)
        self.frame_content.setFrameShadow(qw.QFrame.Raised)

        self.gridLayout = qw.QGridLayout(self.frame_content)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 10)

        ## RIGHT FRAME -------------
        self.frame_content_right = qw.QFrame(self.frame_content)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"")
        self.frame_content_right.setFrameShape(qw.QFrame.StyledPanel)
        self.frame_content_right.setFrameShadow(qw.QFrame.Raised)


        ## MAIN STACK FRAME -------------
        self.frame_mainstack = qw.QStackedWidget(self.frame_content)
        self.frame_mainstack.setObjectName(u"frame_mainstack")

        ## PAGE HOME
        self.page_home = qw.QWidget()
        self.page_home.setObjectName(u"page_home")

        ## PAGE ADMIN
        self.page_admin = qw.QWidget()
        self.page_admin.setObjectName(u"page_admin")

        #### ADD WIDGETS TO FRAME MAINSTACK
        self.frame_mainstack.addWidget(self.page_home)
        self.frame_mainstack.addWidget(self.page_admin)


        ## SIGNAL FRAME -------------
        self.frame_signal = qw.QFrame(self.frame_content)
        self.frame_signal.setObjectName(u"frame_signal")
        self.frame_signal.setMinimumSize(qc.QSize(50, 35))
        self.frame_signal.setMaximumSize(qc.QSize(50, 35))
        self.frame_signal.setStyleSheet(u"")
        self.frame_signal.setFrameShape(qw.QFrame.NoFrame)
        self.frame_signal.setFrameShadow(qw.QFrame.Raised)

        self.verticalLayout_2 = qw.QVBoxLayout(self.frame_signal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 15, 0)

        self.signal_btn = qw.QPushButton(self.frame_signal)
        self.signal_btn.setObjectName(u"signal_btn")
        self.signal_btn.setMinimumSize(qc.QSize(30, 30))
        self.signal_btn.setMaximumSize(qc.QSize(35, 35))
        self.signal_btn.setStyleSheet(u"#signal_btn {\n"
        "  border-radius: 8px;\n"
        "  border-image: url(:/icon_signal/images/signal.png) 0 0 0 0 stretch stretch;\n"
        "  background-repeat: no-repeat;  \n"
        "  background-position: center;\n"
        "}\n"
        "\n"
        "#signal_btn:hover {\n"
        "	background-color : rgb(100,100,100);\n"
        "	color: rgb(200,200,200);\n"
        "}\n"
        "\n"
        "#signal_btn:pressed {\n"
        "     border-radius: 16px;\n"
        "	background-color : rgb(85,85,85);\n"
        "	color: rgb(200,200,200);\n"
        "}")
        self.signal_btn.setAutoDefault(False)
        self.signal_btn.setFlat(True)

        #### ADD WIDGETS TO VERTICAL SIGNAL LAYOUT
        self.verticalLayout_2.addWidget(self.signal_btn)
        ## end SIGNAL FRAME -------------

        ## NAVIGATION FRAME -------------
        self.frame_navigation = qw.QFrame(self.frame_content)
        self.frame_navigation.setObjectName(u"frame_navigation")
        self.frame_navigation.setMinimumSize(qc.QSize(0, 20))
        self.frame_navigation.setMaximumSize(qc.QSize(16777215, 20))
        self.frame_navigation.setStyleSheet(u"#frame_navigation {\n"
        "	background-color: rgb(45, 45, 45);\n"
        "}")
        self.frame_navigation.setFrameShape(qw.QFrame.NoFrame)
        self.frame_navigation.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_9 = qw.QHBoxLayout(self.frame_navigation)
        self.horizontalLayout_9.setSpacing(50)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, 0, 0, 0)

        self.nav_err_msg = qw.QLabel(self.frame_navigation)
        self.nav_err_msg.setObjectName(u"nav_err_msg")
        self.nav_err_msg.setMinimumSize(qc.QSize(1, 20))
        self.nav_err_msg.setMaximumSize(qc.QSize(16777215, 20))
        self.nav_err_msg.setStyleSheet(u"#nav_err_msg {\n"
        "	border-radius: 15px;\n"
        "	background-color: rgb();\n"
        # "	font: 9pt \"Bahnschrift\";\n"
        "	color: rgb(202, 63, 149);\n"
        "	padding-bottom:2px;\n"
        "}")
        fonterr = qg.QFont()
        fonterr.setFamily(u"Bahnschrift")
        fonterr.setPointSize(8)
        self.nav_err_msg.setFont(fonterr)
        self.nav_err_msg.setFrameShape(qw.QFrame.NoFrame)
        self.nav_err_msg.setFrameShadow(qw.QFrame.Raised)
        self.nav_err_msg.setAlignment(qc.Qt.AlignCenter)

        self.nav_info = qw.QLabel(self.frame_navigation)
        self.nav_info.setObjectName(u"nav_info")
        self.nav_info.setMinimumSize(qc.QSize(80, 20))
        self.nav_info.setMaximumSize(qc.QSize(150, 20))
        self.nav_info.setStyleSheet(u"#nav_info {\n"
        "	border-top-right-radius: 0px;\n"
        "	border-top-left-radius: 5px;\n"
        "	border-bottom-right-radius: 0px;\n"
        "	border-bottom-left-radius: 5px;\n"
        "	background-color: rgb(30,30,30);\n"
        "	color: rgb(171,171,171);\n"
        "	font: 8pt \"Bahnschrift\";\n"
        "	padding-right:20px;\n"
        "	padding-bottom:2px;\n"
        "}")
        self.nav_info.setFrameShape(qw.QFrame.NoFrame)
        self.nav_info.setTextFormat(qc.Qt.AutoText)
        self.nav_info.setAlignment(qc.Qt.AlignRight|qc.Qt.AlignTrailing|qc.Qt.AlignVCenter)
        self.nav_info.setMargin(0)
        self.nav_info.setIndent(-1)

        #### ADD WIDGETS TO HORIZONTAL NAVIGATION LAYOUT
        self.horizontalLayout_9.addWidget(self.nav_err_msg)
        self.horizontalLayout_9.addWidget(self.nav_info)
        ## end NAVIGATION FRAME -------------

        #### ADD FRAMES TO FRAME CONTENT - GRID
        self.gridLayout.addWidget(self.frame_navigation, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_mainstack, 1, 0, 2, 1)
        self.gridLayout.addWidget(self.frame_content_right, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_signal, 2, 1, 1, 1)

        #### ADD FRAME CONTENT TO FRAME MID
        self.horizontalLayout_2.addWidget(self.frame_content)

        ### ADD FRAME MID TO MAIN VERTICAL LAYOUT ORDER
        self.verticalLayout.addWidget(self.frame_mid)


##---------------------------------------------

        ###### BOTTOM
 
        self.frame_bottom = qw.QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(qc.QSize(20, 20))
        self.frame_bottom.setMaximumSize(qc.QSize(16777215, 20))
        self.frame_bottom.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.frame_bottom.setFrameShape(qw.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(qw.QFrame.Raised)
        self.frame_bottom.setLineWidth(0)
        self.horizontalLayout_10 = qw.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 5, 0)

        ## AUTHOR FRAME
        self.frame_author = qw.QFrame(self.frame_bottom)
        self.frame_author.setObjectName(u"frame_author")
        self.frame_author.setMaximumSize(qc.QSize(300, 16777215))
        self.frame_author.setStyleSheet(u"")
        self.frame_author.setFrameShape(qw.QFrame.NoFrame)
        self.frame_author.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_4 = qw.QHBoxLayout(self.frame_author)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 0, 15, 0)

        ## LABEL AUTHOR
        self.label_author = qw.QLabel(self.frame_author)
        self.label_author.setObjectName(u"label_author")
        font3 = qg.QFont()
        font3.setFamily(u"Bahnschrift")
        font3.setPointSize(8)
        self.label_author.setFont(font3)
        self.label_author.setAutoFillBackground(False)
        self.label_author.setStyleSheet(u"color: rgb(171, 171, 171);\n"
        "padding-bottom:2px;")
        self.label_author.setScaledContents(False)
        self.label_author.setAlignment(qc.Qt.AlignLeading|qc.Qt.AlignLeft|qc.Qt.AlignVCenter)
        self.label_author.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.label_author)
        ## END AUTHOR FRAME


        ## INFO FRAME
        self.frame_info = qw.QFrame(self.frame_bottom)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(qc.QSize(0, 20))
        self.frame_info.setMaximumSize(qc.QSize(16777215, 20))
        self.frame_info.setStyleSheet(u"")
        self.frame_info.setFrameShape(qw.QFrame.NoFrame)
        self.frame_info.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_11 = qw.QHBoxLayout(self.frame_info)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(15, 0, 0, 0)
        self.horizontalSpacer_3 = qw.QSpacerItem(40, 20, qw.QSizePolicy.Expanding, qw.QSizePolicy.Minimum)


        ## INFO BUTTON
        self.info_btn = qw.QLabel(self.frame_info)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setToolTip("Updates info")
        self.info_btn.setMinimumSize(qc.QSize(16, 16))
        self.info_btn.setMaximumSize(qc.QSize(20, 16))
        font4 = qg.QFont()
        font4.setFamily(u"Arial")
        self.info_btn.setFont(font4)
        self.info_btn.setStyleSheet(u"""
        #info_btn { text-weight:75 }
        """)

        self.info_btn.setAlignment(qc.Qt.AlignRight|qc.Qt.AlignTrailing|qc.Qt.AlignVCenter)

        ## REFRESH BUTTON 
        self.refresh_btn = qw.QPushButton(self.frame_info)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setToolTip("Reset")
        self.refresh_btn.setMinimumSize(qc.QSize(17, 17))
        self.refresh_btn.setMaximumSize(qc.QSize(17, 17))

        ## UPDATE BUTTON 
        self.update_btn = qw.QPushButton(self.frame_info)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setToolTip("Update")
        self.update_btn.setMinimumSize(qc.QSize(16, 16))
        self.update_btn.setMaximumSize(qc.QSize(16, 16))

        ## ADD WIDGETS TO FRAME INFO HORZIONTAL LAYOUT ORDER
        self.horizontalLayout_11.addWidget(self.refresh_btn)
        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)
        self.horizontalLayout_11.addWidget(self.update_btn)
        self.horizontalLayout_11.addWidget(self.info_btn)
        ## => END INFO FRAME

        ## VERSION FRAME
        self.frame_version = qw.QFrame(self.frame_bottom)
        self.frame_version.setObjectName(u"frame_version")
        self.frame_version.setMaximumSize(qc.QSize(120, 16777215))
        self.frame_version.setStyleSheet(u"")
        self.frame_version.setFrameShape(qw.QFrame.NoFrame)
        self.frame_version.setFrameShadow(qw.QFrame.Raised)
        self.horizontalLayout_8 = qw.QHBoxLayout(self.frame_version)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, 0, 15, 0)
        self.label_version = qw.QLabel(self.frame_version)
        self.label_version.setObjectName(u"label_version")
        font5 = qg.QFont()
        font5.setFamily(u"Bahnschrift")
        font5.setPointSize(9)
        self.label_version.setFont(font5)
        self.label_version.setAutoFillBackground(False)
        self.label_version.setStyleSheet(u"color: rgb(171, 171, 171);\n"
        "padding-bottom:2px;")
        self.label_version.setScaledContents(False)
        self.label_version.setAlignment(qc.Qt.AlignCenter)
        self.label_version.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label_version)
        ## => END VERSION FRAME

        ## FRAME GRIP
        self.frame_grip_size = qw.QFrame(self.frame_bottom)
        self.frame_grip_size.setObjectName(u"frame_grip_size")
        self.frame_grip_size.setMinimumSize(qc.QSize(12, 12))
        self.frame_grip_size.setMaximumSize(qc.QSize(12, 12))
        self.frame_grip_size.setFrameShape(qw.QFrame.NoFrame)
        self.frame_grip_size.setFrameShadow(qw.QFrame.Raised)
        ## => END FRAME GRIP


        ## ADD FRAMES TO BOTTOM FRAME LAYOUT
        self.horizontalLayout_10.addWidget(self.frame_author)
        self.horizontalLayout_10.addWidget(self.frame_info)
        self.horizontalLayout_10.addWidget(self.frame_version)
        self.horizontalLayout_10.addWidget(self.frame_grip_size)


        self.verticalLayout.addWidget(self.frame_bottom)
        ## => END BOTTOM FRAME

        ## MAIN
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sandwitch_btn.setDefault(False)
        self.frame_mainstack.setCurrentIndex(0)
        self.signal_btn.setDefault(False)


        qc.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", u"FAVA", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(_translate("MainWindow", u"FAVA", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.sandwitch_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>MENU</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sandwitch_btn.setText("")
        # self.fava_logo.setText("")
        self.minimize.setText(_translate("MainWindow", u"\u2584", None))
        self.maximize.setText("")
        self.exit.setText(_translate("MainWindow", u"X", None))
        self.createfolder_btn.setText("")
        self.createfolder_label.setText(_translate("MainWindow", u"CREATE FOLDER", None))
#if QT_CONFIG(tooltip)
        self.importer_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>Importer</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.importer_btn.setText("")
        self.importer_label.setText(_translate("MainWindow", u"IMPORTER", None))
#if QT_CONFIG(accessibility)
        self.shell_btn.setAccessibleName(_translate("MainWindow", u"shell_btn", None))
#endif // QT_CONFIG(accessibility)
        self.shell_btn.setText("")
        self.shell_label.setText(_translate("MainWindow", u"SHELL", None))
#if QT_CONFIG(tooltip)
        self.exporter_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>Exporter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exporter_btn.setText("")
        self.exporter_label.setText(_translate("MainWindow", u"EXPORTER", None))
        self.uvprinter_btn.setText("")
        self.uvprinter_label.setText(_translate("MainWindow", u"UV PRINTER", None))
        self.materials_btn.setText("")
        self.materials_label.setText(_translate("MainWindow", u"MATERIALS", None))
        self.render_thumbs_btn.setText("")
        self.render_thumbs_label.setText(_translate("MainWindow", u"RENDER THUMBS", None))
#if QT_CONFIG(accessibility)
        self.apps_btn.setAccessibleName(_translate("MainWindow", u"apps_btn", None))
#endif // QT_CONFIG(accessibility)
        self.apps_btn.setText("")
#if QT_CONFIG(accessibility)
        self.apps_label.setAccessibleName(_translate("MainWindow", u"apps_label", None))
#endif // QT_CONFIG(accessibility)
        self.apps_label.setText(_translate("MainWindow", u"APPS ", None))
#if QT_CONFIG(tooltip)
        self.configuration_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>Configuration</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.configuration_btn.setAccessibleName(_translate("MainWindow", u"configuration_btn", None))
#endif // QT_CONFIG(accessibility)
        self.configuration_btn.setText("")
#if QT_CONFIG(accessibility)
        self.configuration_label.setAccessibleName(_translate("MainWindow", u"apps_label", None))
#endif // QT_CONFIG(accessibility)
        self.configuration_label.setText(_translate("MainWindow", u"CONFIG", None))
#if QT_CONFIG(tooltip)
        self.adminpanel_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>Admin panel</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.adminpanel_btn.setAccessibleName(_translate("MainWindow", u"adminpanel_btn", None))
#endif // QT_CONFIG(accessibility)
        self.adminpanel_btn.setText("")
#if QT_CONFIG(accessibility)
        self.adminpanel_label.setAccessibleName(_translate("MainWindow", u"apps_label", None))
#endif // QT_CONFIG(accessibility)
        self.adminpanel_label.setText(_translate("MainWindow", u"ADMIN PANEL", None))
#if QT_CONFIG(tooltip)
        self.signal_btn.setToolTip(_translate("MainWindow", u"<html><head/><body><p>errors, bugs here !</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.signal_btn.setAccessibleName(_translate("MainWindow", u"signal_btn", None))
#endif // QT_CONFIG(accessibility)
        self.signal_btn.setText("")

#if QT_CONFIG(accessibility)
        self.nav_err_msg.setAccessibleName(_translate("MainWindow", u"nav_msg", None))
#endif // QT_CONFIG(accessibility)
        self.nav_err_msg.setText(_translate("MainWindow", u"ERROR !", None))
#if QT_CONFIG(accessibility)
        self.nav_info.setAccessibleName(_translate("MainWindow", u"nav_info", None))
#endif // QT_CONFIG(accessibility)
        self.nav_info.setText(_translate("MainWindow", u"/ HOME", None))


        self.label_author.setText(_translate("MainWindow", u"author: riffraff  |  FOLDERS AND VIRTUAL ASSETS", None))
        self.info_btn.setText(_translate("MainWindow", u"i", None))
        self.label_version.setText(_translate("MainWindow", u"version: r.2.0.1.b", None))
    # retranslateUi

