
class Balanceamento_Carga(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.servidores = 0
        self.saida_lista = []
        self.entrada_lista = []
        self.input_usuarios = []

        self.total_users = 0

        self.Config_Servidor()
        self.Balancear_Carga()



    def Config_Servidor(self):
        pass

    def Saida_De_Usuarios(self, *lista):
        with open("output.txt", 'w') as saida:
            for valor in lista:
                saida.write(str(valor) + '\n')


    def Entrada_De_Usuarios(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = int(entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = int(entrada.readline(1).rstrip("\n"))
            print("configuração do Balanceamento de carga:")
            print("Número máximo de ticks por tarefa: ", self.tick_por_tarefa)
            print("Número máximo de usuários por servidores virtuais: ", self.max_users_servidor)

            linha = 0
            for usuarios in entrada.readlines():
                linha += 1
                if linha > 1:
                    self.input_usuarios.append( int(usuarios.rstrip("\n")))
                    self.total_users = int(usuarios.rstrip("\n")) + self.total_users



    def Balancear_Carga(self):
        self.Entrada_De_Usuarios()
        contador_tick = 0
        limite_max_ticks = 0
        lista = [0]
        user_remover_list = self.input_usuarios.copy()
        #print(self.input_usuarios)
        total_ticks = int(len(self.input_usuarios))+ (self.tick_por_tarefa)
        for tick in range(total_ticks):
            contador_tick +=1



            limite_max_ticks += 1


            if limite_max_ticks > 4:
                #print("removido servidor...")
                limite_max_ticks = 4
                print("contador de ticks atingiu: ", limite_max_ticks)
                if not len(user_remover_list) == 0:

                    users_remover = user_remover_list.pop(0)
                    print("users a serem removidos: ",users_remover)
                    while users_remover > 0:
                        if users_remover == 1:

                            if lista[0] == 1:
                                lista.pop(0)
                                users_remover = users_remover - 1

                            elif lista[0] >= self.max_users_servidor:
                                lista[0] = lista[0] - 1
                                users_remover = users_remover - 1

                        elif users_remover >= 2:

                            if (lista[0] == 1):
                                lista.pop(0)
                                users_remover = users_remover - 1

                            elif lista[0] > 1:
                                lista[0] = lista[0] - 1
                                users_remover = users_remover - 1


                else:
                    print("Esperando entrada de usuários: ")

            if tick<len(self.input_usuarios):

                print('Entrou ',self.input_usuarios[tick], ' usuarios')
                entrada_users = self.input_usuarios[tick]
                while entrada_users > 0:
                    print("r")

                    if entrada_users == 1:

                        if (lista[-1] == 1) or (lista[-1] == 0):
                            lista[-1] = lista[-1] + 1
                            entrada_users = entrada_users - 1

                        elif lista[-1] >= self.max_users_servidor:
                            lista.append(1)
                            entrada_users = entrada_users - 1

                    elif entrada_users >= 2:
                        if (lista[-1] < self.max_users_servidor):
                            lista[-1] = lista[-1] + 1
                            entrada_users = entrada_users - 1

                        elif lista[-1] == self.max_users_servidor:
                            lista.append(self.max_users_servidor)
                            entrada_users = entrada_users - self.max_users_servidor


            else:
                print('Entrou 0 usuarios...')
            #print(self.server_lis)
            #print(self.server)

            numero_servidores = lista.count(2) + lista.count(1)
            print("---------------------------------------------------------")
            print("| Tick  | usuários logados | Servidores")
            if tick<len(self.input_usuarios):
                self.Saida_De_Usuarios(lista)

                print('|', tick + 1, "    | ", self.input_usuarios[tick], "              | ", numero_servidores)
            else:
                print('|', tick+1, "   | ",'---', "            | ", numero_servidores)
            print("---------------------------------------------------------")
            print("lista ", lista)
            print("--------------------------------------------------------")
        self.Saida_De_Usuarios(lista)



Balanceamento_Carga()


