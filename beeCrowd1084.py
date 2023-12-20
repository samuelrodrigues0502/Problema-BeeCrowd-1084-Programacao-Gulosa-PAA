def geraNovoNum(lenNum, qtdNumApagados, num):
    pilhaNum = []

    for i in num:
        # Verifica se o topo da pilha (caso não esteja vazia)
        # é menor que o algarismo atual do número
        while len(pilhaNum) > 0 and i > pilhaNum[-1] and qtdNumApagados != 0:
            # Caso ainda haja números pra apagar, o topo da pilha é removido
            pilhaNum.pop()
            qtdNumApagados = qtdNumApagados - 1
        pilhaNum.append(i)
    # Circunstância onde não foram apagados todos os números
    # Ex: 7 4 -> 1000000
    # Ao decorrer do laço, 0 nunca vai ser maior que 0, então
    # não haverá remoção dos números da pilha
    while qtdNumApagados != 0:
        pilhaNum.pop()
        qtdNumApagados = qtdNumApagados - 1

    strNew = ''.join(pilhaNum)

    print(strNew)

while(True):
    
    string1, string2 = map(int, input().split())
    if string1 == string2 == 0:
        break
    string3 = input()
    geraNovoNum(string1, string2, string3)

