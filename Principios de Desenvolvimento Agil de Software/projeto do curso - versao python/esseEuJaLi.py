import os
import PySimpleGUI as sg
import string

# Dados pré-cadastrados ------------------------------------------------------

# Usuários cadastrados
usuarios = [
    {
        "user": "Andre",
        "password": "senhaandre",
        "pontos_totais": 0,
        "total_terror": 0,
        "total_romance": 0,
        "conquista_terror": "nao",
        "conquista_romance": "nao",
        "livros_lidos": []
    },
    {
        "user": "Filipe",
        "password": "senhafilipe",
        "pontos_totais": 0,
        "total_terror": 0,
        "total_romance": 0,
        "conquista_terror": "nao",
        "conquista_romance": "nao",
        "livros_lidos": []
    },
    {
        "user": "Mariana",
        "password": "senhamariana",
        "pontos_totais": 20,
        "total_terror": 6,
        "total_romance": 3,
        "conquista_terror": "sim",
        "conquista_romance": "nao",
        "livros_lidos": ["Drácula"]
    },
    {
        "user": "Carlos",
        "password": "senhacarlos",
        "pontos_totais": 30,
        "total_terror": 2,
        "total_romance": 8,
        "conquista_terror": "nao",
        "conquista_romance": "sim",
        "livros_lidos": []
    },
    {
        "user": "Ana",
        "password": "senhana",
        "pontos_totais": 25,
        "total_terror": 5,
        "total_romance": 5,
        "conquista_terror": "sim",
        "conquista_romance": "sim",
        "livros_lidos": ["Drácula", "Orgulho e Preconceito"]
    },
    {
        "user": "Bruno",
        "password": "senhabruno",
        "pontos_totais": 15,
        "total_terror": 4,
        "total_romance": 2,
        "conquista_terror": "nao",
        "conquista_romance": "nao",
        "livros_lidos": []
    },
    {
        "user": "Luiza",
        "password": "senhaluiza",
        "pontos_totais": 22,
        "total_terror": 7,
        "total_romance": 1,
        "conquista_terror": "sim",
        "conquista_romance": "nao",
        "livros_lidos": []
    }
]

# Livros cadastrados
livros = [
    {
        "titulo": "Drácula",
        "autor": "Bram Stoker",
        "genero": "Terror",
        "numero_paginas": 418
    },
    {
        "titulo": "O Iluminado",
        "autor": "Stephen King",
        "genero": "Terror",
        "numero_paginas": 447
    },
    {
        "titulo": "Frankenstein",
        "autor": "Mary Shelley",
        "genero": "Terror",
        "numero_paginas": 280
    },
    {
        "titulo": "O Exorcista",
        "autor": "William Peter Blatty",
        "genero": "Terror",
        "numero_paginas": 340
    },
    {
        "titulo": "O Chamado de Cthulhu",
        "autor": "H.P. Lovecraft",
        "genero": "Terror",
        "numero_paginas": 420
    },
    {
        "titulo": "Orgulho e Preconceito",
        "autor": "Jane Austen",
        "genero": "Romance",
        "numero_paginas": 432
    },
    {
        "titulo": "Romeu e Julieta",
        "autor": "William Shakespeare",
        "genero": "Romance",
        "numero_paginas": 320
    },
    {
        "titulo": "O Morro dos Ventos Uivantes",
        "autor": "Emily Brontë",
        "genero": "Romance",
        "numero_paginas": 416
    },
    {
        "titulo": "Jane Eyre",
        "autor": "Charlotte Brontë",
        "genero": "Romance",
        "numero_paginas": 100
    },
    {
        "titulo": "A Culpa é das Estrelas",
        "autor": "John Green",
        "genero": "Romance",
        "numero_paginas": 66
    }
]

# --------------------------------------------------------------------------

usuario_autenticado = None

# Layouts das telas --------------------------------------------------

# Tela login
layout_login = [
    [sg.Text('Usuario')],
    [sg.Input(key='user')],
    [sg.Text('Senha')],
    [sg.Input(key='password', password_char='*')],
    [sg.Button('Entrar')],
    [sg.Text('', key='mensagem')]
]

# Tela listagem de livros
layout_lista = [
    [sg.Text('', key='mensagem_usuario')],
    [sg.Button('Drácula')],
    [sg.Button('O Iluminado')],
    [sg.Button('Frankenstein')],
    [sg.Button('O Exorcista')],
    [sg.Button('O Chamado de Cthulhu')],
    [sg.Button('Orgulho e Preconceito')],
    [sg.Button('Romeu e Julieta')],
    [sg.Button('O Morro dos Ventos Uivantes')],
    [sg.Button('Jane Eyre')],
    [sg.Button('A Culpa é das Estrelas')],
    [sg.Button('Ranking')],
    [sg.Button('Minhas conquistas')],
]

# Tela de informações do livro
layout_livro = [
    [sg.Text('', key='Titulo')],
    [sg.Text('', key='Autor')],
    [sg.Text('', key='Genero')],
    [sg.Text('', key='lido')],
    [sg.Text('', key='paginas')],
    [sg.Button('Lido')],
    [sg.Button('Voltar')],
]

# -----------------------------------------------------------------------


def conquistas():

    user = usuario_autenticado["user"]
    pontos = usuario_autenticado["pontos_totais"]
    conquista_terror = "Troféu Terror" if usuario_autenticado["conquista_terror"] == "sim" else "Nenhum Troféu"
    conquista_romance = "Troféu Romance" if usuario_autenticado["conquista_romance"] == "sim" else "Nenhum Troféu"
    livros_lidos = usuario_autenticado["livros_lidos"]
    
    layout_conquistas = [
        [sg.Text(f'Usuário: {user}')],
        [sg.Text(f'Pontos Totais: {pontos}')],
        [sg.Text(f'Conquista Terror: {conquista_terror}')],
        [sg.Text(f'Conquista Romance: {conquista_romance}')],
        [sg.Text('Livros Lidos:')],
        [sg.Listbox(values=livros_lidos, size=(40, 10))],
    ]
    
    window = sg.Window('Minhas Conquistas', layout_conquistas)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED :
            window.close()
            break



def ranking():
    usuarios_ordenados = sorted(usuarios, key=lambda usuariosR: usuariosR["pontos_totais"], reverse=True)
    
    layout_ranking = [
        [sg.Text('Ranking dos Usuários')],
        [sg.Table(
            values=[[usuariosR["user"], usuariosR["pontos_totais"]] for usuariosR in usuarios_ordenados],
            headings=["Usuário", "Pontos Totais"],
            display_row_numbers=False,
            auto_size_columns=True,
            num_rows=min(len(usuarios_ordenados), 10),
            key='tabela',
            row_height=30,
        )],
    ]
    
    window = sg.Window('Ranking', layout_ranking)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED :
            window.close()
            break



def atribui_pontos(livro, titulo):
    paginas = int(livro["numero_paginas"])
    usuario_autenticado["livros_lidos"].append(titulo)
    usuario_autenticado["pontos_totais"] += (paginas % 100) + 1

    if livro["genero"] == "Romance":
        usuario_autenticado["total_romance"] += 1
        if usuario_autenticado["total_romance"] >= 5:
            usuario_autenticado["conquista_romance"] = "sim"
    else:
        usuario_autenticado["total_terror"] += 1
        if usuario_autenticado["total_terror"] >= 5:
            usuario_autenticado["conquista_terror"] = "sim"


def buscar_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    return None

def tela_livro(titulo):
    livro = buscar_livro(titulo)
    if livro is None:
        sg.popup("Livro não encontrado!")
        return

    layout_livro = [
        [sg.Text(f'Título: {livro["titulo"]}', key='Titulo')],
        [sg.Text(f'Autor: {livro["autor"]}', key='Autor')],
        [sg.Text(f'Gênero: {livro["genero"]}', key='Genero')],
        [sg.Text(f'Lido: {livro.get("lido")}', key='lido')],
        [sg.Text(f'Número de Páginas: {livro["numero_paginas"]}', key='paginas')],
        [sg.Button('Lido')],

    ]

    window = sg.Window('Informações do Livro', layout_livro)
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        
        elif event == 'Lido':
            if titulo not in usuario_autenticado["livros_lidos"]:
                atribui_pontos(livro, titulo)
                window['lido'].update(f'Lido: sim')
 
        

def listagem():
    window = sg.Window('Eu já li', layout_lista)
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event in ['Drácula', 'O Iluminado', 'Frankenstein', 'O Exorcista', 
                       'O Chamado de Cthulhu', 'Orgulho e Preconceito', 
                       'Romeu e Julieta', 'O Morro dos Ventos Uivantes', 
                       'Jane Eyre', 'A Culpa é das Estrelas']:
            tela_livro(event)

        elif event == 'Ranking':
            ranking()  
            
        elif event == 'Minhas conquistas':
            conquistas()  


def autentica(user, password):
    global usuario_autenticado
    for usuario in usuarios:
        if usuario["user"] == user and usuario["password"] == password:
            usuario_autenticado = usuario
            return True
    return False


def tela_login():
    window = sg.Window('Eu já li', layout_login)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'Entrar':
            user = values['user']
            password = values['password']
            if autentica(user, password):
                window.close()
                listagem()
            else:
                window['mensagem'].update('Usuário ou senha inválidos')
                window['user'].update('')
                window['password'].update('')

def main():
    tela_login()

main()
