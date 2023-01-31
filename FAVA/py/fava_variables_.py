import os

#### LOGGED USER PATH
# logged_user = (os.getlogin()) ## automatic

logged_user = "borko"
logged_user_path = (os.path.expanduser(f"{'~'}{logged_user}"))

########### FAVA

##### ADMIN PANEL

# Paths
qssFilePath = logged_user_path + r"\Dropbox\Scripting\maxscript\Construction\files"
qssFavaFilePath = logged_user_path + r"\Dropbox\Scripting\Blender\FAVA\cssqss"
qrcFavaFilePath = logged_user_path + r"\Dropbox\Scripting\Blender\FAVA"
licPath = logged_user_path + r"\Dropbox\Scripting\maxscript\4_Final stage\Config\lic"
modulesPath = logged_user_path + r"\Dropbox\Scripting\maxscript\4_Final stage\Config\modules"

tempFavaFolder = r"C:\Users\Public\Documents\fStructX" #not used
qssFileName = "adminPanelStylesheet.qss"
qssFavaFileName = "qssFava.qss"
qrcFavaFile = "resource_.qrc"
logName = r"log.txt" #not used
licName = r"Licenses.ini"

logFile = os.path.join(tempFavaFolder, logName) #not used
licenseFile = os.path.join(licPath, licName)
qssFile = os.path.join(qssFilePath, qssFileName)
qssFava = os.path.join(qssFavaFilePath, qssFavaFileName)
qrcFava = os.path.join(qrcFavaFilePath, qrcFavaFile)

# Text
removeBtnText = "Remove"
licenseOnText = "ON"
licenseOffText = "OFF"
updateBtnText = "Update"
activateAllText = "+"
removeAllText = "-"
usersCountText = '=> USERS :'

# License true/false
true = "true"
false = "false"

# Roles
roles = {
    "o":"owner",
    "a":"admin",
    "u":"user",
}

# Header columns
columns = ["Id", "Name", "Account", "Role", "Register to", "License", "Delete user"]

# Sections
domainSection = 'DOMAIN'
domainName = ''
ownerSection = 'OWNER'
ownerName = 'riffraff'

# Options
keyName = "__name__"
keyRole = "__role__"
keyLic = "__lic__"
keyReg = "__reg__"
keyAccount = "__account__"
keyId = "__id__"

# ints
pauseFor = 2500
# usersCount = 4

# Messages
deleteUserMsg = 'Are you sure you want to delete this user ? \n\t         [  {0}  ]'
licenseOnOffMsg = 'Are you sure you want to turn [ {0} ]  [ {1} ]  license ?'
removeAllUsersMsg = 'Are you sure you want to remove ALL users ?'
licenseOnOffAllUsersMsg = 'Are you sure you want to set all license [ {0} ] ?'
usersCountMsg = '{0}'
basesize = "Base size/-   Height: {0} | Width: {1}"
resize = "Re-size/-   Height: {0} | Width: {1}"

##### UI FUNCTIONS 

# MENU
expanded = 200
notExpanded = 65

createFolderName = "Create Folder"
importerName = "Importer"
exporterName = "Exporter"
shellName = "Shell"
renderThumbsName = "Render Thumbs"
applicationsName = "Apps"
configurationName = "Config"
adminName = "Admin panel"

# STATUS BAR
last_update_message = "last update : {0} - local update on: {1}"
