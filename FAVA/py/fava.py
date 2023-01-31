
# IMPORT PYSIDE2 MODULES
import fava_import_modules as modules

# IMPORT GUI
from fava_ui import UI_Fava

# IMPORT VARIABLES
import fava_variables_ as gc

# IMPORT UI FUNCTIONS
from fava_ui_functions import *

import PySide2.QtWidgets as qw
import PySide2.QtGui as qg
import PySide2.QtCore as qc

class MainWindow(qw.QMainWindow, UI_Fava): 

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.GLOBAL_POS = qc.QPoint(0, 0)
        self.keyCombination = ""
        self.setMouseTracking(1)
        self.pageName = ""
        self.currentSize = None
        self.test = "test"
        
        ## SET UP UI MAIN WINDOW
        self.setupUi(self)

        ## functions
        self.funcs()

        # ## UPDATE UI DEFS
        self.update_ui_services()

        ## UPDATE UI
        self.update_ui()

        ## CONNECTIONS
        self.connectButtonsToMethods()

        ## SHOW MAIN WINDOW
        self.show()

    def connectButtonsToMethods(self):
        ## EXPAND MENU
        self.sandwitch_btn.clicked.connect(lambda: UI_Functions.menu_expand(self,True))

        ## MINIMIZE WINDOW
        self.minimize.clicked.connect(lambda: UI_Functions.minimizeWin(self))

        ## MAXIMIZE WINDOW
        self.maximize.clicked.connect(lambda: UI_Functions.maximizeWin(self))

        ## CLOSE WINDOW
        self.exit.clicked.connect(lambda: UI_Functions.closeWin(self))

        ## RESET FULL WINDOW
        self.refresh_btn.clicked.connect(lambda: UI_Functions.refreshProgram(self, True))

        ## UPDATE PROGRAM CODE
        self.update_btn.clicked.connect(lambda: UI_Functions.updateProgram(self,True))

    def funcs(self):

        ## EXPAND INFO
        UI_Functions.lastUpdateInfo(self, True)

        UI_Functions.changeNavigationText(self, "HOME")
        
  
    def update_ui(self):

        ## MAIN WINDOW ICON
        UI_Functions.setIcon(self, True)

        ## ADD FONTS
        UI_Functions.addTheFonts(self, True)

        ## BEAUTIFYING THE WINDOW
        UI_Functions.uiBeautify(self)


  
    def update_ui_services(self):

        ## REMOVE WINDOW TITLE BAR AND SET CUSTOM ONE
        UI_Functions.removeTitleBar(self, True)       

        ## MOVE WINDOW
        UI_Functions.moveWin(self)

        ## RESIZE WIN
        UI_Functions.resizeWin(self, True)

        ## DOUBLE CLICK TO MAXIMIZE AND RESTORE
        UI_Functions.doubleClickMaximizeRestore(self)


    ## MOUSE PRESS AND GET GLOBAL POSITION OF THE EVENT
    def mousePressEvent(self, event):
        self.GLOBAL_POS = event.globalPos()

        if event.buttons() == qc.Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == qc.Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == qc.Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
        
    

    ## CLOSE WINDOW WITH SHORTCUT COMBINATION (1+Escape)
    def keyReleaseEvent(self, event):

        key1 = qc.Qt.Key_Escape
        key2 = qc.Qt.Key_1
        key1txt = "esc"
        key2txt = "1"

        ## add key 1
        if event.key() == key1:
            self.keyCombination += key1txt
            print(self.keyCombination)

        ## add key 2
        elif event.key() == key2:
            self.keyCombination += key2txt
            print(self.keyCombination)

        kC = self.keyCombination
        combination1 = key1txt + key2txt
        combination2 = key2txt + key1txt

        ## clear if input is not ok
        if kC not in (key2txt, key1txt, combination1, combination2):
            self.keyCombination = ""

        ## close if input is ok
        if kC in (combination1, combination2):
            self.close()

    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    ## GET WINDOW CURRENT SIZE
    def getSize(self):
        winsize = [self.width(), self.height()]
        return winsize


def main():
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication(modules.sys.argv)

    mainWin = MainWindow()
    # mainWin.core()
    
    ## LOAD QSS FILE
    UI_Functions.loadStylesheetFile(mainWin, app)

    UI_Functions.loadResourceFile(mainWin)

    app.exec_()

if __name__ == "__main__":
    main()
