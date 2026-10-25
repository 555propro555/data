[app]

title = PC Bridge App
package.name = pcbridge
package.domain = org.pcbridge

# ADD THIS
source.dir = .

# ADD THIS
version = 1.0

source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy,pyjnius

android.permissions = CALL_PHONE,READ_SMS,RECEIVE_SMS,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
