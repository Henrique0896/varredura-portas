
from socket import gethostbyname, socket, AF_INET, SOCK_STREAM

#Executa caso o programa receba um dado inesperado
def erroEntrada():
    print("\nEntrada inválida!\n")
    exit()


# ENTRADA DO IP
#O usúario irá passar um IP ou um link para que seja feita a varredura
#O método gethostbyname vai retornar o IP caso seja digitado um link
#gethostbyname retorna o próprio IP se o usuário digitar um válido, se não, ele lança uma exceção 
print(" \n\tPrograma de varredura de portas abertas!")
try:
    dispositivo = input("Digite o IP/Domínio do host que deseja realizar a varredura: ")
    ip = gethostbyname(dispositivo)
except:
    erroEntrada()
#Se estiver tudo ok, teremos um IP válido salvo na variável 'ip'


# ENTRADA DO INTERVALO DE PORTAS
#O usúario vai digitar o intervalo de portas para a varredura
#Caso ele não digite um número inteiro, será lançada uma exceção
#Caso ele digite números fora do intervalo esperado, será lançada uma exceção também
try:
    print("\nDigite o intervalo de portas que vai ser coberto:")
    portaInicial = int(input("Porta Inicial: "))
    portaFinal = int(input("Porta Final: "))
    if(portaInicial > portaFinal or portaInicial < 0 or portaFinal > 65635):
        raise Exception
except:
    erroEntrada()
#Se tudo estiver ok, agora temos o ip e um intervalo para fazer a varredura


# REALIZAÇÃO DA VARREDURA
#É criado um laço para percorrer todo o intervalo escolhido
#A variável 'sock' recebe um novo socket com a família de endereços 'AF_INET' (Padrão)
#O tipo de socket também é o Padrão 'SOCK_STREAM'
#A variável 'res' conterá a resposta da conexão ao socket com o endereço (IP e Porta)
#Se a porta estiver aberta o método 'sock.connect_ex' retornará '0'
try:
    print("\nPORTA           STATUS")
    for i in range(portaInicial, portaFinal+1):
        sock = socket(AF_INET, SOCK_STREAM)
        res = sock.connect_ex((ip,  i))
        if (res == 0):
            print(" %d      ->     ABERTA" %(i))
        else:
            print(" %d      ->     fechada" %(i))
    print("\nVarredura encerrada!\n")
except:
    print("Erro inesperado ao realizar a varredura")