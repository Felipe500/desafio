
class Balanceamento_Carga(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.servidores = 0
        self.server = {}
        self.server_lis = []
        self.input_usuarios = []

        self.total_users = 0

        self.Config_Servidor()
        self.Balancear_Carga()



    def Config_Servidor(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = (entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = (entrada.readline(1).rstrip("\n"))
        print("configuração do Balanceamento de carga:")
        print("Número máximo de ticks por tarefa: ", self.tick_por_tarefa)
        print("Número máximo de usuários por servidores virtuais: ", self.max_users_servidor)

    def Entrada_De_Usuarios(self):
        with open("input.txt",'r') as arquivo:
            self.tick_por_tarefa = (arquivo.readline(2).rstrip("\n"))
            self.max_users_servidor = (arquivo.readline(1).rstrip("\n"))
            linha = 0
            for usuarios in arquivo.readlines():
                linha += 1
                if linha > 1:
                    self.input_usuarios.append( int(usuarios.rstrip("\n")))
                    self.total_users = int(usuarios.rstrip("\n")) + self.total_users



    def Balancear_Carga(self):
        self.Entrada_De_Usuarios()
        entrada_users = 0
        linha = 0
        tarefas = 0
        lista = [0]
        user_remover_list = self.input_usuarios.copy()
        #print(self.input_usuarios)
        for x in range(len(self.input_usuarios)+7):
            linha +=1
            cont = 0
            if x<len(self.input_usuarios):

                print('Entrou ',self.input_usuarios[x], ' usuarios')
                entrada_users = self.input_usuarios[x]
                while entrada_users > 0:
                    #print(self.input_usuarios)
                    if entrada_users == 1:

                        if (lista[-1] == 1) or (lista[-1] == 0):
                            lista[-1] = lista[-1] + 1
                            # print(" valor add ", lista)
                            entrada_users = entrada_users - 1
                            # print("lista[-1] ", lista)
                            #print("lista----", lista)
                        else:
                            lista.append(1)
                            # print("lista[-1] ", lista)
                            #print(" 1 user atuais tt", entrada_users)
                            entrada_users = entrada_users - 1
                            #print("lista----", lista)

                    elif entrada_users >= 2:
                        if (lista[-1] == 1):
                            lista[-1] = lista[-1] + 1
                            #print(" valor add ", lista)
                            entrada_users = entrada_users - 1
                            # print("lista[-1] ", lista)
                            #print("lista----", lista)
                        elif lista[-1] == 2:
                            lista.append(2)
                            # print("lista[-1] ", lista)
                            #print(" 1 user atuais tt", entrada_users)
                            entrada_users = entrada_users - 2
                            #print("lista----", lista)

            else:
                print('Entrou 0 usuarios...')

            self.servidores = lista.count(2) + lista.count(1)
            #print("lista----",lista)

            tarefas += 1
            print("contador de ticks: ", tarefas)

            if tarefas > 3:
                #print("removido servidor...")
                tarefas = 4

                if not len(user_remover_list) == 0:

                    users_remover = user_remover_list[0]
                    print("users a serem removidos: ",user_remover_list[0])
                    while users_remover > 0:
                        users_remover = users_remover - 1
                    print(user_remover_list.pop(0))
                else:
                    print("Esperando entrada de usuários: ")


            #print(self.server_lis)
            #print(self.server)
            print("---------------------------------------------------------")
            print("| Tick  | usuários logados | Servidores")
            if x<len(self.input_usuarios):
                print('|', x + 1, "    | ", self.input_usuarios[x], "              | ", self.servidores)
            else:
                print('|', x+1, "   | ",'---', "            | ", self.servidores)
            print("---------------------------------------------------------")
            print("lista ", lista)
            print("--------------------------------------------------------")



Balanceamento_Carga()


