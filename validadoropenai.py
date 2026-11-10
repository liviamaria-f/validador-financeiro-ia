import csv
import sys
INTERACTIVE_MODE = True
from openai import OpenAI

import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def converter_valor(texto):
    if texto == "":
        return None
    texto = texto.strip().replace("R$","").replace(" ","")
    texto = texto.replace(".","").replace(",",".")
    try:
        return float(texto)
    except ValueError:
        return None

def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace(",","X").replace(".",",").replace("X",".")

def validar_registro(linha, numero_linha):
    erros = []

    if len(linha) < 2:
        erros.append(f"Linha {numero_linha}: registro incompleto")
        return erros

    descricao = linha[0].strip()
    valor_texto = linha[1].strip()

    if descricao == "":
        erros.append(f"Linha {numero_linha}: descrição vazia")

    if valor_texto == "":
        erros.append(f"Linha {numero_linha}: valor vazio")
        return erros

    numero = converter_valor(valor_texto)
    if numero is None:
        erros.append(f"Linha {numero_linha}: valor inválido -> '{valor_texto}'")
        return erros

    if numero < 0:
        if INTERACTIVE_MODE:
            resposta = input(f"Linha {numero_linha}: '{descricao}' tem valor negativo ({formatar_moeda(numero)}). É intencional? s/n: ").strip().lower()
            if resposta != "s":
                erros.append(f"Linha {numero_linha}: valor negativo não confirmado -> '{valor_texto}'")
        else:
            erros.append(f"Linha {numero_linha}: valor negativo -> '{valor_texto}'")

    return erros

def ler_csv(caminho):
    linhas = []
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            linhas.append(linha)
    return linhas
def ler_digitado():
    print("Digite registros no formato: descriçåo, valor: ")
    linhas = []
    while True:
        entrada = input("> ").strip()
        if entrada == "":
            break
        linhas.append(entrada.split(","))
    return linhas

def main():
    if len(sys.argv) == 2:
        linhas = ler_csv(sys.argv[1])
    else:
        linhas = ler_digitado()

    todos_erros = []
    
    for i, linha in enumerate(linhas, start=1):
        if i == 1 and linha[0].lower() in ("descricao", "descrição"):
            continue

        erros_da_linha = validar_registro(linha, i)
        todos_erros.extend(erros_da_linha)

    print("\n--- Relatório de Validação ---")
    if not todos_erros:
        print("Nenhuma inconsistência encontrada. Dados válidos!")
    else:
        for erro in todos_erros:
            print(erro)
        print(f"\nTotal de inconsistências: {len(todos_erros)}")
        print("\n--- Explicação da IA ---")
        explicacao = explicar_erros(todos_erros)
        print(explicacao)

def explicar_erros(lista_de_erros):
    prompt = f"""
    Você é um assistente financeiro. O usuário tem um CSV com os seguintes problemas:
    {lista_de_erros}
    Explique em português simples o que cada problema significa e como corrigir.
    """
    resposta = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
    return resposta.choices[0].message.content

    try:
        resposta = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Não foi possível gerar a explicação da IA: {e}"

if __name__ == "__main__":
    main()
        
    
