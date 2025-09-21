import random
from model.SocketCliente import SocketCliente
from view.ConsoleView import ConsoleView

class ClientController:
    def __init__(self):
        self.socket = SocketCliente()
        self.numeros = []

    def iniciar(self):
        # Conectarse al servidor
        self.socket.conectar()

        # Registrarse en el servidor
        self.socket.enviar({"accion": "registrar", "cliente": "Cliente1"})
        respuesta = self.socket.recibir()
        if respuesta:
            self.numeros = respuesta.get("numeros", [])
            ConsoleView.mostrar_mensaje("Registro exitoso en el servidor")
            ConsoleView.mostrar_numeros(self.numeros)

        # Ejemplo: pedir un número aleatorio que me falte
        faltantes = [n for n in range(11) if n not in self.numeros]
        if faltantes:
            num = random.choice(faltantes)
            self.socket.enviar({"accion": "solicitar", "numero": num, "cliente": "Cliente1"})
            ConsoleView.mostrar_mensaje(f"Solicitando el número {num}")

    def cerrar(self):
        self.socket.cerrar()
