import json

def main ():
    Biblioteca = carrega_arquivo()  # carrega os contatos salvos (ou {} se não existir)
    Exibe_tela ()
    alternativa = input("Escolha uma opçao: ")
    while True:
        match alternativa:
           
            case "1":
                Adiciona_contato(Biblioteca) 
                salva_contatos(Biblioteca) 

            case "2":
                 Lista_contato(Biblioteca)
                    
            case "3":
                Busca_nome(Biblioteca)
                    
            case "4":
                 Remove_contato(Biblioteca)
                 salva_contatos(Biblioteca)

            case "0":
                print ("Programa encerrado!")
                break     

            case _ :
                print ("Valor invalido!")     
            
        
       
        Exibe_tela ()
        alternativa = input("Escolha uma opçao: ")
    
                        

def Exibe_tela ():   
    print ("\n===== AGENDA =====") 
    print ("1 - Adicionar contato \n2 - Listar contatos\n3 - Buscar por nome\n4 - Remover contato\n0 - Sair")

def Adiciona_contato(biblioteca_nome):

    while True:
        nome = input("Nome do contato: ")
        if len(nome)>0:
           break
        print ("Insira um nome valido!")    
            
    tel = input("Insira seu numero de celular(sem espaçamento) com o DDD:")
    while True:
        if (tel.isdigit()) and (len(tel) == 11) :
            print ("Numero de telefone verificado")
            
            break
        else:
            print("Insira um numero de telefone valido")
            tel = input("Insira seu numero de celular(sem espaçamento) com DDD:")
    
    if nome in biblioteca_nome:
        print("Contato atualizado!\n")
    else:
         print ("Contato registrado!\n")
    biblioteca_nome [nome] = tel


    
def Lista_contato(contatos_adicionados):
    print("\n-----LISTA DE CONTATOS-------\n")
    for nome , tel in contatos_adicionados.items():
        print (f"Nome: {nome:<5} |   Telefone: {tel}")

def Busca_nome (procura_biblio):
    print ("\n--------BUSCA---------\n")
    search = input ("Insira o nome do contato: ")
    flag = False
    for nome , tel in procura_biblio.items():
        if (search == nome):
            print(f"Contato '{nome}' encontrado!")
            print (f"Nome: {nome:<5} |   Telefone: {tel}")
            flag = True
                  
    if not flag:
        print("Contato nao encontrado!")     

def Remove_contato(biblioteca):
    print ("\n------Exclusao de contatos------\n")
    delete = input("Insira o contato que deseja excluir: ")
    if delete in biblioteca:
        del biblioteca[delete]
        print (f"O contato '{delete}' foi removido dos seus contatos")
    else:
        print ("Contato nao encontrado!")    

def salva_contatos (agenda):
    with open("contatos.json","w", encoding="utf-8" ) as arquivo:
        json.dump(agenda, arquivo,indent=4, ensure_ascii=False)  

def carrega_arquivo():
    try: 
        with open("contatos.json", "r", encoding="utf-8" ) as arquivo:
            return json.load(arquivo) 
    except FileNotFoundError:
        return{}

main()    