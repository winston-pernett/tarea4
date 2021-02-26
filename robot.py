from command import Command, Hablar, Encender, Apagar, Dormir


class Bot:
    def __init__(self):
        pass

    def accion(self, comando):
        comando.execute()

bot = Bot()
bot.accion(Encender())
bot.accion(Apagar())
bot.accion(Comer())
