import os

class Coleta:

    def cadastro_coleta_lixo(cadastro_existe, cadastro_coleta):
        cadastro_dic = {}
        with open(cadastro_existe, 'r') as Listar_Log:
            for line in Listar_Log:
                key, value = line.split()
                cadastro_dic[key] = value
            print(cadastro_dic)
        num_casa = input("Digite o numero da casa para cadastro da coleta:")
        for casa_num in cadastro_dic.keys():
            if casa_num == num_casa:
                print("Endereço localizado:")
                name = cadastro_dic[casa_num]
        print(name)

        if (os.path.exists(cadastro_coleta)):
            with open(cadastro_coleta, 'a') as CadastroColeta_Log:
                item_coletado = input("Digite o item a ser coletado:")
                tipo_lixo = input("Selecione o tipo do item a ser coletado (1)- Lixo Reciclavel | (2)- Lixo Comum:")
                print(tipo_lixo)
                if tipo_lixo == "1":
                    tipo_lixo = "Lixo Reciclavel"
                    frota = "A"
                else:
                    tipo_lixo = "Lixo Comum"
                    frota = "B"
                formatado_item_coletado = (f'{item_coletado} ')
                formatado_tipo_lixo = (f'{tipo_lixo}\n')
                CadastroColeta_Log.writelines([f'Frota: {frota}, Item a ser coletado: {formatado_item_coletado}, Endereço: {name}, Tipo do lixo: {formatado_tipo_lixo}'])
        else:
            with open(cadastro_coleta, 'w') as CadastroColeta_Log:
                item_coletado = input("Digite o item a ser coletado:")
                tipo_lixo = input("Selecione o tipo do item a ser coletado (1)- Lixo Reciclavel | (2)- Lixo Comum:")
                if tipo_lixo == 1:
                    tipo_lixo = "Lixo Reciclavel"
                    frota = "A"
                else:
                    tipo_lixo = "Lixo Comum"
                    frota = "B"
                formatado_item_coletado = (f'{item_coletado} ')
                formatado_tipo_lixo = (f'{tipo_lixo}\n')
                CadastroColeta_Log.writelines([f'Frota: {frota}, Item a ser coletado: {formatado_item_coletado}, Endereço: {name}, Tipo do lixo: {formatado_tipo_lixo}'])

    def listar_coleta(cadastro_coleta):
        with open(cadastro_coleta, 'r') as Listar_Log:
            # print(Listar_Log.readlines())
            for line in Listar_Log:
                print(line.rstrip('\n'))

    def despejar_coleta(cadastro_coleta):
        with open(cadastro_coleta, 'w') as Listar_Log:
            Listar_Log.write('')
            print("Despejo executado com sucesso")