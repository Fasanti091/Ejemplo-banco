class Perosna:
    pass

class Banco:
    def __init__(self, nombre: str, direccion: str) -> None:
        self.clientes = []
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self) -> str:
        return f"Banco {self.nombre} || Direccion: {self.direccion}"
    
    def agregar_cliente(self, persona: Persona):
        self.clientes.append(persona)
    
    def concultar_ceunta_cliente(self, documento: str) -> Persona:
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente