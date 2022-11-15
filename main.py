import os
import time


def cadastro_residencia(cadastro_existe):
    if (os.path.exists(cadastro_existe)):
        with open(cadastro_existe, 'a') as Cadastro_Log:
            num_casa = input("Digite o numero da casa:")
            endereco_casa = input("Digite o endereço da casa:")
            formatado_num_casa = (f'{num_casa} ')
            formatado_endereco_casa = (f'{endereco_casa}')
            Cadastro_Log.writelines([formatado_num_casa, formatado_endereco_casa])
    else:
        with open(cadastro_existe, 'w') as Cadastro_Log:
            num_casa = input("Digite o numero da casa:")
            endereco_casa = input("Digite o endereço da casa:")
            formatado_num_casa = (f'{num_casa} ')
            formatado_endereco_casa = (f'{endereco_casa}')
            Cadastro_Log.writelines([formatado_num_casa, formatado_endereco_casa])


def listar_residencia(cadastro_existe):
    with open(cadastro_existe, 'r') as Listar_Log:
        print(Listar_Log.readlines())


def listar_coleta(cadastro_coleta):
    with open(cadastro_coleta, 'r') as Listar_Log:
        print(Listar_Log.readlines())

def busca_frota(cadastro_coleta):
    data = []
    with open(cadastro_coleta, 'r') as Listar_Log:
        for line in Listar_Log:
            data.append(line.split(','))
    convert_list = tuple(data)
    dic = dict(enumerate(data))
    frota = "Frota: B"
    lista_exibicao = []
    for key in dic.items():
        int = 0
        values = dic.get(int)
        if frota in values:
            lista_exibicao.append(values)
        #if key == 1:
         #   print(dic.get(key))
        int += 1
    print(lista_exibicao[int])



def despejar_coleta(cadastro_coleta):
    with open(cadastro_coleta, 'w') as Listar_Log:
        Listar_Log.write('')
        print("Despejo executado com sucesso")


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
            tipo_lixo = input("Selecione o tipo do item a ser coletado (1)- Lixo Reciclavel | (2)- Lixo Comum: ")
            if tipo_lixo == 1:
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
            tipo_lixo = input("Selecione o tipo do item a ser coletado (1)- Lixo Reciclavel | (2)- Lixo Comum: ")
            if tipo_lixo == 1:
                tipo_lixo = "Lixo Reciclavel"
                frota = "A"
            else:
                tipo_lixo = "Lixo Comum"
                frota = "B"
            formatado_item_coletado = (f'{item_coletado} ')
            formatado_tipo_lixo = (f'{tipo_lixo}\n')
            CadastroColeta_Log.writelines([f'Frota: {frota}, Item a ser coletado: {formatado_item_coletado}, Endereço: {name}, Tipo do lixo: {formatado_tipo_lixo}'])


def main():
    cadastro = 'C:\\Users\\gui_a\\PycharmProjects\\CrudColeta\\cadastro.txt'
    cadastro_coleta = 'C:\\Users\\gui_a\\PycharmProjects\\CrudColeta\\cadastro_coleta.txt'
    while True:
        print(("Bem vindo Coleta Crud"))
        print("\nChoose service you want to use : ")
        print("""
        1 : Cadastro Residencia 
        2 : Listar Residencia
        3 : Cadastrar coleta do lixo
        4 : Listar Coleta Lixo
        5 : Despejar Coleta
        6 : Buscar por frota
        7 : ??
        0 : Exit"""
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            cadastro_residencia(cadastro)
        elif choice == '2':
            listar_residencia(cadastro)
        elif choice == '3':
            cadastro_coleta_lixo(cadastro, cadastro_coleta)
        elif choice == '4':
            listar_coleta(cadastro_coleta)
        elif choice == '5':
            despejar_coleta(cadastro_coleta)
        elif choice == '6':
            busca_frota(cadastro_coleta)
        elif choice == '7':
            break
        elif choice == '0':
            exit()


if __name__ == "__main__":
    main()
