import os
import time

class Residencia:

    def cadastro_residencia(self):
        if (os.path.exists(self)):
            with open(self, 'a') as Cadastro_Log:
                num_casa = input("Digite o numero da casa:")
                endereco_casa = input("Digite o endereço da casa:")
                formatado_num_casa = (f'{num_casa} ')
                formatado_endereco_casa = (f'{endereco_casa}')
                Cadastro_Log.writelines([formatado_num_casa, formatado_endereco_casa])
        else:
            with open(self, 'w') as Cadastro_Log:
                num_casa = input("Digite o numero da casa:")
                endereco_casa = input("Digite o endereço da casa:")
                formatado_num_casa = (f'{num_casa} ')
                formatado_endereco_casa = (f'{endereco_casa}')
                Cadastro_Log.writelines([formatado_num_casa, formatado_endereco_casa])

    def listar_residencia(self):
        with open(self, 'r') as Listar_Log:
            # print(Listar_Log.readlines())
            for line in Listar_Log:
                print(line.rstrip('\n'))
