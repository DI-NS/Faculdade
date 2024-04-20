from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela





contatos = []

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

def EscreverMensagem():
    # Exemplo de criação de uma mensagem

    usuario_encontrado = False
    busca_nome = input("Digite o Nome do contato que você deseja adionar a mensagem: ")

    # varre a lista para procurar se o contato existe
    for contato in contatos:
        if busca_nome == contato["nome"]:
            usuario_encontrado = True
            break

    if usuario_encontrado == True:
        msg = input("digite aqui sua mensagem: ")
        if "mensagem" in contato:
            contato["mensagem"].append(msg)   
        
        else: 
            contato ["mensagem"] = [msg]    
        print("Mensagem Criada com Sucesso!") 
    else:
        print("Usuário não encontrado")
    
    # destinatario = Contato("Contato para envio", "Numero para envio")
    # mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if opcao in ("0", "1", "2", "3", "4"):
        
        if int(opcao) == 1:
            AdicionarContato()
        elif int(opcao) == 2:
            MostrarContatos()
        elif int(opcao) == 3:
            EditarContato()
        elif int(opcao) == 4:
            EscreverMensagem()
        elif int(opcao) == 0:
            fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")