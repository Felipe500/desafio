
class Balanceamento_Carga(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.servidores = 0
        self.server = {}
        self.server_lis = []
        self.usuarios = []

        self.total_users = 0

        self.config_servidor()
        self.Balancear_Carga()



    def config_servidor(self):
        with open("input.txt",'r') as entrada:
            self.tick_por_tarefa = (entrada.readline(2).rstrip("\n"))
            self.max_users_servidor = (entrada.readline(1).rstrip("\n"))
        print("configuração do Balanceamento de carga:")
        print("Número máximo de ticks por tarefa: ", self.tick_por_tarefa)
        print("Número máximo de usuários por servidores virtuais: ", self.max_users_servidor)

    def entrada_de_usuarios(self):
        with open("input.txt",'r') as arquivo:
            self.tick_por_tarefa = (arquivo.readline(2).rstrip("\n"))
            self.max_users_servidor = (arquivo.readline(1).rstrip("\n"))
            linha = 0
            for usuarios in arquivo.readlines():
                linha += 1
                if linha > 2:
                    self.usuarios.append( int(usuarios.rstrip("\n")))
                    self.total_users = int(usuarios.rstrip("\n")) + self.total_users


    def listar(self):
        cont = 0
        for users in range(self.total_users):

            if cont == 2:
                self.server_lis.append(users)
                cont = 0
            else:
                #self.server_lis[0] = cont
                cont += 1
    def Balancear_Carga_2(self):
        self.entrada_de_usuarios()
        entrada_users = 0
        linha = 0
        tarefas = 0
        lista = [0]

        for x in range(self.total_users+ 4):
            linha +=1
            cont = 0

            while entrada_users > 0:

                if entrada_users == 1:
                    # print("lista[-1] ",lista[-1])
                    if (lista[-1] == 1) or (lista[-1] == 0):
                        lista[-1] = lista[-1] + 1
                        # print(" valor add ", lista)
                        entrada_users = entrada_users - 1
                        # print("lista[-1] ", lista)
                    else:
                        lista.append(1)
                        # print("lista[-1] ", lista)
                        print(" 1 user atuais tt", entrada_users)
                        entrada_users = entrada_users - 1

                elif entrada_users >= 2:
                    if (lista[-1] == 1):
                        lista[-1] = lista[-1] + 1
                        print(" valor add ", lista)
                        entrada_users = entrada_users - 1
                        # print("lista[-1] ", lista)
                    elif lista[-1] == 2:
                        lista.append(2)
                        # print("lista[-1] ", lista)
                        print(" 1 user atuais tt", entrada_users)
                        entrada_users = entrada_users - 2



            print("lista----",lista)
            tarefas += 1
            print("contador de ticks: ", tarefas)
            if tarefas == 4:
                print("removido servidor...")
                tarefas = 0

            print(self.server_lis)
            print(self.server)
            print("---------------------------------------------------------")
            print("| Tick  | usuários logados | Servidores")
            if x<len(self.usuarios):
                print('|', x + 1, "    | ", self.usuarios[x], "              | ", self.servidores)
            else:
                print('|', x+1, "   | ",'---', "            | ", self.servidores)
            print("---------------------------------------------------------")
            print("lista ", lista)



    def Balancear_Carga(self):
        entrada_users = 0
        lista = [0]
        cont = 0
        entre_user_list =[]
        self.entrada_de_usuarios()
        with open("input.txt",'r') as arquivo:
            linha  = 0
            #self.usuarios
            for usuarios in arquivo.readlines():
                linha +=1


                if linha > 2:
                    self.total_users =  int(usuarios.rstrip("\n")) + self.total_users
                    entrada_users += int(usuarios.rstrip("\n"))
                    entre_user_list.append(int(usuarios.rstrip("\n")))
                    self.tick_por_tarefa = (arquivo.readline(2).rstrip("\n"))
                    self.max_users_servidor = (arquivo.readline(1).rstrip("\n"))
                    cont = cont + 1
                    print("users atual : ", entrada_users)

                    if cont == 4:
                        user_remove = entre_user_list[0]
                        print("remover usuarios: ",user_remove)
                        cont = 0


                    while entrada_users > 0:

                        if entrada_users == 1:
                            #print("lista[-1] ",lista[-1])
                            if (lista[-1] == 1) or (lista[-1] == 0):
                                lista[-1] = lista[-1] + 1
                                #print(" valor add ", lista)
                                entrada_users = entrada_users - 1
                                #print("lista[-1] ", lista)
                            else:
                                lista.append(1)
                                #print("lista[-1] ", lista)
                                print(" 1 user atuais tt", entrada_users)
                                entrada_users = entrada_users - 1

                        elif entrada_users >= 2:
                            if (lista[-1] == 1):
                                lista[-1] = lista[-1] + 1
                                print(" valor add ", lista)
                                entrada_users = entrada_users - 1
                                #print("lista[-1] ", lista)
                            elif lista[-1] == 2:
                                lista.append(2)
                                #print("lista[-1] ", lista)
                                print(" 1 user atuais tt", entrada_users)
                                entrada_users = entrada_users - 2

                    self.servidores = lista.count(2) + lista.count(1)
                    print("lista[-1] atual ", lista)
                    #print(self.server_lis)
                    #print(self.server)
                    print("---------------------------------------------------------")
                    print("| Tick  | usuários | Servidores")
                    print('|', linha - 2, "    | ", usuarios.rstrip("\n"), "      | ",self.servidores )
                    print("---------------------------------------------------------")
                    print("lista--- ", lista)

            print("users: ",self.total_users)
            self.listar()



Balanceamento_Carga()


