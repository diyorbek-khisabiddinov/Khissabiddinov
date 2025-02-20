

    
import json
with open("/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB04/JSON/sample-data.json", "r") as f:
    data = json.load(f)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    descr = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    print(f"{dn:50} {descr:3} {speed:7} {mtu}")


#     Метод	    |       Описание	           |     Входной аргумент	 |      Пример использования         |
# --------------|------------------------------|-------------------------|-----------------------------------|
#  json.load(f) | Загружает JSON из файла	   |    Файловый объект	     |         json.load(f)              |
# json.loads(s) |	Загружает JSON из строки   |       Строка JSON	     |  json.loads('{"name": "Alice"}')  |