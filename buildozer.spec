[app]

title = PC Bridge App
package.name = pcbridge
package.domain = org.pcbridge

source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy,pyjnius

android.permissions = CALL_PHONE,READ_SMS,RECEIVE_SMS,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

# Recommended
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1
