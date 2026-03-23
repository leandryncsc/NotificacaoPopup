import time
from plyer import notification
import os

def lembrete():

    icon_path = "cafe.ico"
    
    if not os.path.exists(icon_path):
        icon_path = None
    
    notification.notify(
        title="Fala Leandrão, chegou o grande momento!",
        message="Hora de tomar seu café! ☕",
        timeout=10,
        app_icon=icon_path  
        )

while True:
    lembrete()
    time.sleep(30)  