from abc import ABC, abstractmethod
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class Encender(Command):
    def __init__(self):
        pass

    def execute(self):
        print("Encendido")

class Apagar(Command):

    def __init__(self):
        pass

    def execute(self):
        print(" Bye! ")

class Hablar(Command):
    def __init__(self, message):
        self.mensaje = message

    def execute(self):
        print(self.mensaje)

class Dormir(Command):
    def __init__(self, message):
        pass

    def execute(self):
        print("See you soon!")


