<div align="center">

# 🐍 Beginner Portfolio

### Uma trilha prática para aprender lógica de programação com Python

**9 projetos · Python puro · Do terminal à arquitetura de aplicações**

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Projetos-9-FFD43B?style=for-the-badge&logo=python&logoColor=306998" alt="9 projetos">
  <img src="https://img.shields.io/badge/Foco-Lógica%20e%20boas%20práticas-2EA44F?style=for-the-badge" alt="Foco em lógica e boas práticas">
</p>

> Uma bateria de projetos para praticar fundamentos de Python de forma progressiva.
> A inspiração pode vir de ferramentas de IA, mas o código é escrito à mão para
> desenvolver raciocínio, autonomia e confiança.

</div>

<br>

## 🧭 Navegação

| Etapa | Projetos | Habilidades principais |
| :---: | :--- | :--- |
| 🌱 **Fundamentos** | [01 Calculadora](#-01--calculadora-de-terminal) · [02 Jogo de adivinhação](#-02--jogo-de-adivinhação) · [03 Agenda](#-03--agenda-de-contatos) | Lógica, funções, coleções e validação |
| 🧰 **Dados e arquivos** | [04 Controle financeiro](#-04--controle-financeiro) · [05 Analisador de texto](#-05--analisador-de-texto) | JSON, CSV, arquivos e manipulação de dados |
| 🏗️ **Orientação a objetos** | [06 Estoque](#-06--sistema-de-estoque) · [07 Banco](#-07--banco-simplificado) | OOP, herança, polimorfismo e persistência |
| ✅ **Qualidade e integração** | [08 Testes](#-08--testes-e-refatoração) · [09 Tarefas CLI](#-09--gerenciador-de-tarefas-cli) | pytest, arquitetura e projeto integrador |

---

## ✨ Sobre esta trilha

Este repositório reúne **9 desafios práticos**, organizados para aumentar a
complexidade aos poucos. Cada projeto apresenta:

- 🎯 um problema realista para resolver;
- 🧠 conceitos de Python para praticar;
- 📋 requisitos objetivos;
- ✅ critérios para saber quando a implementação está pronta;
- 🚀 extras opcionais para ir além;
- 🗺️ um primeiro passo para começar sem travar.

> **Princípio da trilha:** primeiro faça funcionar, depois organize, teste e
> explique as decisões tomadas.

---

## 🌱 Fundamentos

### 🧮 01 · Calculadora de terminal

> Uma calculadora em loop com histórico das operações da sessão.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Recebe dois números e uma operação (`+`, `-`, `*`, `/`, potência ou resto),
exibe o resultado e guarda as últimas contas realizadas.

**Conceitos praticados**

Tipos e conversão · operadores · condicionais · `while` · funções com retorno ·
listas · f-strings

**Requisitos**

- Menu com as opções: calcular, ver histórico, limpar histórico e sair.
- Cada operação deve estar em uma função separada.
- Divisão por zero e entradas inválidas não podem quebrar o programa.
- O histórico deve mostrar as últimas 10 contas numeradas.

**Critérios de aceitação**

O programa só termina quando a opção “sair” é escolhida, entradas incorretas
não geram traceback e não existe código repetido entre as operações.

**Extras**

Usar o último resultado em uma nova conta e formatar números com duas casas
decimais.

**Por onde começar**

Escreva e teste primeiro as funções das operações isoladamente. Só depois monte
o menu.

</details>

### 🎲 02 · Jogo de adivinhação

> Um jogo de tentativas com dicas, níveis de dificuldade e placar.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

O computador sorteia um número e o jogador tenta acertá-lo recebendo dicas de
“maior” ou “menor”.

**Conceitos praticados**

`random` · laços com `break` · dicionários · ordenação · strings · funções

**Requisitos**

- Três níveis com faixas numéricas e limites de tentativas diferentes.
- Placar em um dicionário `{nome: melhor_pontuação}`, exibido em ordem.
- Validação de entrada: nada de letras ou números fora da faixa.
- Perguntar ao jogador se deseja jogar novamente.

**Critérios de aceitação**

A lógica do jogo deve ser separada da lógica de exibição. O placar só deve ser
atualizado quando a pontuação melhorar.

**Extras**

Pontuação considerando tentativas e dificuldade; modo em que o computador tenta
adivinhar o número escolhido pelo jogador.

**Por onde começar**

Monte uma rodada com um número fixo, sem sorteio. Depois adicione níveis e
placar.

</details>

### 📇 03 · Agenda de contatos

> Um CRUD em memória para organizar contatos por categoria.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Cadastra, busca, edita e remove contatos com nome, telefone, e-mail e categoria.

**Conceitos praticados**

Lista de dicionários · funções com parâmetros · list comprehensions · busca e
filtro · ordenação com `key` · tratamento de duplicatas

**Requisitos**

- Validar cadastro: telefone apenas com dígitos e e-mail com `@`.
- Buscar por trecho do nome sem diferenciar maiúsculas de minúsculas.
- Listar por categoria e ordenar por nome.
- Impedir contatos duplicados.

**Critérios de aceitação**

Nenhuma função deve misturar `input` com a lógica de dados. Use funções que
recebem parâmetros, retornam valores e tenha pelo menos duas comprehensions bem
aplicadas.

**Extras**

Exportar a agenda formatada em texto e agrupar contatos por categoria em um
dicionário de listas.

**Por onde começar**

Defina no papel a estrutura de um contato e da agenda antes de escrever as
funções.

</details>

---

## 🧰 Dados e arquivos

### 💰 04 · Controle financeiro

> Receitas, despesas e resumo mensal com persistência em arquivos.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Registra receitas e despesas com data, valor, categoria e descrição, salva os
dados e gera um resumo mensal.

**Conceitos praticados**

JSON e CSV · `datetime` · `try/except/finally` · módulos próprios · agregação
de dados

**Requisitos**

- Persistir dados entre execuções usando JSON como armazenamento principal.
- Exportar o extrato de um mês para CSV.
- Gerar total de receitas, despesas, saldo e gastos por categoria.
- Não derrubar o programa quando o arquivo estiver ausente ou corrompido.
- Dividir o código em pelo menos três arquivos, como
  `armazenamento.py`, `relatorios.py` e `main.py`.

**Critérios de aceitação**

Fechar e abrir o programa mantém os dados, datas inválidas recebem uma mensagem
clara e valores monetários não apresentam erros visíveis de arredondamento.

**Extras**

Filtro por intervalo de datas e meta de gasto mensal com alerta.

**Por onde começar**

Implemente primeiro apenas salvar e carregar uma lista de dicionários. Depois
construa as funcionalidades em cima da persistência.

</details>

### 📝 05 · Analisador de texto

> Estatísticas úteis a partir de qualquer arquivo `.txt`.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Lê um texto e calcula total de palavras, palavras mais frequentes, tamanho
médio, palavras únicas e linhas mais longas.

**Conceitos praticados**

Strings · `set` · `collections.Counter`/`defaultdict` · `pathlib` ·
`*args`/`**kwargs` · comprehensions · funções reutilizáveis

**Requisitos**

- Normalizar o texto com minúsculas e remoção de pontuação.
- Manter uma lista configurável de stop words, como “de”, “a” e “o”.
- Criar um relatório que aceite opções via `**kwargs`, como `top=10` e
  `min_tamanho=4`.
- Salvar o resultado em um arquivo de saída.

**Critérios de aceitação**

Funcionar com qualquer arquivo de texto, tratar arquivos vazios ou inexistentes
e manter a normalização isolada em uma função própria.

**Extras**

Comparar dois textos para encontrar palavras comuns e exclusivas e contar
frases.

**Por onde começar**

Teste a normalização com três ou quatro frases escritas à mão antes de ler
arquivos.

</details>

---

## 🏗️ Orientação a objetos

### 📦 06 · Sistema de estoque

> Produtos, movimentações e relatórios usando OOP básica.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Controla produtos, quantidades e preços por meio de entradas e saídas de
estoque.

**Conceitos praticados**

Classes e objetos · atributos e métodos · encapsulamento com `@property` ·
`__str__`/`__repr__` · exceções customizadas · type hints · docstrings

**Requisitos**

- Criar `Produto` com nome, preço e quantidade validados por `@property`.
- Criar `Estoque` para gerenciar a coleção de produtos.
- Usar exceções próprias, como `EstoqueInsuficienteError` e
  `ProdutoNaoEncontradoError`.
- Gerar relatório de produtos abaixo do mínimo e do valor total em estoque.
- Persistir em JSON, convertendo objetos para dicionários e vice-versa.

**Critérios de aceitação**

Nenhum atributo pode ser alterado externamente de forma inválida. Exceções
devem ser levantadas e tratadas em lugares diferentes, e todo método público
deve ter type hints.

**Extras**

Implementar `__eq__`, `__lt__` e um `@classmethod` para criar produtos a partir
de dicionários.

**Por onde começar**

Escreva apenas `Produto` e teste no terminal interativo antes de criar
`Estoque`.

</details>

### 🏦 07 · Banco simplificado

> Contas, transações e transferências com OOP avançada.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Simula contas bancárias de tipos diferentes, operações financeiras e extratos.

**Conceitos praticados**

Herança · polimorfismo · classes abstratas com `abc` · composição · `super()` ·
`@staticmethod`/`@classmethod` · persistência de objetos

**Requisitos**

- Criar a classe abstrata `Conta` com depositar, sacar e extrato.
- Criar pelo menos duas subclasses, como `ContaCorrente` e `ContaPoupanca`,
  cada uma com sua regra de saque.
- Criar `Cliente` com várias contas e `Transacao` com data.
- Implementar transferência atômica: se falhar, nada muda.
- Persistir clientes, contas e transações em JSON.

**Critérios de aceitação**

O mesmo código deve percorrer contas e chamar `sacar()` sem conhecer o tipo
concreto. Não espalhe condicionais `if tipo == ...` pelo código.

**Extras**

Implementar `__iter__` no extrato e um relatório do saldo total do cliente.

**Por onde começar**

Desenhe o diagrama de classes (atributos, métodos e relações) antes de codar.

</details>

---

## ✅ Qualidade e integração

### 🧪 08 · Testes e refatoração

> Transforme o Projeto 7 em uma aplicação mais profissional.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Não é um programa novo: refatora o banco simplificado, cria testes e organiza
o código como um pacote Python.

**Conceitos praticados**

`pytest` · fixtures · `venv` · `pip` · `requirements.txt` · PEP 8 · docstrings ·
estrutura de pacote

**Requisitos**

- Criar ambiente virtual e gerar `requirements.txt`.
- Escrever no mínimo 15 testes para depósitos, saques, limites,
  transferências e persistência.
- Testar exceções com `pytest.raises`.
- Reorganizar o código em um pacote `banco/`.
- Passar na verificação de estilo com Ruff ou Flake8.

**Critérios de aceitação**

O pytest passa limpo, outra pessoa consegue clonar e executar o projeto com
três comandos e pelo menos um bug é encontrado e corrigido pelos testes.

**Extras**

Medir cobertura com `pytest-cov` e alcançar 85% ou mais.

**Por onde começar**

Escreva primeiro os testes das operações simples, como depósito, para ganhar
ritmo.

</details>

### 📋 09 · Gerenciador de tarefas CLI

> O projeto integrador da trilha: uma aplicação de linha de comando completa.

<details>
<summary><strong>Ver escopo do projeto</strong></summary>

**O que faz**

Gerencia tarefas com prioridade, prazo, tags e status por meio de uma
interface de terminal.

**Requisitos**

- Usar `argparse`, por exemplo:
  `tarefas add "Estudar" --prioridade alta --prazo 2026-12-01`.
- Implementar pelo menos `Tarefa`, `GerenciadorTarefas` e `Repositorio`.
- Isolar persistência em JSON e permitir trocar a camada de armazenamento.
- Trabalhar com prazos usando `datetime` e destacar tarefas vencidas.
- Filtrar e ordenar por prioridade, prazo e tag.
- Exibir mensagens amigáveis, sem traceback para o usuário.
- Usar estrutura de pacote, `venv`, `requirements.txt`, README e exemplos.
- Escrever no mínimo 20 testes com pytest.

**Critérios de aceitação**

Instalação e uso documentados, regras de negócio cobertas por testes, código
seguindo PEP 8 com type hints e docstrings, e decisões de design explicáveis.

**Extras**

Tarefas recorrentes, exportação semanal em Markdown e um segundo repositório
SQLite que possa substituir o atual trocando apenas uma linha de código.

**Por onde começar**

Escreva o README antes do programa, descrevendo como ele será usado. Isso
ajuda a definir a interface antes da implementação.

</details>

---

## 🛠️ Como usar

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/caiobarretobr/Beginner__portfolio.git
cd Beginner__portfolio
```

Execute o projeto atual de calculadora:

```bash
python -m calc_python
```

> Os demais projetos entram na trilha conforme forem implementados. Cada um
> deve ter suas próprias instruções de instalação, execução e testes.

---

<div align="center">

### 🚀 Aprender construindo é o objetivo

Feito para praticar um conceito por vez, evoluir o código com intenção e
transformar dúvidas em pequenos projetos funcionais.

</div>
