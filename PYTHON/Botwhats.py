import pywhatkit
from datetime import datetime
import time

seconds = time.time() + 60
date = datetime.fromtimestamp(seconds)
pywhatkit.sendwhatmsg('+34xxxxxx', 'Hola', date.hour, date.minute)


time.sleep(5)


