class Balanceamento_Carga(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.config_servidor()


    def config_servidor(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = (entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = (entrada.readline(1).rstrip("\n"))
        print("configuração do Balanceamento de carga:")
        print("Número máximo de ticks por tarefa: ", self.tick_por_tarefa)
        print("Número máximo de usuários por servidores virtuais: ", self.max_users_servidor)

    def config_(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = (entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = (entrada.readline(1).rstrip("\n"))


Balanceamento_Carga()
