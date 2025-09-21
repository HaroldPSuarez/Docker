import socket

class SocketServer:
    """Servidor TCP básico que escucha clientes."""

    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"[SocketServer] Escuchando en {self.host}:{self.port}")

    def accept_connection(self):
        """Espera y acepta una conexión entrante."""
        conn, addr = self.server_socket.accept()
        print(f"[SocketServer] Conexión desde {addr}")
        return conn, addr

    def close(self):
        """Cierra el servidor."""
        print("[SocketServer] Cerrando servidor")
        self.server_socket.close()
