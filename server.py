import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_clear(self):
        self.value.clear()
        return "List cleared."

    def exposed_size(self):
        return len(self.value)

    def exposed_remove(self, item):
        try:
            self.value.remove(item)
            return f"Removed: {item}"
        except ValueError:
            return f"Item '{item}' not found."

    def exposed_contains(self, item):
        return item in self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    print(f"Server running on port {PORT}")
    server.start()
