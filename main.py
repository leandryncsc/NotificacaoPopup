import time
from winotify import Notification
import os

def lembrete():

    icon_path = "cafe.ico"
    
    kwargs = {
        "app_id": "Notificacao",
        "title": "Fala Leandrão, chegou o grande momento!",
        "msg": "Hora de tomar seu café! ☕",
        "duration": "short"
    }

    if os.path.exists(icon_path):
        kwargs["icon"] = os.path.abspath(icon_path)
    
    toast = Notification(**kwargs)
    toast.show()

while True:
    lembrete()
    time.sleep(30)