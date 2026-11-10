# Validador Financeiro com Inteligência Artificial 🤖💰

Este projeto une a rotina contábil à Inteligência Artificial. Ele lê e valida arquivos de dados financeiros (CSV/TXT) e, para facilitar a vida de quem não é técnico, utiliza a API da OpenAI para **explicar as inconsistências encontradas em linguagem natural**.

## 🎯 O Problema
Em rotinas de fechamento contábil e conciliação bancária, é comum receber planilhas com inconsistências. Validadores tradicionais apenas exibem códigos de erro frios (ex: `Linha 2: valor inválido -> 'abc'`). Isso gera retrabalho, pois o profissional precisa interpretar o erro técnico antes de corrigir o dado.

## 💡 A Solução
O script faz duas coisas:
1. **Validação:** Checa formatos, campos vazios e valores negativos indevidos no arquivo CSV/TXT.
2. **Explicação com IA:** Se encontrar erros, envia a lista de inconsistências para a API da OpenAI (modelo `gpt-4o-mini`), que atua como um assistente financeiro, gerando um relatório amigável explicando *o que* está errado e *como* corrigir.

## 🚀 Como executar o projeto

### Pré-requisitos
* Python 3.8 ou superior
* Uma chave de API da OpenAI (você pode gerar uma em [platform.openai.com](https://platform.openai.com/))

### Passo a passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/liviamaria-f/validador-financeiro-ia.git
   cd validador-financeiro-ia
   
   2. Crie e ative um ambiente virtual (recomendado):
   bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   
3. Instale as dependências:
   bash
   pip install openai python-dotenv
   
4. Configurando a sua Chave de API (MUITO IMPORTANTE):
   Para manter a segurança, a chave não fica salva no código. Você deve criar o seu próprio arquivo .env a partir do nosso exemplo:
   · Renomeie o arquivo .env.example (que está neste repositório) para .env.
   · Abra o arquivo .env e substitua o texto de exemplo pela sua chave real da OpenAI:
     text
     OPENAI_API_KEY=sk-sua-chave-verdadeira-aqui
   · O arquivo .gitignore já está configurado para impedir que a sua chave vaze no GitHub.
   
 Tecnologias e Conceitos Utilizados
   · Python: Lógica de validação, manipulação de arquivos (I/O) e estruturação de funções.
   · OpenAI API (gpt-4o-mini): Integração com LLM para geração de relatórios em linguagem natural.
   · Prompt Engineering: Criação de um prompt que atua como um "assistente financeiro".
   · Segurança: Uso de variáveis de ambiente (python-dotenv) e tratamento de exceções (try/except).
   
