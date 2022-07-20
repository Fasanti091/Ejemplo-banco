class Persona:
    def __init__(self, nombre: str, apellido: str, documento: int, saldo: float) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.__saldo = saldo
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} || Apellido: {self.apellido} || Documento: {self.documento}"
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def realizar_pago(self, monto: float):
        self.__saldo -= monto
    
    def realizar_deposito(self, monto: float):
        self.__saldo += monto

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
