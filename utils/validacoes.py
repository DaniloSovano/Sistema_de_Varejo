import time


def validar_opcao(messagem) -> int :
    while True:
        try:
            return int(input(messagem))
        except ValueError:
            print("Opção inválida! Por favor, insira uma opção válida.")
            time.sleep(2)

def confirmar_saida():
    while True:
        sair = validar_opcao("Você tem certeza que quer sair do programa? (1 - Sim, 2 - Não): ")
        
        if sair == 1:
            return True
        elif sair == 2:
            return False