# IMPORT MODULES
from fava import MainWindow, modules, qc, qw, qg, gc

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = False

class UI_Functions(MainWindow):

    isEnabled = ""
    isInfoExpanded = ""
    infobutton = ""
    infotext = ""
    date = ""
    pageName = ""

    # def __init__(self):
    #     (MainWindow).__init__(self)


    ## SET FONT
    def addTheFonts(self, status):
        if status:
            qg.QFontDatabase.addApplicationFont(":/fonts/bahnschrift.ttf")
            qg.QFontDatabase.addApplicationFont(":/fonts/arial.ttf")
            qg.QFontDatabase.addApplicationFont(":/fonts/arialbd.ttf")

    ## SET ICON TO WINDOW
    def setIcon(self, isShow):
        if isShow: 
            icon = qg.QIcon()
            icon.addFile(":/fava_logo/images/icon.png", qc.QSize(), qg.QIcon.Normal, qg.QIcon.Off)
            self.setWindowIcon(icon)

    ##  RETURN STATUS
    def returnStatus(self):
        return GLOBAL_STATE

    ## EXPAND MENU
    def menu_expand(self, enable):
        
        # EXPAND MENU IF ENABLED
        if enable:

            #GET MENU FRAME
            menu = self.frame_leftmenu
            menuMinWidthProperty = b"minimumWidth"

            #GET WIDTH
            menuW = menu.width()


            #SET TARGET WIDTH 
            if menuW == gc.notExpanded:
                targetWidth = gc.expanded
            else:
                targetWidth = gc.notExpanded

            #ANIMATION
            menu.animation = qc.QPropertyAnimation(menu, menuMinWidthProperty)
            menu.animation.setDuration(400)
            menu.animation.setStartValue(menuW)
            menu.animation.setEndValue(targetWidth)
            menu.animation.setEasingCurve(qc.QEasingCurve.InOutQuart)
            menu.animation.start()
    
    ## INFO EXPAND
    def lastUpdateInfo(self, enable):

        self.isEnabled = enable
        btnMinWidth = b"minimumWidth"

        def infoEvent(event):

            if event.buttons() == qc.Qt.LeftButton and self.isEnabled and self.info_btn.width() <= 20:

                ## CHANGE STYLE
                self.info_btn.setStyleSheet(u"""#info_btn { background-color: rgb(43, 39, 70); border-color: rgb(51, 46, 84); padding-right:15px; padding-bottom:2px;}""") 
                fontinfo = qg.QFont()
                fontinfo.setFamily(u"Bahnschrift")
                fontinfo.setPointSize(8)
                self.info_btn.setFont(fontinfo)

                ## GET LAST UPDATE DATE AND SET TEXT
                #TODO
                self.date = "24.02.2021"
                self.infotext = gc.last_update_message.format(self.date, self.date)
                self.info_btn.setText(self.infotext.format(self.date))

                ## ANIMATION OF THE BUTTON
                self.info_btn.animation = qc.QPropertyAnimation(self.info_btn, btnMinWidth)
                self.info_btn.animation.setDuration(150)
                self.info_btn.animation.setStartValue(0)
                self.info_btn.animation.setEndValue(((len(self.infotext))/10)*55)
                self.info_btn.animation.setEasingCurve(qc.QEasingCurve.InOutQuart)
                self.info_btn.animation.start()
            else:
                ## ANIMATION OF THE BUTTON
                self.info_btn.animation = qc.QPropertyAnimation(self.info_btn, btnMinWidth)
                self.info_btn.animation.setDuration(150)
                self.info_btn.animation.setStartValue(((len(self.infotext))/10)*55)
                self.info_btn.animation.setEndValue(16)
                self.info_btn.animation.setEasingCurve(qc.QEasingCurve.InOutQuart)
                self.info_btn.animation.start()

                ## CHANGE STYLE
                self.info_btn.setStyleSheet(u"""#info_btn {
                    border:1px solid rgb(150,150,150);
                    border-radius: 5px;
                    color: rgb(200, 200, 200);
                    padding-right:3px;
                }

                #info_btn:hover {
                    border: 1px solid rgb(255,255,255);
                    border-radius: 5px;
                    color: rgb(255, 255, 255);
                }""") 
                fontinfo = qg.QFont()
                fontinfo.setFamily(u"Arial")
                self.info_btn.setFont(fontinfo)
                self.info_btn.setFixedSize(qc.QSize(16, 16))

                ## SET TEXT
                self.infotext = "i"
                self.info_btn.setText(self.infotext)


        self.info_btn.mousePressEvent = infoEvent

    ## UPDATE PROGRAM
    def refreshProgram(self, isRefreshable):
    ##TODO: refresh
        if isRefreshable:
            print("Program fava is refreshed!")   

    ## UPDATE PROGRAM
    def updateProgram(self, isUpdateable):
    ##TODO: update
        if isUpdateable:
            print("Program fava is updated!")     

    ## MOVE WINDOW
    def moveWin(self):
        ## MOVE WINDOW
        def moveWin(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UI_Functions.returnStatus(self) == 1:
                UI_Functions.maximizeWin(self)

            # MOVE WINDOW
            if event.buttons() == qc.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.GLOBAL_POS)
                self.GLOBAL_POS = event.globalPos()
                event.accept()
            
        # WIDGET TO MOVE
        self.frame_logo.mouseMoveEvent = moveWin

    ## MINIMIZE
    def minimizeWin(self):
        self.showMinimized()
        self.minimize.setToolTip("Minimize")
        print("Minimize window")

    ## MAXIMIZE
    def maximizeWin(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.maximize.setToolTip("Restore")
            print("Window Maximized")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.maximize.setToolTip("Maximize")
            print("Window Restored")

    ## MAXIMIZE DOUBLE CLICK
    def doubleClickMaximizeRestore(self):

        ## DOUBLE CLICK ON TOP BAR - MAXIMIZE AND RESTORE
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == qc.QEvent.MouseButtonDblClick:
                qc.QTimer.singleShot(150, lambda: UI_Functions.maximizeWin(self))

        if GLOBAL_TITLE_BAR:
            self.frame_logo.mouseDoubleClickEvent = doubleClickMaximizeRestore

    ## CLOSE WINDOW
    def closeWin(self):
        self.exit.setToolTip("Close FAVA")
        print("Close window")
        self.close()

    ## RESIZE WINDOW
    def resizeWin(self, isResizeable):

        self.currentSize = self.getSize()
        print(gc.basesize.format(self.currentSize[1], self.currentSize[0]))

        def resizeWinEvent(event):
            if event.type() == qc.QEvent.MouseButtonRelease:
                resized = self.getSize()
                print(gc.resize.format(resized[1], resized[0]))
                
        if isResizeable:
            sizegrip = qw.QSizeGrip(self.frame_grip_size)
            sizegrip.setStyleSheet("border-image: url(:/icon_grip/images/cil-size-grip.png) 0 0 0 0 stretch stretch;")
            sizegrip.mouseReleaseEvent = resizeWinEvent

    ## REMOVE TITLE BAR
    def removeTitleBar(self, status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(qc.Qt.FramelessWindowHint)
            self.setAttribute(qc.Qt.WA_TranslucentBackground)

    ## BEAUTIFY
    def uiBeautify(self):        
        ## SHOW DROP SHADOW
        shadow = qw.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(17)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(qg.QColor(0, 0, 0, 150))
        self.frame_bottom.setGraphicsEffect(shadow)

    ## LOAD STYLES
    def loadStylesheetFile(self, app):
        # ## LOAD QSS FILE
        qssfile = qc.QFile(gc.qssFava)

        if not qssfile.open(qc.QFile.ReadOnly | qc.QFile.Text):
            return
        
        qss = qc.QTextStream(qssfile)

        app.setStyleSheet(qss.readAll())

    ## LOAD RESOURCE FILE
    def loadResourceFile(self):
        pass
        
    ## CHANGE NAVIGATION TEXT
    def changeNavigationText(self, page_name):
        print(UI_Functions.getNavigationText(self))

        divider = "/"
        pageName = "{0} {1}".format(divider, page_name)
        self.nav_info.setText(pageName)

    ## GET NAV TEXT
    def getNavigationText(self):
        currentNavInfo = self.nav_info.text()
        return currentNavInfo

    

    

        
    
