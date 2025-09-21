from controller.ClientController import ClientController

if __name__ == "__main__":
    cliente = ClientController()
    try:
        cliente.iniciar()
    except KeyboardInterrupt:
        print("⏹ Cliente detenido")
    finally:
        cliente.cerrar()
