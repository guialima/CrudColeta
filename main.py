import os
import time
import pprint
from residencia import *
from coleta import *



def busca_frota(cadastro_coleta):
    data = []
    with open(cadastro_coleta, 'r') as Listar_Log:
        for line in Listar_Log:
            data.append(line.split(','))
    convert_list = tuple(data)
    dic = dict(enumerate(data))
    qual_frota = input("Selecione qual frota voce gostaria de filtrar (A)- Frota(Lixo Reciclavel) | (B)- Frota(Lixo Comum):")
    if qual_frota == "A":
        frota = "Frota: A"
    else:
        frota = "Frota: B"
    lista_exibicao = []
    int = 0
    for key in dic.items():
        values = dic.get(int)
        if frota in values:
            lista_exibicao.append(values)
        #if key == 1:
         #   print(dic.get(key))
        int += 1
    pprint.pprint(lista_exibicao)
    #print(lista_exibicao, sep=']')



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
            Residencia.cadastro_residencia(cadastro)
        elif choice == '2':
            Residencia.listar_residencia(cadastro)
        elif choice == '3':
            Coleta.cadastro_coleta_lixo(cadastro, cadastro_coleta)
        elif choice == '4':
            Coleta.listar_coleta(cadastro_coleta)
        elif choice == '5':
            Coleta.despejar_coleta(cadastro_coleta)
        elif choice == '6':
            busca_frota(cadastro_coleta)
        elif choice == '7':
            break
        elif choice == '0':
            exit()


if __name__ == "__main__":
    main()
