import socket
import json

class SocketCliente:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        self.sock.connect((self.host, self.port))
        print(f"✅ Conectado al servidor en {self.host}:{self.port}")

    def enviar(self, data):
        mensaje = json.dumps(data).encode("utf-8")
        self.sock.sendall(mensaje)

    def recibir(self):
        data = self.sock.recv(1024).decode("utf-8")
        if data:
            return json.loads(data)
        return None

    def cerrar(self):
        self.sock.close()
