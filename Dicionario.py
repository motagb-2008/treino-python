
def main():
    dicionario = {}
    frase = input("insira uma frase:\n").lower()
    verifica_dicionario(dicionario, frase)
    exibe_dicionario (dicionario)

def verifica_dicionario(dicionario,frase):
    cont = 1

   # for para percorrer cada palavra da frase
    for palavra in frase.split():

        #verificar se uma palavra aparece mais de uma vez
        if palavra not in dicionario:
            dicionario [palavra] = 1
            
        else:
            dicionario [palavra] += cont 

def exibe_dicionario (meu_dicionario):
    print ("---------DICIONARIO--------")
    print ("Palavras:     Qtd de vezes usadas:\n ---------------------------------")
    for termos , contagem in sorted(meu_dicionario.items()):
         print(f"{termos:<9} |    {contagem}")

main()         
      