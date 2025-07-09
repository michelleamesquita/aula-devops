Feature: Acessar o Google

  Scenario: Abrir a página inicial do Google
    Given que estou na página inicial do Google
    Then a página deve conter o texto "Pesquisa Google"

  Scenario: Pesquisar a palavra linux no Google
    Given que estou na página inicial do Google
    When eu pesquiso por "linux"
    Then a página deve mostrar resultados para "linux"