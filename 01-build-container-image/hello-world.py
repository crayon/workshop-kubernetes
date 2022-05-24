import os
from datetime import datetime

name = os.environ.get("HELLO_USER")
current_time = datetime.utcnow().strftime("%H:%M:%S %d.%m.%y")
print(f"Hello {name}, current time is {current_time}")
