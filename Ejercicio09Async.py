import random
import asyncio

async def consulta_db_async(nombre):
    tiempo = random.randint(1, 5)
    print(f"{nombre} inició (tarda {tiempo}s)")
    await asyncio.sleep(tiempo)
    print(f"{nombre} terminó")

async def usaAsincronia():
    inicio = asyncio.get_event_loop().time()

    print("Consulta a base de datos usando Asincronia.")

    tareas = [
        consulta_db_async("Consulta 1"),
        consulta_db_async("Consulta 2"),
        consulta_db_async("Consulta 3")
    ]

    await asyncio.gather(*tareas)

    fin = asyncio.get_event_loop().time()
    print(f"Tiempo total con async: {fin - inicio:.2f}s\n")

asyncio.run(usaAsincronia())
