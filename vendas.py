import csv

def read_csv(filename):
    sales = []
    with open (filename, newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file)
        next(reader)
        
        for line in reader:
            produto, quantidade, preco_unitario = line
            
            sales.append({
                'produto': produto,
                'quantidade': int(quantidade),
                'preco_unitario': float(preco_unitario)
            })
    return sales

def total_sales(sales):
    
    totais = {}
    total_geral = 0
    maior_quantidade = 0
    mais_vendido = ''
    
    for sale in sales:
        produto = sale['produto']
        quantidade = sale['quantidade']
        preco_unitario = sale['preco_unitario']
        #Total por venda
        total_venda = quantidade * preco_unitario
        
        if produto not in totais:
            totais[produto] = {'quantidade': 0, 'total': 0.0}
            
        totais[produto]['quantidade'] += quantidade
        #Total por produto
        totais[produto]['total'] += total_venda
        #Total geral
        total_geral += total_venda

        for produto, dados in totais.items():
            if dados['quantidade'] > maior_quantidade:
                maior_quantidade = dados['quantidade']
                mais_vendido = produto
                
    return totais, total_geral, mais_vendido
                
def exibir_relatorio(totais, total_geral, mais_vendido):
    print("Relatório de vendas\n")
    print(f"{'Produto':<10} {'Quantidade':<10} {'Valor Total'}")
    print("-" * 43)
    
    for produto, dados in totais.items():
        quantidade = dados['quantidade']
        total = dados['total']
        print(f"{produto:<10} {quantidade:<10} R$ {total:.2f}")
    
    print(f"\nProduto mais vendido: {mais_vendido}")
    print(f"Total geral: R$ {total_geral:.2f}")
    
sales = read_csv("vendas.csv")
totais, total_geral, mais_vendido = total_sales(sales)
exibir_relatorio(totais=totais, mais_vendido=mais_vendido, total_geral=total_geral)
