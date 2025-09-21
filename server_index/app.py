from controller.IndexController import IndexController

if __name__ == "__main__":
    index = IndexController(host="localhost", port=5000)
    index.start()
