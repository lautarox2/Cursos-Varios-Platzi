from datetime import datetime
import pytz

bogota_time = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_time)

print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M"))
