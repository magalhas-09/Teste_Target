import json

# Função para processar o faturamento
def processar_faturamento(faturamento_diario):
    # Filtrando os dias sem faturamento
    dias_com_faturamento = [f for f in faturamento_diario if f > 0]

    # Calculando o menor e maior faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    # Calculando a média de faturamento
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contando os dias em que o faturamento foi superior à média
    dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_faturamento)

    # Retornando os resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Função principal para carregar os dados do JSON e processar o faturamento
def main():
    try:
        # Abrindo e carregando o arquivo JSON
        with open('c:/temp/ws-eclipse/TesteTarget/src/aplicacoes/Faturamento.py', 'r') as file:
            dados = json.load(file)
        
        # Obtendo o vetor de faturamento diário
        faturamento_diario = dados.get('faturamento_diario', [])

        if not faturamento_diario:
            raise ValueError("Arquivo JSON não contém dados de faturamento diário.")

        # Processando os dados
        menor, maior, dias_acima_media = processar_faturamento(faturamento_diario)

        # Exibindo os resultados
        print(f"Menor valor de faturamento: R$ {menor:.2f}")
        print(f"Maior valor de faturamento: R$ {maior:.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
    except ValueError as e:
        print(e)

# Executando o programa
if __name__ == '__main__':
    main()
