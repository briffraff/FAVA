import bpy

blenderRunFilePath = r"C:\Users\riffraff\Dropbox\Scripting\Blender\test.py"
blenderRunFileName = "test"
enable = "enable"
disable = "disable"
install = "install"
remove = "remove"
refresh = "refresh"

def enable_disable_Addon(status):
    
    if status == enable:
        ## ENABLE INSTALLED ADDON
        bpy.ops.preferences.addon_enable(module=blenderRunFileName)
    elif status == disable:
        ## DISABLE INSTALLED ADDON
        bpy.ops.preferences.addon_disable(module=blenderRunFileName)


def install_remove_Addon(status):
    if status == install:
        bpy.ops.preferences.addon_install(overwrite=True,filepath=blenderRunFilePath,filter_folder=True,filter_glob="*.py")
    elif status == remove:
        
        enable_disable_Addon(disable)
        enable = disable
        bpy.ops.preferences.addon_remove(module=blenderRunFileName)


def refresh_Addon(status):
    if status == refresh:
        bpy.ops.preferences.addon_refresh()



