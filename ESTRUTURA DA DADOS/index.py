from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela
from queue import Queue
from datetime import datetime


contatos = []
mensagem = Queue()
busca_nome_global = ""
cont= 0
# FUNÇÕES
def AdicionarContato():
 
    # ESCREVER LÓGICA AQUI!
    global contatos
    nome = input("Digite o nome: ")
    numero = int(input("Digite o número: "))
    usuario_existe = False
    novo_usuario = {
        "nome": nome,
        "numero": numero
        
    }

    if len(contatos) >0:
        for contato in contatos:
            # verifica se o novo contato já está na base de dados
            if  contato == novo_usuario:
                usuario_existe = True
                print("Contato já foi cadastrado na base de dados anteriormente.")
                break
            else:
                usuario_existe = False

        if usuario_existe == False:
            contatos.append(novo_usuario)
            print("Usuário Criado com Sucesso!")
        
    else:
        # base de dados vazia, então adiciona o primeiro elemento
        contatos.append(novo_usuario)
        print("Usuário Criado com Sucesso!")
    
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI
    print(contatos)
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    usuario_encontrado = False
    usario_que_sera_editado = {}
   
    busca_nome = input("Digite o Nome do contato que você deseja alterar: ")
    # varre a lista para procurar se o contato existe
    for contato in contatos:
        if busca_nome == contato["nome"]:
            usuario_encontrado = True
            usario_que_sera_editado = contato
            break

    if usuario_encontrado == True:
        #encontramos o usuario
        escolha = int(input("Digite 1 pra editar nome 2 para editar o número: "))

        if escolha == 1:
            novo_nome = input("Digite um novo nome: ")
            usario_que_sera_editado["nome"] = novo_nome
            print("Nome Alterado com sucesso!")

        elif escolha == 2: 
                numero_novo = int(input("Atualize aqui o número: "))
                usario_que_sera_editado['numero'] = numero_novo
                print('numero alterado com sucesso!')

    else:
        print('Contato não encontrado')
           
             
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def salvar_mensagem():
    global busca_nome_global
    usuario_encontrado = False
    busca_nome = input("Digite o Nome do contato que você deseja adionar a mensagem: ")
    busca_nome_global = busca_nome
    for contato in contatos:
        if busca_nome == contato["nome"]:
            usuario_encontrado = True
            break
    if usuario_encontrado == True:

        elemento = input("Digite a mensagem que deseja adicionar à fila: ")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem.put([elemento, data_hora, busca_nome])
        print("Elemento foi adicionado à fila, você já consegue ve a sua mensagem, ela é a última! ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        for elemento in list(mensagem.queue):
            print(elemento)
        print("Quantidade de mensagem na fila: ",(mensagem.qsize()))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        input("Aperte enter para continuar")

        return True

    elif usuario_encontrado == False:
        print("O usuário que você digitou não existe, tente novamente ")
        input("Aperte enter para continuar")

        return False

def imprimir_mensagem():
    print("Mensagem na fila:\n")
    for elemento in list(mensagem.queue):
            print(elemento)
    print("Existe um total de",mensagem.qsize(),"Mesangens na fila")
    print("\nMensagem impressa.")
    input("[APERTE ENTER PARA CONTINUAR]")

def Enviarmensagem():
    
    if not mensagem.empty() == True:

        usuario_encontrado = False
        for contato in contatos:
            if busca_nome_global == contato["nome"]:
                usuario_encontrado = True
                break

        if usuario_encontrado == True:
            print("Mensagens da fila: \n")
            for elemento in list(mensagem.queue):
                print(elemento,"\n")
            escolha = input("Você deseja enviar a primeira mensagem S/N: ").upper()
            msg = []
            if escolha == "S":        
                msg_excluida = mensagem.get()
                msg.append(msg_excluida)

                if "mensagem" in contato:
                    contato["mensagem"].append(msg)
                    print("Mensagem Enviada com Sucesso!")
                    print("Quantidade de mensagem na fila: ",(mensagem.qsize()))
                    print("Detalhes da mensgem enviada: ", msg_excluida)
                    input("[APERTE ENTER PARA CONTINUAR]") 
                
                else: 
                    contato ["mensagem"] = [msg]   
                    print("Mensagem Enviada com Sucesso!")
                    print("Quantidade de mensagem na fila: ",(mensagem.qsize()))
                    print("Detalhes da mensgem enviada: ", msg_excluida)
                    input("[APERTE ENTER PARA CONTINUAR]")
            else:
                print("OK, sua Mensagem não foi enviada")
                input("[APERTE ENTER PARA CONTINUAR]")
                # Enviarmensagem()
                return
        else:
            print("Mensagem não enviada")
            input("[APERTE ENTER PARA CONTINUAR]")
            Enviarmensagem()
    else:
        print("Você não tem nenhuma mensagem em sua fila")
        print("volte ao menu anterior e cadastre sua mensagem")
        input("digite enter para continuar")
        imprimirMenuPrincipal()

# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

def escrever_mensagem():
    while True:
        limparTela()
        opcao = input("Escolha uma opção:\n 1. escrever mensagem para a fila\n 2. Mostrar mensagens da fila\n 3. Voltar ao menu anterior\nOpção: ")
        if opcao == '1':
            mensagem_foi_salva = salvar_mensagem()
            if mensagem_foi_salva:
                break
        elif opcao == '2':
            imprimir_mensagem()
        elif opcao == '3':
            imprimirMenuPrincipal() 
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            input("[APERTE ENTER PARA CONTINUAR]")
            limparTela()

while not fimPrograma:
    limparTela()
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if opcao in ("0", "1", "2", "3", "4","5"):
        
        if int(opcao) == 1:
            AdicionarContato()
        elif int(opcao) == 2: 
            escrever_mensagem()
        elif int(opcao) == 3:
            MostrarContatos()
        elif int(opcao) == 4:
            EditarContato()
        elif int(opcao) == 5:
            Enviarmensagem()
        elif int(opcao) == 0:
            fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")