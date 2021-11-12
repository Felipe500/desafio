import random
import string
import termtables as tt

class servidor(object):
    def __init__(self):
        self.nome_servidor = 'NRE-'+self.Gerar_nome()
        #print("Meu servidor: "+ str(self.nome_servidor))
        self.alocacao = 0
    def __str__(self):
        return self.nome_servidor

    def Gerar_nome(self):
        return  ''.join(random.choice(string.ascii_lowercase) for i in range(6))




class Balanceamento_Carga(object):
    def __init__(self):
        self.tick_por_tarefa = 0
        self.max_users_servidor = 0
        self.servidores = 0
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
            linha = 0
            for usuarios in arquivo.readlines():
                linha += 1
                if linha > 2:
                    self.usuarios.append( int(usuarios.rstrip("\n")))


    def Balancear_Carga(self):
        entrada_users = 1
        with open("input.txt",'r') as arquivo:
            linha  = 0

            for usuarios in arquivo.readlines():
                linha +=1


                if linha > 2:
                    self.total_users =  int(usuarios.rstrip("\n")) + self.total_users
                    entrada_users += int(usuarios.rstrip("\n"))
                    self.tick_por_tarefa = (arquivo.readline(2).rstrip("\n"))
                    self.max_users_servidor = (arquivo.readline(1).rstrip("\n"))

                    if (entrada_users>0) and (entrada_users >= 2):
                        print("+1 Servidor Criado")
                        self.servidores += 1
                        print("users atual: ", self.total_users)
                        entrada_users = 0

                    print("---------------------------------------------------------")
                    print("| Tick  | usuários | Servidores")
                    print('|', linha - 2, "    | ", usuarios.rstrip("\n"), "      | ", self.servidores)

            print("users: ",self.total_users)




a1 = servidor()
print(a1.nome_servidor)
a2 = servidor()
print(a2.nome_servidor)
a3 = servidor()
print(a3.nome_servidor)
Balanceamento_Carga()


