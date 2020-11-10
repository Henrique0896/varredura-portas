
from socket import gethostbyname, socket, AF_INET, SOCK_STREAM
from os import system

# ENTRADA DO IP
#O usuario ira passar um IP ou um link para que seja feita a varredura
#O metodo gethostbyname vai retornar o IP caso seja digitado um link
#gethostbyname retorna o proprio IP se o usuario digitar um valido, se nao, ele lanca uma excecao 
try:
    system('clear')
    print("Programa de varredura de portas abertas!")
    dispositivo = input("Digite o IP/Dominio do host que deseja realizar a varredura: ")
    ip = gethostbyname(dispositivo)
    system('clear')
except:
    print('Erro! Verifique e tente novamente!')
    exit()
#Se estiver tudo ok, teremos um IP valido salvo na variavel 'ip'


# ENTRADA DO INTERVALO DE PORTAS
#O usuario vai digitar o intervalo de portas para a varredura
#Caso ele nao digite um numero inteiro, sera lancada uma excecao
#Caso ele digite numeros fora do intervalo esperado, sera lancada uma excecao tambem
try:
    print("\nDigite o intervalo de portas que vai ser coberto:")
    portaInicial = int(input("Porta Inicial: "))
    portaFinal = int(input("Porta Final: "))
    if(portaInicial > portaFinal or portaInicial < 0 or portaFinal > 65635):
        raise Exception
    system('clear')
except:
    print('Erro! Verifique e tente novamente!')
    exit()
#Se tudo estiver ok, agora temos o ip e um intervalo para fazer a varredura


# REALIZACAO DA VARREDURA
#E criado um laco para percorrer todo o intervalo escolhido
#A variavel 'sock' recebe um novo socket com a familia de enderecos 'AF_INET' (Padrao)
#O tipo de socket tambem sera o Padrao 'SOCK_STREAM'
#A variavel 'res' contera a resposta da conexao ao socket com o endereco (IP e Porta)
#Se a porta estiver aberta o metodo 'sock.connect_ex' retornara '0'
try:
    print("Varredura em andamento...")
    portasAbertas = []
    for i in range(portaInicial, portaFinal+1):
        print("Verificando porta: %d" %(i))
        sock = socket(AF_INET, SOCK_STREAM)
        res = sock.connect_ex((ip,  i))
        if (res == 0):
            portasAbertas.append(i)
        system('clear')
    print("Varredura encerrada!\n")
except:
      print('Erro! Verifique e tente novamente')

#Imprimindo as portas
print("O host: %s " %(dispositivo))
print("Possui: %d porta(s) aberta(s)" %(len(portasAbertas)))
print("No intervalo %d - %d" %(portaInicial, portaFinal))

if( len(portasAbertas) > 0):
    print("\nLista de Portas Abertas:")
    for i in range( len(portasAbertas) ):
        print(portasAbertas[i])
print("\n")