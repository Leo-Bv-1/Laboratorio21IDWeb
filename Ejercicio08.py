import json

equipos = [
    {
        "nombre": "Barcelona",
        "pais": "España",
        "nivelAtaque": 95,
        "nivelDefensa": 80
    },
    {
        "nombre": "Bayern Munich",
        "pais": "Alemania",
        "nivelAtaque": 90,
        "nivelDefensa": 85
    },
    {
        "nombre": "Manchester City",
        "pais": "Inglaterra",
        "nivelAtaque": 88,
        "nivelDefensa": 84
    }
]

json_equipos = json.dumps(equipos, indent=4, ensure_ascii=False)
print(json_equipos)
