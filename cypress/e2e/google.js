import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

Given("que estou na página inicial do Google", () => {
  cy.visit("https://www.google.com");
});

When("eu pesquiso por {string}", (palavra) => {
  // O campo de pesquisa do Google tem o name 'q'
  cy.get('input[name="q"]').type(`${palavra}{enter}`);
});

Then("a página deve conter o texto {string}", (texto) => {
  cy.contains(texto);
});

Then("a página deve mostrar resultados para {string}", (palavra) => {
  // O Google mostra o termo pesquisado em algum lugar da página de resultados
  cy.get('input[name="q"]').should("have.value", palavra);
});