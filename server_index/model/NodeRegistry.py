import random

class NodeRegistry:
    """Registro de nodos conectados."""

    def __init__(self):
        self.nodes = {}

    def register_node(self, name, address):
        """Registra un nodo con 11 números aleatorios (0-10)."""
        numbers = [random.randint(0, 10) for _ in range(11)]
        self.nodes[name] = {"address": address, "numbers": numbers}
        print(f"[NodeRegistry] {name} registrado en {address} -> {numbers}")
        return numbers

    def list_nodes(self):
        """Devuelve todos los nodos registrados."""
        return self.nodes
