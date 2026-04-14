# Biblioteca Rasa Chatbot

> Chatbot inteligente para bibliotecas escolares, construído com [Rasa Open Source](https://rasa.com/).

![Python](https://img.shields.io/badge/Python-3.8--3.10-blue?style=flat-square&logo=python&logoColor=white)
![Rasa](https://img.shields.io/badge/Rasa-3.x-purple?style=flat-square&logo=rasa&logoColor=white)
![Status](https://img.shields.io/badge/status-ativo-brightgreen?style=flat-square)
![Linguagem](https://img.shields.io/badge/idioma-Português-009c3b?style=flat-square)

---

## O que é?

Esse projeto se trata de um chatbot desenvolvido como atividade prática de biblioteca escolar. Ele responde perguntas sobre livros — título, autor, sinopse, personagens, tema, gênero e ano de publicação — de forma conversacional, diretamente pelo navegador.

---

## Funcionalidades

- Conversa em **português brasileiro**
- Responde perguntas sobre o livro cadastrado
- Botões de atalho para as perguntas mais comuns
- Interface visual simples via `interface.html`
- Powered by Rasa NLU + regras personalizadas

---

## Estrutura do Projeto

```
devchatbot/
├── biblio/
│   ├── data/
│   │   ├── nlu.yml        # Exemplos de frases por intenção
│   │   ├── stories.yml    # Fluxos de conversa
│   │   └── rules.yml      # Regras de resposta direta
│   ├── actions/
│   │   └── actions.py     # Ações customizadas (Python)
│   ├── domain.yml         # Intents, respostas e configuração
│   ├── config.yml         # Pipeline de NLU e políticas
│   └── models/            # Modelos treinados (gerado pelo rasa train)
└── interface.html         # Interface do chat no navegador
```

---

## Como rodar

### Pré-requisitos

- Python **3.8, 3.9 ou 3.10** (o Rasa **não funciona** com 3.11+)
- pip atualizado

```bash
pip install --upgrade pip
```

### 1. Instalar o Rasa

```bash
pip install rasa
```

### 2. Entrar na pasta do projeto

```bash
cd devchatbot/biblio
```

### 3. Treinar o modelo

```bash
rasa train
```

> Aguarde — o treinamento pode levar alguns minutos na primeira vez.

### 4. Iniciar o servidor

```bash
rasa run --enable-api --cors "*"
```

### 5. Abrir a interface

Com o servidor rodando, abra o arquivo `interface.html` no navegador (duplo clique).

---

## Perguntas que o bot responde

| Intenção | Exemplos de pergunta |
|---|---|
| Título | "Qual é o título do livro?" |
| Autor | "Quem escreveu o livro?" |
| Sinopse | "Do que trata o livro?" / "Me dá um resumo" |
| Personagens | "Quais são os personagens principais?" |
| Tema | "Qual é o tema central?" / "Qual a mensagem?" |
| Gênero | "Qual é o gênero literário?" |
| Ano | "Quando foi publicado?" |

---

## Livro configurado

> **O Pequeno Príncipe** — Antoine de Saint-Exupéry (1943)

Para trocar o livro, edite as respostas `utter_*` no arquivo `biblio/domain.yml` e rode `rasa train` novamente.

---

## Tecnologias

- [Rasa Open Source](https://rasa.com/docs/rasa/) — framework de chatbot
- HTML + CSS + JavaScript — interface do usuário
- Python — ações customizadas

---

## Licença

Projeto desenvolvido para fins acadêmicos. Livre para uso e modificação.
