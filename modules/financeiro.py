import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
# Adiciona o diretório superior ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.data import data  # Importa a variável "data" do arquivo "database.py"
from utils.meses import meses




def plot_estoque_restante():
    # Converter colunas para valores numéricos
    data['QUANT'] = pd.to_numeric(data['QUANT'], errors='coerce').fillna(0)
    for mes in meses:
        data[mes] = pd.to_numeric(data[mes], errors='coerce').fillna(0)

    # 📉 **Calcular o estoque restante**
    data['ESTOQUE_FINAL'] = data['QUANT'] - data[meses].sum(axis=1)

    # 📊 Criar gráfico de barras
    plt.figure(figsize=(12, 6))  # Tamanho da figura
    plt.bar(data['PROD'], data['ESTOQUE_FINAL'], color='skyblue')

    # Personalização do gráfico
    plt.xlabel("Produtos")  # Nome do eixo X
    plt.ylabel("Estoque Restante")  # Nome do eixo Y
    plt.title("Estoque Final de Cada Produto após 12 Meses")  # Título do gráfico
    plt.xticks(rotation=45)  # Rotacionar nomes dos produtos
    plt.grid(axis='y', linestyle="--", alpha=0.7)  # Adicionar grade horizontal

    # Exibir gráfico
    plt.show()

def dados_financeiros(opt:str):
    # Calcular o total investido, vendido e lucro/prejuízo
    total_investido = 0
    total_vendido = 0
    total_lucro = 0

    for index, row in data.iterrows():
        vc = row['VC']  # Custo unitário
        vv = row['VV']  # Valor de venda unitário
        
        for mes in meses:
            quant_vendida = row[mes]  # Quantidade vendida no mês
            total_investido += vc * quant_vendida  # Custo total
            total_vendido += vv * quant_vendida  # Receita total

    # Lucro total = Receita total - Custo total
    total_lucro = total_vendido - total_investido

    data['Total Investido'] = data.apply(lambda row: row['VC'] * row[meses].sum(), axis=1)
    data['Total Vendido'] = data.apply(lambda row: row['VV'] * row[meses].sum(), axis=1)
    data['Lucro'] = data['Total Vendido'] - data['Total Investido']

    if opt == 'lucros':
        print('Produtos e seus lucros')
        print(data[['PROD' ,'Lucro']])
    elif opt == 'investimentos':
        print('Produtos e seus investimentos e vendas')
        print(data[['PROD' ,'Total Investido','Total Vendido']])
    elif opt == 'totais':
         # Exibir os resultados
        print(f"Total Investido: R$ {total_investido:.2f}")
        print(f"Total Vendido: R$ {total_vendido:.2f}")
        if total_lucro >= 0:
            print(f"Lucro Total: R$ {total_lucro:.2f}")
        else:
            print(f"Prejuízo Total: R$ {-total_lucro:.2f}")

def plot_quantidade_de_vendas_por_produto():
    global data
    # Calcular a quantidade total vendida de cada produto após 12 meses
    data['Total Vendido'] = data[meses].sum(axis=1)

    # Ordenar os produtos pela quantidade total vendida (opcional)
    data = data.sort_values(by='Total Vendido', ascending=False)

    # Plotar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(data['PROD'], data['Total Vendido'], color='skyblue')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade Total Vendida')
    plt.title('Quantidade de Vendas de Cada Produto após 12 Meses')
    plt.xticks(rotation=45, ha='right')  # Rotacionar os nomes dos produtos para melhor visualização
    plt.tight_layout()  # Ajustar layout para evitar cortes
    plt.show()


def print_parecer():
    total_investido = (data['VC'] * data[meses].sum(axis=1)).sum()
    total_vendido = (data['VV'] * data[meses].sum(axis=1)).sum()
    lucro_total = total_vendido - total_investido
    margem_lucro = (lucro_total / total_vendido) * 100

    # Calcular a distribuição das vendas por produto
    data['Total Vendido por Produto'] = data[meses].sum(axis=1)
    distribuicao_vendas = data[['PROD', 'Total Vendido por Produto']].sort_values(by='Total Vendido por Produto', ascending=False)

    # Gerar o parecer
    parecer = f"""
    === Parecer sobre a Saúde Financeira da Empresa ===

    1. Total Investido: R$ {total_investido:.2f}
    2. Total Vendido: R$ {total_vendido:.2f}
    3. Lucro Total: R$ {lucro_total:.2f}
    4. Margem de Lucro: {margem_lucro:.2f}%

    Análise:
    """

    if lucro_total > 0:
        parecer += "A empresa está operando com LUCRO.\n"
        if margem_lucro > 10:
            parecer += "A margem de lucro é SAUDÁVEL, indicando boa eficiência na conversão de vendas em lucro.\n"
        else:
            parecer += "A margem de lucro é BAIXA, sugerindo que a empresa pode estar com custos elevados ou preços de venda insuficientes.\n"
    else:
        parecer += "A empresa está operando com PREJUÍZO. É necessário revisar urgentemente os custos e estratégias de vendas.\n"

    parecer += "\nDistribuição das Vendas por Produto:\n"
    for index, row in distribuicao_vendas.iterrows():
        parecer += f"- {row['PROD']}: {row['Total Vendido por Produto']} unidades vendidas\n"

    parecer += "\nRecomendações:\n"
    if lucro_total > 0 and margem_lucro > 10:
        parecer += "- Focar em produtos com maior margem de lucro.\n- Expandir as vendas dos produtos mais rentáveis.\n- Manter o controle de custos.\n"
    elif lucro_total > 0 and margem_lucro <= 10:
        parecer += "- Revisar custos para identificar oportunidades de redução.\n- Aumentar preços de venda, se possível.\n- Focar em produtos com maior margem de lucro.\n"
    else:
        parecer += "- Revisar urgentemente os custos e identificar os maiores gastos.\n- Avaliar a possibilidade de aumentar os preços de venda.\n- Descontinuar produtos que não geram lucro.\n"

    # Exibir o parecer
    print(parecer)

def print_produtos_maior_menor_lucro():
        for mes in meses:
            data[mes] = pd.to_numeric(data[mes], errors='coerce').fillna(0)

    # 📊 **Calcular lucro total de cada produto**
        data['LUCRO_TOTAL'] = (data['VV'] - data['VC']) * data[meses].sum(axis=1)

    # 🔥 **Encontrar produtos com maior e menor lucro**
        produto_mais_lucrativo = data.loc[data['LUCRO_TOTAL'].idxmax(), ['PROD', 'LUCRO_TOTAL']]
        produto_menos_lucrativo = data.loc[data['LUCRO_TOTAL'].idxmin(), ['PROD', 'LUCRO_TOTAL']]
    # Exibir resultados formatados
        print(f"📈 Produto com MAIOR lucro: {produto_mais_lucrativo['PROD']} - Lucro Total: R$ {produto_mais_lucrativo['LUCRO_TOTAL']:.2f}")
        print(f"📉 Produto com MENOR lucro: {produto_menos_lucrativo['PROD']} - Lucro Total: R$ {produto_menos_lucrativo['LUCRO_TOTAL']:.2f}")

def vendas_por_produto_cartesiano():
    for mes in meses:
        data[mes] = pd.to_numeric(data[mes], errors='coerce').fillna(0)

# 📊 Criar gráfico

    plt.figure(figsize=(12, 6))  # Tamanho da figura

# Percorrer cada produto e plotar sua quantidade vendida ao longo dos meses
    for index, row in data.iterrows():
        plt.plot(meses, row[meses], marker='o', linestyle='-', label=row['PROD'])

    # Personalização do gráfico
    plt.xlabel("Meses")  # Nome do eixo X
    plt.ylabel("Quantidade Vendida")  # Nome do eixo Y
    plt.title("Quantidade de Produtos Vendidos por Mês")  # Título do gráfico
    plt.xticks(rotation=45)  # Rotacionar meses para melhor visualização
    plt.grid(True, linestyle="--", alpha=0.7)  # Adicionar grade pontilhada
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Legenda dos produtos

    # Exibir gráfico
    plt.show()

def vendas_por_produto():
    global data
    data['Total Vendido'] = data[meses].sum(axis=1)

    # Ordenar os produtos pela quantidade total vendida (opcional)
    data = data.sort_values(by='Total Vendido', ascending=False)

    # Plotar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(data['PROD'], data['Total Vendido'], color='skyblue')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade Total Vendida')
    plt.title('Quantidade de Vendas de Cada Produto após 12 Meses')
    plt.xticks(rotation=45, ha='right')  # Rotacionar os nomes dos produtos para melhor visualização
    plt.tight_layout()  # Ajustar layout para evitar cortes
    plt.show()