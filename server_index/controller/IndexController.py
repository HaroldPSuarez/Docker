import json
from model.SocketServer import SocketServer
from model.NodeRegistry import NodeRegistry
from view.ConsoleView import ConsoleView

class IndexController:
    """Controlador principal del indexador."""

    def __init__(self, host='localhost', port=5000):
        self.server = SocketServer(host, port)
        self.registry = NodeRegistry()

    def start(self):
        """Inicia el loop del servidor para aceptar y registrar clientes."""
        ConsoleView.show_message("Servidor indexador en ejecución...")

        try:
            while True:
                conn, addr = self.server.accept_connection()

                try:
                    # Recibir nombre del cliente
                    raw = conn.recv(1024)
                    if not raw:
                        conn.close()
                        continue

                    client_name = raw.decode('utf-8').strip()
                    ConsoleView.show_message(f"Cliente conectado: {client_name}")

                    # Registrar cliente y asignar números
                    numbers = self.registry.register_node(client_name, addr)

                    # Responder al cliente con JSON
                    payload = json.dumps({
                        "assigned_to": client_name,
                        "numbers": numbers
                    })
                    conn.send(payload.encode('utf-8'))

                    ConsoleView.show_message(f"Números enviados a {client_name}")

                except Exception as e:
                    ConsoleView.show_message(f"Error con cliente {addr}: {e}")
                finally:
                    conn.close()

        except KeyboardInterrupt:
            ConsoleView.show_message("Servidor detenido con Ctrl+C")
            self.server.close()
