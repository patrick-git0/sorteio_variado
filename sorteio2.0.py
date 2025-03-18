import random

def sorteio():
    print("### SORTEIO ###")
    participantes = []

    # Coleta os nomes dos participantes
    while True:
        nome = input("Digite o nome do participante (ou pressione Enter para finalizar): ").strip()
        if nome == "":
            break
        participantes.append(nome)

    if not participantes:
        print("Nenhum participante cadastrado. Sorteio cancelado!")
        return

    # Pergunta quantos vencedores serão sorteados
    while True:
        try:
            qtd_vencedores = int(input("Quantos vencedores deseja sortear? "))
            if qtd_vencedores < 1:
                print("Deve ser pelo menos 1 vencedor!")
            elif qtd_vencedores > len(participantes):
                print("Número de vencedores não pode ser maior que o número de participantes!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Realiza o sorteio sem repetir participantes
    vencedores = random.sample(participantes, qtd_vencedores)
    
    # Exibe os vencedores
    print("\n🎉 Os vencedores do sorteio são: 🎉")
    for vencedor in vencedores:
        print(" -", vencedor)

if __name__ == "__main__":
    sorteio()
