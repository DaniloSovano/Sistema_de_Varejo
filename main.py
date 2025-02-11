import os
import time
from modules.financeiro import (
    dados_financeiros, 
    plot_estoque_restante, 
    plot_quantidade_de_vendas_por_produto, 
    print_produtos_maior_menor_lucro,
    print_parecer,
    vendas_por_produto,
    vendas_por_produto_cartesiano
)
from utils.validacoes import validar_opcao, confirmar_saida
#limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n🔹 Pressione ENTER para continuar...")
#função com as opções disponiveis no menu
def menu():
    return '''
    ===== SISTEMA DE GESTÃO VAREJISTA =====

    📊 Relatório financeiro baseado nos últimos 12 meses.

    1️⃣ Dados financeiros 
    2️⃣ Controle de Estoque  
    3️⃣ Análise Financeira  
    4️⃣ Relatório de Vendas  
    5️⃣ Sair  
    '''
#funções do menu de vendas
def menu_vendas():
    opt = ''
    while opt != 5:
        limpar_tela()
        print('''
            ===== RELATÓRIO DE VENDAS =====

    📊 Análise detalhada das vendas e lucratividade dos produtos.

    1️⃣ Produtos mais vendidos  
    2️⃣ Produto com maior e menor lucro  
    3️⃣ Vendas por produto (Gráfico Cartesiano)  
    4️⃣ Vendas por produto (Gráfico de Barras)  
    5️⃣ Voltar  
        ''')
        opt = validar_opcao('👉 Selecione uma opção: ')

        if opt == 1:
            plot_quantidade_de_vendas_por_produto()
            pausar()
        elif opt == 2:
            print_produtos_maior_menor_lucro()
            pausar()
        elif opt == 3:
            vendas_por_produto_cartesiano()
            pausar()
        elif opt == 4:
            vendas_por_produto()
            pausar()
#funções do menu financeiro 
def menu_financeiro():
    opt = ''
    while opt != 4:
        limpar_tela()
        print('''
        ===== RELATÓRIO FINANCEIRO =====

        📊 Análise detalhada das finanças.

        1️⃣ Lucros
        2️⃣ Investimentos e Despesas 
        3️⃣ Total
        4️⃣ Voltar
        ''')
        opt = validar_opcao('👉 Selecione uma opção: ')

        if opt == 1:
            dados_financeiros('lucros') 
            pausar()
        elif opt == 2:
            dados_financeiros('investimentos')
            pausar()
        elif opt == 3:
            dados_financeiros('totais')
            pausar()

sair = True
while sair:
    limpar_tela()
    print(menu())
    option = validar_opcao('👉 Selecione uma opção: ')
    try:
        if option == 1:
            menu_financeiro()
        elif option == 2:
            plot_estoque_restante()
            pausar()
        elif option == 3:
            menu_vendas()
        elif option == 4:
            print_parecer()
            pausar()
        elif option == 5:
            if confirmar_saida():
                print("Saindo....")
                time.sleep(2)
                sair = False
    except KeyboardInterrupt:
        print("\nVocê não pode interromper o programa pelo teclado. Para sair, escolha a opção 5.")
        pausar()
        continue
