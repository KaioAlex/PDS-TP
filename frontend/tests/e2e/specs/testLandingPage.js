describe("Check LP", () => {
  it("Visits the app root url", () => {
    cy.visit("/");
    cy.contains("h1", "O futuro do controle de finanças está aqui");
    cy.contains("p", "Descubra como é fácil controlar suas contas com SplitWallet");
  });
});