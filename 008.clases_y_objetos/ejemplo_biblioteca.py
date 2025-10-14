class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0  # Inicializamos en la página 0 (cerrado)

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"Libro 1: {libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"Libro 2: {libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")