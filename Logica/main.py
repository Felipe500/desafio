class ServidorVirtual(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.config_servidor()


    def config_servidor(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = (entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = (entrada.readline(1).rstrip("\n"))
        print("config: ", x ,"  -- " ,y)

ServidorVirtual()
