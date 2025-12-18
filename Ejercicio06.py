from geometria import Rectangulo, Triangulo, Circulo

figuras = [
    Rectangulo(4, 6),
    Triangulo(3, 4, 5, 4, 3),
    Circulo(2.5)
]

for figura in figuras:
    figura.mostrar_datos()
