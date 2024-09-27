Teste de Desenvolvimento - Aplicação Web C# Consumindo API v3 do Bling
Objetivo:
Desenvolver uma aplicação web simples usando C# e um banco de dados SQL que consome a API v3 do Bling. O foco do teste é avaliar a habilidade do candidato em integrar APIs, manipular dados e desenvolver funcionalidades de back-end. A aplicação deverá ser capaz de importar e gerenciar dados de vendas e produtos, além de analisar e prospectar compras.
Descrição do Teste:
1. Preparação:
Antes de iniciar o desenvolvimento, o candidato deverá realizar algumas etapas de preparação:
Criar uma conta gratuita no Bling:
[https://www.bling.com.br/inscricao?plano=PlanoMercurio]
Cadastrar 10 produtos fictícios na conta Bling:
[https://www.bling.com.br/produtos.php#list]
Cada produto deve ter um nome, descrição, código SKU, preço e fornecedor.
Gerar ao menos 30 vendas para esses produtos:
[https://www.bling.com.br/vendas.php#list]
As vendas devem incluir uma variedade de quantidades e combinar diferentes itens dentro de uma mesma venda.
2. Funcionalidades a Implementar:
Módulo de Importação de Vendas:
Descrição: Desenvolver um módulo que consome a API v3 do Bling para importar as vendas cadastradas e armazená-las no banco de dados SQL.
Requisitos:
    • As vendas devem ser importadas com todos os detalhes, incluindo produtos vendidos, quantidades, preços, clientes e datas.
    • Deve haver um botão de "Importar Vendas" que, ao ser clicado, realiza a importação e exibe uma confirmação do sucesso ou erro da operação.
    • As vendas importadas devem ser listadas em uma tabela na aplicação.
Módulo de Importação de Produtos:
Descrição: Criar um módulo que consome a API v3 do Bling para importar todos os produtos cadastrados e armazená-los no banco de dados SQL.
Requisitos:
    • Os produtos devem ser importados com todas as informações, como código SKU, nome, descrição, preço, estoque, fornecedor e TAGs.
    • Deve haver um botão de "Importar Produtos" que, ao ser acionado, realiza a importação e exibe os produtos em uma tabela na aplicação.
Módulo de Compras:
Descrição: Implementar um módulo para analisar as compras por um período selecionado pelo usuário e prospectar compras de produtos com base em um número de dias informado e uma projeção de crescimento das vendas.
Requisitos:
    • O usuário deve poder selecionar um período (data inicial e final) para análise das vendas realizadas.
    • O usuário deve informar uma porcentagem de projeção de crescimento das vendas, que deve ser considerada no cálculo de prospecção.
    • A aplicação deve calcular as quantidades médias vendidas dos produtos nesse período, aplicar a projeção de crescimento informada e sugerir uma quantidade de compra baseada em uma projeção para um número de dias futuro.
    • Exemplo: Se foram vendidas 100 unidades de um item em 30 dias, e o usuário deseja projetar a compra para suprir 30 dias futuros de vendas com um crescimento de 30%, a aplicação deve exibir que a quantidade a ser comprada é de 130 unidades.
    • Deve haver uma lista (ou derivado) que mostre todos os itens do estoque junto com suas projeções de compra.
    • O módulo deve permitir a filtragem de projeções por fornecedor, oferecendo ao usuário a opção de selecionar o fornecedor através de uma combobox ou realizar uma pesquisa no textbox. A interface exibirá somente as projeções dos produtos vinculados ao fornecedor selecionado.
    • Deve ser possível gerar um pedido de compra com os itens e quantidades prospectadas. Este pedido deve ser enviado através da API para o Bling, onde será gerado um pedido de compra real na plataforma.

3. Requisitos Técnicos:
Linguagem e Framework: C# com ASP.NET Core.
Banco de Dados: SQL Server ou SQLite.
Interface Gráfica: Simples, utilizando Razor Pages ou MVC. A interface pode ser básica, focando na funcionalidade.
Integração: Utilizar a API v3 do Bling para todas as operações de importação e exportação de dados, incluindo a geração de pedidos de compra.
Documentação: O código deve ser bem documentado, com comentários explicando as principais funcionalidades e decisões tomadas.
Controle de Versão: O código deve ser versionado utilizando Git, com commits frequentes e mensagens claras.
4. Entregáveis:
Código-Fonte: O repositório Git com todo o código da aplicação.
Instruções de Uso (Opcional): Um arquivo README.md detalhando como configurar o ambiente, executar a aplicação e realizar os testes.
Vídeo de Demonstração (Opcional): Um curto vídeo explicando as funcionalidades desenvolvidas e como a aplicação funciona.
5. Critérios de Avaliação:
Funcionalidade: A aplicação cumpre todos os requisitos listados?
Código: O código é bem estruturado, modular e fácil de entender?
Integração com API: A integração com a API v3 do Bling foi realizada de forma eficiente e segura?
Manipulação de Dados: A importação e manipulação dos dados são realizadas corretamente?
Prospecção de Compras: A lógica para prospecção de compras está bem implementada e é funcional?
Documentação: A aplicação está bem documentada.
Uso do Git: O uso do controle de versão é consistente, e os commits são frequentes e informativos?
Dicas Adicionais:
Validação de Dados: Implemente validações nos módulos de importação para garantir que os dados sejam consistentes e corretos.
Tratamento de Erros: Certifique-se de tratar exceções de maneira adequada para evitar que a aplicação falhe silenciosamente.
Testes Unitários: Se possível, implemente testes unitários para as principais funcionalidades da aplicação.
Documentação API Bling [https://developer.bling.com.br/bling-api#introdu%C3%A7%C3%A3o]
Canal do YouTube Bling: O canal do Bling oferece uma série de vídeos curtos que ensinam como cadastrar fornecedores, produtos, vendas, entre outras funcionalidades essenciais que podem ser necessárias para o desenvolvimento da aplicação. [https://www.youtube.com/@BlingBr]

