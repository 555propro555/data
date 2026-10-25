[app]

# (str) Title of your application
title = PC Bridge App

# (str) Package name
package.name = pcbridge

# (str) Package domain (needed for android packaging)
package.domain = org.pcbridge

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,pyjnius

# (list) Permissions
# Essential for your app's Bluetooth, SMS, and Call features
android.permissions = CALL_PHONE, READ_SMS, RECEIVE_SMS, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Supported API target
android.api = 33

# (string) Minimum API your APK will support
android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
