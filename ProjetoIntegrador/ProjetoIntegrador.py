import PySimpleGUI as janelas
import mysql.connector

#conexão com banco de dados
conexao = mysql.connector.connect(
    host = '209.209.40.87',
    port = 19505,
    user = 'Teste',
    password = '123456789',
    database = 'BD_MACAW'
)

cursor = conexao.cursor()

# Criar janelas e estilos.


#Janela login
def janela_login():
    janelas.theme('Green')
    layout = [
        [janelas.Image(r"assests\Logo_200.png", s = (None,None), pad = (150, None))],
        [janelas.Text('                Usuario:', ), janelas.Input(key='usuario', size = (30, 1))],
        [janelas.Text('                Senha:  ', ), janelas.Input(key='senha', password_char='*', size = (30, 1))],
        [janelas.Button('Entrar', pad = (200, 0))]
    ]

    return  janelas.Window('Tela de Login', layout, size = (500, 600), finalize= True )

#Janela Home
def janela_escolha():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Escolha que tipo de opção faz sua necessidade:', size=(35,1))],
        [janelas.Button('Cadastro de funcionarios', size=(20,1)), janelas.Button('Cadastro de aluno', size=(20, 1))], # butões de escolha de janelas.
        [janelas.Button('Cadastro de diciplinas', size=(20,1)), janelas.Button('Cadastro de curso', size=(20, 1))],
        [janelas.Button('Cadastro de turno', size=(20,1)), janelas.Button('Matricula', size=(20, 1))]
    ]
    return janelas.Window('escolha', layout=layout, finalize=True, size = (500, 600)) #Chamando a janela

#Janela cadastro aluno
def janela_cadastro_aluno():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Nome:    '), janelas.Input(key ='nome', size=(40,3))],
        [janelas.Text('E-mail:   '), janelas.Input(key ='email', size=(40,3))],
        [janelas.Text('Telefone:'), janelas.Input(key ='telefone', size=(40,3))],
        [janelas.Text('Cep:      '), janelas.Input(key ='cep', size=(40,3))],
        [janelas.Text('CPF:     '), janelas.Input(key ='cpf', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de aluno', layout=layout,  finalize=True, size = (500, 600))  

#Janela cadastro funcionarios
def janela_cadastro_funcionarios():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Nome:    '), janelas.Input(key = 'nome', size=(40,3))],
        [janelas.Text('E-mail:   '), janelas.Input(key = 'email', size=(40,3))],
        [janelas.Text('Telefone:'),janelas.Input(key = 'telefone', size=(40,3))],
        [janelas.Text('Cep:      '), janelas.Input(key = 'cep', size=(40,3))],
        [janelas.Text('CPF:     '), janelas.Input(key = 'cpf', size=(40,3))],
        [janelas.Text('Senha:  '), janelas.Input(key = 'senha', password_char='*', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de funcionarios', layout=layout,  finalize=True, size = (500, 600))  

#Janela cadastro disciplina
def janela_cadastro_disciplina():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Nome da disciplina'), janelas.Input(key = 'disciplina', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de diciplinas', layout=layout,  finalize=True, size = (500, 600))  

#Janela cadastro curso
def janela_cadastro_curso():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Nome do curso:'), janelas.Input(key = 'curso', size=(40,3))],
        [janelas.Text('Carga horário:   '), janelas.Input(key = 'cghr', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de curso', layout=layout,  finalize=True, size = (500, 600))  

#Janela cadastro turno
def janela_cadastro_turno():
    janelas.theme('Green')
    layout = [
        [janelas.Text('Nome do Turno:'), janelas.Input(key = 'turno', size=(40,3))],
        [janelas.Text('Carga horário:   '), janelas.Input(key = 'cghr', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de turno', layout=layout, finalize=True, size = (500, 600))  

#janela cadastro matricula
def janela_cadastro_matricula(): 
    janelas.theme('Green')
    
    #Função retorno cpf
    def cpf():
        comando = f'SELECT CPF FROM TB_ALUNO'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        CPF = []
        CPF_solo = []

        for cpf in resultado[0:len(resultado)]:
            CPF.append(cpf)

        for cpf in CPF:
            index_cpf = CPF.index(cpf)
            cpf_tratado = CPF[index_cpf]
            novo_curso = cpf_tratado[0].replace('{}', '')
            CPF_solo.append(novo_curso)
        
        return CPF_solo
    
    #Função retorno curso
    def cursos():
        comando = f'SELECT NOME_CURSO FROM TB_CURSO'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        cursos = []
        cursos_solo = []

        for curso in resultado[0:len(resultado)]:
            cursos.append(curso)

        for curso in cursos:
            index_curso = cursos.index(curso)
            curso_tratado = cursos[index_curso]
            novo_curso = curso_tratado[0].replace('{}', '')
            cursos_solo.append(novo_curso)
        
        return cursos_solo
    
    #Função retorno diciplina
    def diciplina():
        comando = f'SELECT NOME_DISCIPLINA FROM TB_DISCIPLINA'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        diciplinas = []
        diciplinas_solo = []

        for Diciplinas in resultado[0:len(resultado)]:
            diciplinas.append(Diciplinas)

        for Diciplinas in diciplinas:
            index_Diciplinas = diciplinas.index(Diciplinas)
            Diciplinas_tratado = diciplinas[index_Diciplinas]
            novo_Diciplinas = Diciplinas_tratado[0].replace('{}', '')
            diciplinas_solo.append(novo_Diciplinas)
        
        return  diciplinas_solo
    
    #Função retorno turno    
    def turno():
        comando = f'SELECT NOME_TURNO FROM TB_TURNO'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        turnos = []
        turnos_solo = []

        for Turnos in resultado[0:len(resultado)]:
            turnos.append(Turnos)

        for Turnos in turnos:
            index_Turnos = turnos.index(Turnos)
            Turnos_tratado = turnos[index_Turnos]
            novo_Turnos = Turnos_tratado[0].replace('{}', '')
            turnos_solo.append(novo_Turnos)
        
        return  turnos_solo
    
    #Tela cadastro matricula    
    layout = [
        [janelas.Text('CPF:      '), janelas.Combo(values= list(cpf()),k='CPF', size=(40,3))],
        [janelas.Text('Curso:    '), janelas.Combo(values= list(cursos()), key = 'cursos', size=(40,3))],
        [janelas.Text('Diciplina:'), janelas.Combo(values= list(diciplina()), key = 'Diciplina', size=(40,3))],
        [janelas.Text('Turno:    '), janelas.Combo(values= list(turno()), key = 'Turno', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Matricula', layout=layout,  finalize=True, size = (500, 600)) 

# Criar as janelas inicias.
janelaLogin, janelaHome, janelaCadAluno, janelaCadFuncionario, janelaCadDisciplina, janelaCadCurso, janelaCadTurno, janelaCadMatricula   = janela_login(), None, None, None, None, None, None, None #Criadas das duas janelas, o None serve para que a janela não recebar nenhum valor.

# Criar um loop de leitura de eventos.
while True: # lupe infinito
    window,event,values = janelas.read_all_windows()
    # Verificação de login
    if window == janelaLogin and event == 'Entrar':
        #Verificação de email
        verificacao = "SELECT EMAIL FROM TB_FUNCIONARIOS WHERE EMAIL ='{}'".format(values['usuario'])
        cursor.execute(verificacao)
        resultado = cursor.fetchall()

        verificacao_campo_funcionarios=''

        if len(resultado) != 0:
            verificacao_campo_funcionarios = 'EMAIL'
        #término verificação de email

        #Verificação de cpf
        if verificacao_campo_funcionarios != 'EMAIL':
            verificacao = "SELECT CPF FROM TB_FUNCIONARIOS WHERE CPF ='{}'".format(values['usuario'])
            cursor.execute(verificacao)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                verificacao_campo_funcionarios = 'CPF'

        if verificacao_campo_funcionarios != 'EMAIL' and verificacao_campo_funcionarios != 'CPF':
            verificacao_campo_funcionarios = 'INVALIDO'
        # Término verificação cpf

        # Validação login
        if verificacao_campo_funcionarios == 'EMAIL' or verificacao_campo_funcionarios == 'CPF':

            verificacao = "SELECT SENHA FROM TB_FUNCIONARIOS WHERE {} ='{}'".format(verificacao_campo_funcionarios, values['usuario'])
            cursor.execute(verificacao)
            password_login = cursor.fetchall()

            
            if values['senha'] in password_login[0]:

                janelaHome = janela_escolha()
                janelaLogin.hide()
            else:
                janelas.popup('Você digitou uma senha invalida, tente novamente.')
        elif verificacao_campo_funcionarios == 'INVALIDO':
            janelas.popup('Você digitou um usuario, tente novamente.')


    # Quando queremos ir para próxima janela;
    if window == janelaHome and event == 'Cadastro de aluno': 
        janelaCadAluno = janela_cadastro_aluno()
        janelaHome.hide() 
     # Do home até  cadastro até funcionarios; 
    if window == janelaHome and event == 'Cadastro de funcionarios': 
        janelaCadFuncionario = janela_cadastro_funcionarios()
        janelaHome.hide()
    # Do home até  cadastro até diciplinas; 
    if window == janelaHome and event == 'Cadastro de diciplinas': 
        janelaCadDisciplina = janela_cadastro_disciplina()
        janelaHome.hide()       
    # Do home até  cadastro até diciplinas; 
    if window == janelaHome and event == 'Cadastro de curso':
        janelaCadCurso = janela_cadastro_curso()
        janelaHome.hide()
    # Do home até  cadastro até turno;
    if window == janelaHome and event == 'Cadastro de turno':
        janelaCadTurno = janela_cadastro_turno()
        janelaHome.hide()
    # Do home até  cadastro até Matricula;
    if window == janelaHome and event == 'Matricula':
        janelaCadMatricula = janela_cadastro_matricula()
        janelaHome.hide()


    
    # Quando janela for fechada;
    if window == janelaLogin and event == janelas.WIN_CLOSED:
        break
    if window == janelaHome and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadAluno and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadFuncionario and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadCurso and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadDisciplina and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadTurno and event == janelas.WIN_CLOSED:
        break
    if window == janelaCadMatricula and event == janelas.WIN_CLOSED:
        break


    # Quando queremos voltar para janela de home;
    if window == janelaCadAluno and event == "Voltar":
        janelaCadAluno.hide()
        janelaHome.un_hide()  
    
    if window == janelaCadFuncionario and event == "Voltar":
        janelaCadFuncionario.hide()
        janelaHome.un_hide() 
         
    if window == janelaCadDisciplina and event == "Voltar":
        janelaCadDisciplina.hide()
        janelaHome.un_hide()   
        
    if window == janelaCadCurso and event == "Voltar":
        janelaCadCurso.hide()
        janelaHome.un_hide()  
    
    if window == janelaCadTurno and event == "Voltar":
        janelaCadTurno.hide()
        janelaHome.un_hide()  
    
    if window == janelaCadMatricula and event == "Voltar":
        janelaCadMatricula.hide()
        janelaHome.un_hide()     


    # Realizar cadastro de aluno
    if window == janelaCadAluno and event == "Salvar":
        nome= str(values['nome']).upper()
        email = str(values['email'])
        telefone = str(values['telefone'])
        cep = str(values['cep'])
        cpf = str(values['cpf'])

        
        comando = f'INSERT INTO TB_ALUNO (NOME_ALUNO, EMAIL, TELEFONE, CEP, CPF) VALUES ("{nome}", "{email}", "{telefone}", "{cep}", "{cpf}")'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Aluno cadastrado realizada com sucesso!')
    #Realizar cadastro de funcionários
    if window == janelaCadFuncionario and event == "Salvar":
        nome= str(values['nome']).upper()
        email = str(values['email'])
        telefone = str(values['telefone'])
        cep = str(values['cep'])
        cpf = str(values['cpf'])
        senha = str(values['senha'])
 
        
        comando = f'INSERT INTO TB_FUNCIONARIOS (NOME_FUNCIONARIO, EMAIL, TELEFONE, CEP, CPF, SENHA) VALUES ("{nome}", "{email}", "{telefone}", "{cep}", "{cpf}", "{senha}")'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Funcionario cadastrado realizada com sucesso!')
    #Realizar cadastro de disciplina
    if window == janelaCadDisciplina and event == "Salvar":
        disciplina = str(values['disciplina']).upper()
         
        
        comando = f'INSERT INTO TB_DISCIPLINA (NOME_DISCIPLINA) VALUES ("{disciplina}")'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Diciplina cadastrado realizada com sucesso!')
    #Realizar cadastro de curso
    if window == janelaCadCurso and event == "Salvar":
        curso = str(values['curso']).upper()
        cghr = str(values['cghr'])
        
     
        comando = f'INSERT INTO TB_CURSO (NOME_CURSO, CARGA_HORARIA) VALUES ("{curso}", "{cghr}")'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Curso cadastrado realizada com sucesso!')
    #Realizar cadastro de turno
    if window == janelaCadTurno and event == "Salvar":
        turno = str(values['turno']).upper()
        cghr = str(values['cghr'])
        
        
        comando = f'INSERT INTO TB_TURNO (NOME_TURNO, HORARIO_TURNO) VALUES ("{turno}", "{cghr}")'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Turno cadastrado realizada com sucesso!')
    #Realizar cadastro de matricula
    if window == janelaCadMatricula and event == "Salvar":
        cpf = str(values['CPF'])
        curso = str(values['cursos'])
        disciplina = str(values['Diciplina'])
        turno = str(values['Turno'])


        #Recupera id_curso 
        def ID_curso(id_cursos):
            comando = f'SELECT ID_CURSO FROM TB_CURSO WHERE NOME_CURSO = "{id_cursos}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            cursos = []
            cursos_solo = int

            for curso in resultado[0:len(resultado)]:
                cursos.append(curso)

            for curso in cursos:
                index_curso = cursos.index(curso)
                curso_tratado = cursos[index_curso]
                cursos_solo = curso_tratado[0]
                
            
            return cursos_solo
        #Recupera id_disciplina
        def ID_disciplina(id_disciplina):
            comando = f'SELECT ID_DISCIPLINA FROM TB_DISCIPLINA WHERE NOME_DISCIPLINA = "{id_disciplina}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            diciplinas = []
            diciplinas_solo = int

            for Diciplinas in resultado[0:len(resultado)]:
                diciplinas.append(Diciplinas)

            for Diciplinas in diciplinas:
                index_Diciplinas = diciplinas.index(Diciplinas)
                Diciplinas_tratado = diciplinas[index_Diciplinas]
                diciplinas_solo = Diciplinas_tratado[0]
                
            
            return  diciplinas_solo
        #Recupera id_turno
        def ID_turno(id_turno):
            comando = f'SELECT ID_TURNO FROM TB_TURNO WHERE NOME_TURNO = "{id_turno}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            turnos = []
            turnos_solo = int

            for Turnos in resultado[0:len(resultado)]:
                turnos.append(Turnos)

            for Turnos in turnos:
                index_Turnos = turnos.index(Turnos)
                Turnos_tratado = turnos[index_Turnos]
                turnos_solo = Turnos_tratado[0]
                
            
            return  turnos_solo

 

        comando = f'INSERT INTO TB_MATRICULA (FK_CPF_ALUNO, FK_ID_CURSO, FK_ID_DISCIPLINA, FK_ID_TURNO ) VALUES ("{cpf}", {ID_curso(curso)}, {ID_disciplina(disciplina)}, {ID_turno(turno)})'
        cursor.execute(comando)
        conexao.commit()

        janelas.popup('Matricula realizada com sucesso!')
        