import math

class Figura:
    contador_id = 1

    def __init__(self):
        self.id = Figura.contador_id
        Figura.contador_id += 1

    def area(self):
        return "Area de figura."

    def perimetro(self):
        return "Perimetro de figura."

    def mostrar_datos(self):
        print(f"ID: {self.id}")
        print(f"Figura: {self.__class__.__name__}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")
        print("-" * 30)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, base, altura):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    