class Libro:
    def __init__(self, titulo, autor, año, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = disponibilidad

    def prestar (self):
        if (self.disponibilidad == True):
            self.disponibilidad = False
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"'{self.titulo}' no está disponible.")
    
    def devolver(self):
        self.disponible = True
        print(f"'{self.titulo}' ha sido devuelto.")

    def __str__(self):
        estado = "Disponible" if self.disponibilidad else "Prestado"
        return f"{self.titulo} | {self.autor} ({self.año}) - {estado}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, disponibilidad, formato, tamanoMB):
        super().__init__(titulo, autor, año, disponibilidad)
        self.formato = formato
        self.tamanoMB = tamanoMB

    def prestar(self):
        print(f"'{self.titulo}' es digital y siempre está disponible.")

    def __str__(self):
        return (f"{self.titulo} | {self.autor} ({self.año}) - "
                f"Digital [{self.formato}, {self.tamanoMB}MB]")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def listar_libros(self):
        print("\nLISTA DE LIBROS")
        for libro in self.libros:
            print(libro)

    def buscar_por_autor(self, autor):
        print(f"\nLibros de {autor}:")
        encontrados = False
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                print(libro)
                encontrados = True
        if not encontrados:
            print("No se encontraron libros de ese autor.")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print("Libro no encontrado.")

biblioteca = Biblioteca()
l1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)
l2 = Libro("La ciudad y los perros", "Mario Vargas Llosa", 1963, True)
l3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True)
d1 = LibroDigital("Python para todos", "Charles Severance", 2016, True, "PDF", 5)
d2 = LibroDigital("Clean Code", "Robert C. Martin", 2008, True, "EPUB", 3)
biblioteca.agregar_libro(l1)
biblioteca.agregar_libro(l2)
biblioteca.agregar_libro(l3)
biblioteca.agregar_libro(d1)
biblioteca.agregar_libro(d2)
biblioteca.listar_libros()
biblioteca.prestar_libro("Cien años de soledad")
for _ in range(5):
    biblioteca.prestar_libro("Python para todos")
biblioteca.prestar_libro("Cien años de soledad")
biblioteca.buscar_por_autor("Mario Vargas Llosa")
