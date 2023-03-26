import PySimpleGUI as sg

sg.theme('purple')

newemail = 'a'
newsenha = 1

def login():
    sg.theme('Dark')
    layout = [
        [sg.Text('Email:'), sg.Input(text_color='white', key='-EMAIL-')],
        [sg.Text('Senha:'), sg.Input(text_color='white', key='-SENHA-')],
        [sg.Button('Login', key='-LOGIN-')],
        [sg.Button('Esqueci a senha', key="-RECOVER-"), sg.Button('Cadastrar', key='-CADASTRAR-')]
    ]
    return sg.Window('Login', layout=layout, finalize=True, size=(1000,500), element_justification='c')

def cadastro():
    sg.theme('Dark')
    Cadastro = [
        [sg.Text('Novo email:'), sg.Input(key ='-NEWEMAIL-')],
        [sg.Text('Nova Senha:'), sg.Input(key ='-NEWSENHA-')],
        [sg.Button('Fazer login')]
]
    return sg.Window('Cadastro', layout=Cadastro, finalize=True, size=(1000,500), element_justification='c')

def recover():
    sg.theme('Dark')
    Recover = [
        [sg.Text('Nova senha'), sg.Input(key="-RECOVER-")]
    ]
    return sg.Window('Recover', layout= Recover, finalize=True, size = (500, 300), element_justification='c' )

janela1, janela2, janela3= login(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == "-CADASTRAR-":
        janela2 = cadastro()
        janela1.hide()
    if window == janela2 and event == 'Fazer login':
        newemail = values["-NEWEMAIL-"]
        newsenha = values["-NEWSENHA-"]
        values["-EMAIL-"] = newemail
        values["-SENHA-"] = newsenha
        janela2.hide()
        janela1.un_hide()
    if window == janela1 and event == "-LOGIN-":
        print(f'{values["-EMAIL-"], {values["-SENHA-"]}}')
        print(f'{newemail}, {newsenha}')
        if values["-EMAIL-"] != newemail or values["-SENHA-"] != newsenha:
            sg.PopupError('Email ou senha incorretos')
        else:
            sg.Popup(f'Seja bem vindo, {values["-EMAIL-"]}')
    if window == janela1 and event == "-RECOVER-":
        janela3 = recover()
        janela1.hide()
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    
    # Ainda Falta ajustar o "Recover!"
    

        


   
            
        
    