#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Biblioteca padrão
import os
from time import sleep
import shutil

# Biblioteca terceiros
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def formata_str(msg):
    msg = f'>>>>> {msg}'
    tamanho_msg = len(msg)
    print('*' * tamanho_msg)
    print(msg)


def organiza(opcao, main_path):
    if main_path != '':
        if opcao == 'S':
            arquivos_dir = os.listdir(main_path)

            user_extension = input('Qual é a extensão? ')

            dest_path = (main_path + '/' + user_extension)

            for arq in arquivos_dir:
                file, separator, extension = arq.partition('.')
                main_file_path = (main_path + '\\' + arq)

                if os.path.exists(dest_path):
                    if extension == user_extension:
                        os.system('')
                        print(f'\033[33m>>>>> Arquivo' + f' "{extension}" ' +
                            f'encontrado: {file}\033[0;0m')
                        print(f'>>>>> Movendo arquivo: "{file}" para "{dest_path}"')
                        shutil.move(main_file_path, dest_path)
                        print(f'\033[32m>>>>> Arquivo movido com sucesso\033[0;0m\n')
                        sleep(0.5)

                else:
                    os.system('')
                    os.mkdir(dest_path)
                    if extension == user_extension:
                        print(f'\033[33m>>>>> Arquivo' + f' "{extension}" ' +
                            f'encontrado: {file}\033[0;0m')
                        print(
                            f'>>>>> Movendo arquivo: "{file}" para "{dest_path}"')
                        shutil.move(main_file_path, dest_path)
                        print(f'\033[32m>>>>> Arquivo movido com sucesso\033[0;0m\n')
                        sleep(0.5)
            opcao = input('Deseja continuar? [S/N] ')
            if (opcao == 's') or (opcao == 'S'):
                opcao_diretorio = input('Deseja continuar na mesma pasta? [S/N] ')
                if (opcao_diretorio == 's') or (opcao_diretorio == 'S'):
                    pass

                elif (opcao_diretorio == 'n') or (opcao_diretorio == 'N'):
                    main_path = filedialog.askdirectory()
                    opcao = 'S'
                    organiza(opcao, main_path)

                else:
                    msg = 'Aviso: Opção inválida'
                    formata_str(msg)
                    sleep(0.7)
                    os.system('cls')
                    opcao = 'S'
                    organiza(opcao, main_path)
                opcao = 'S'
                organiza(opcao, main_path)

            elif (opcao == 'n') or (opcao == 'N'):
                opcao = opcao.upper()
                organiza(opcao, main_path)

            else:
                msg = 'Aviso: Opção inválida'
                formata_str(msg)
                sleep(0.7)
                os.system('cls')
                opcao = 'S'
                organiza(opcao, main_path)

        elif opcao == 'N':
            msg = 'Finalizando... Volte sempre!'
            formata_str(msg)
            sleep(3)
            os.system('cls')
            exit

        else:
            msg = 'Aviso: Opção inválida'
            formata_str(msg)
            sleep(0.7)
            os.system('cls')
            opcao = 'S'
            organiza(opcao, main_path)
    else:
        msg = 'Diretório não selecionado...'
        formata_str(msg)
        sleep(3)
        os.system('cls')
        opcao = 'S'
        main_path = filedialog.askdirectory()
        organiza(opcao, main_path)

print('Selecione o diretório que você deseja organizar: ')
sleep(2)
opcao = 'S'
main_path = filedialog.askdirectory()
organiza(opcao, main_path)
