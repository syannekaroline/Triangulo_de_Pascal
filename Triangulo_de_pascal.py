import math
print("{:=^60}".format("Triângulo de Pascal"))
print("\nAlgoritmo gerador do triângulo de pascal e plote o triângulo gerado. Para cada execução do programa, o usuário deve informar o valor de N que corresponde ao número de linhas que terá o triângulo.\n")

#receber o valor de N
N= int(input("Insira o valor do Número de linhas que terá o triângulo(N) : "))

for i in range(1,N+1):
  for k in range(i):
    print(math.comb(i-1,k),"\t",end='')
  print("\n")