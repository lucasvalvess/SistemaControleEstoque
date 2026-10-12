# 📦 Sistema de Controle de Estoque

Sistema web desenvolvido em **Django** para gerenciamento de estoque, permitindo o cadastro e gerenciamento de **produtos, categorias e fornecedores**.

O projeto foi desenvolvido como atividade prática da disciplina de **Desenvolvimento de Sistemas Web**, utilizando conceitos de desenvolvimento web com Django, organização de código, CRUD, relacionamento entre entidades, Git/GitHub e práticas de desenvolvimento colaborativo.

---

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Objetivo](#-objetivo)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Arquitetura](#-arquitetura)
- [Modelo de dados](#-modelo-de-dados)
- [Relacionamentos](#-relacionamentos)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Executando o projeto](#-executando-o-projeto)
- [Rotas principais](#-rotas-principais)
- [CRUDs](#-cruds)
- [Regras de negócio](#-regras-de-negócio)
- [Interface](#-interface)
- [Administração](#-administração)
- [Git e fluxo de desenvolvimento](#-git-e-fluxo-de-desenvolvimento)
- [Testes](#-testes)
- [Status do projeto](#-status-do-projeto)
- [Próximos passos](#-próximos-passos)
- [Autores](#-autores)

---

# 📖 Sobre o projeto

O **Sistema de Controle de Estoque** é uma aplicação web desenvolvida para facilitar o gerenciamento de produtos armazenados em um estoque.

A aplicação permite organizar os produtos por categorias e fornecedores, controlar quantidades disponíveis e identificar produtos que atingiram ou estão abaixo do estoque mínimo definido.

O sistema possui uma interface web construída utilizando os recursos de templates do Django, com um layout compartilhado entre as diferentes páginas da aplicação.

---

# 🎯 Objetivo

O principal objetivo do projeto é desenvolver um sistema web funcional para controle de estoque utilizando o framework **Django**, aplicando conceitos de:

- Desenvolvimento web;
- Arquitetura baseada em MVC/MTV;
- Banco de dados relacional;
- ORM;
- CRUD;
- Formulários;
- Relacionamentos entre entidades;
- Templates;
- Validação de dados;
- Git e GitHub;
- GitHub Projects;
- Pull Requests;
- Code Review;
- Desenvolvimento colaborativo.

Além do objetivo técnico, o projeto também simula um fluxo de desenvolvimento baseado em práticas ágeis.

---

# 🚀 Funcionalidades

## 📊 Visão geral

O sistema possui uma página inicial com informações gerais do estoque.

São apresentados indicadores como:

- Total de produtos ativos;
- Total de categorias ativas;
- Total de fornecedores ativos;
- Quantidade total de itens em estoque;
- Produtos com estoque baixo.

---

## 📦 Produtos

O módulo de produtos permite:

- Cadastrar produtos;
- Listar produtos;
- Editar produtos;
- Excluir produtos;
- Associar produtos a categorias;
- Associar produtos a fornecedores;
- Definir preço de compra;
- Definir preço de venda;
- Definir quantidade em estoque;
- Definir estoque mínimo;
- Definir SKU;
- Definir descrição;
- Ativar ou desativar produtos;
- Identificar produtos com estoque baixo.

### Informações do produto

Cada produto possui:

| Campo | Descrição |
|---|---|
| Nome | Nome do produto |
| SKU | Identificador único do produto |
| Descrição | Informações adicionais |
| Preço de compra | Valor pago pelo produto |
| Preço de venda | Valor de venda |
| Quantidade em estoque | Quantidade atualmente disponível |
| Estoque mínimo | Quantidade mínima desejada |
| Categoria | Categoria associada |
| Fornecedor | Fornecedor associado |
| Ativo | Indica se o produto está ativo |

---

# 🗂️ Categorias

O módulo de categorias permite:

- Criar categorias;
- Listar categorias;
- Editar categorias;
- Excluir categorias;
- Ativar ou desativar categorias;
- Adicionar descrição.

As categorias são utilizadas para organizar os produtos.

Exemplos:

```text
Eletrônicos
Informática
Periféricos
Limpeza
Escritório
Alimentos
