from command import Command, Hablar, Encender, Apagar, Dormir


class Bot:
    "comando = None"
    def __init__(self):
        pass

    def accion(self, order):
        try:
            order.execute()
        except NameError:
            print('An exception flew by!')
            raise


bot = Bot()
bot.accion(Encender())
bot.accion(Apagar())
bot.accion(Comer())
