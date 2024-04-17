# MeteoromixApp - Previsão do Tempo :partly_sunny:
Projeto API com Previsão do Tempo em Python 

---
Tabela de conteúdo
1. [Sobre o desafio](#sobre)
2. [Arquitetura do projeto](#arquitetura)
3. [Requisitos do projeto](#requisitos)
4. [Desafios do projeto](#desafios)
---

<div id='sobre' />

## Sobre o desafio

Este projeto tem como objetivo consultar uma API utilizando Python que permita a previsão do tempo para uma cidade específica, com possibilidade de gerar um gráfico da previsão do tempo e alertas em caso de condições precárias do tempo.

---

<div id='arquitetura' />

## Arquitetura do projeto

A API será consultada, utilizando a biblioteca Requests para buscar informações sobre a previsão do tempo do [OpenWeatherMap API](https://openweathermap.org/api). A arquitetura seguirá a lógica de Requisição -> Processamento -> Resposta, com uma camada de controle para lidar com as informações recebidas e os alertas.

**Requisição** | **Processamento** | **Resposta**
-------------- | ----------------- | ------------
A camada de requisição é responsável por buscar informações de previsão do tempo referentes à cidade desejada pelo usuário na OpenWeatherMap API. | A camada de processamento fará o tratamento dos resultados recebidos pelo OpenWeatherMap, tranformando-os em informações mais legíveis, e gerando o gráfico, se requisitado. | A camada de resposta é responsável por enviar a resposta final ao usuário, contendo informações sobre a previsão do tempo, gráfico (se for solicitado) e alertas, caso haja algum.

---

<div id='requisitos' />

## Requisitos do projeto

**Requisito** | **Descrição**
------------- | -------------
Consultar previsão do tempo. | O usuário deve ser capaz de informar o nome da cidade que quer obter a previsão do tempo para obter informações sobre o tempo atual e futuro.
Geração de gráfico. | Se o usuário desejar, ele terá a possibilidade de ver um gráfico que mostre a previsão do tempo para os próximos dias naquela cidade.
Alertas. | Deve haver um sistema que detecte quando alguma das condições meteorológicas estiverem atingindo valores preocupantes e emitindo um alerta para que o usuário tome as precauções necessárias.

---

<div id='desafios' />

## Desafios do Projeto

1. **Integração API** : Integrar informações de diferentes fontes pode ser um desafio. Neste projeto, a integração da OpenWeatherMap API pode exigir muita pesquisa e persistência.

2. **Criação de alertas** : A lógica do sistema de alerta pode ser complicada, principalmente ao determinar quando e como devem ser emitidos.

3. **Gráficos personalizados** : A geração de gráficos personalizados pode envolver muitas nuances e detalhes.