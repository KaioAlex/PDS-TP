describe("Visit LandingPage", () => {
  it("Visits the app root url", () => {
    cy.visit("/");
    cy.contains("h1", "O futuro do controle de finanças está aqui");
    cy.contains("p", "Descubra como é fácil controlar suas contas com SplitWallet");
  });
});

describe("Visit Login Header", () => {
  it("Visits the app login url", () => {
    cy.visit("/");
    cy.contains('Login').click()

    // Should be on a new URL which
    cy.url().should('include', '/login')
  });
});

describe("Visit Register Header", () => {
  it("Visits the app register url", () => {
    cy.visit("/");
    cy.contains('Cadastrar').click()

    // Should be on a new URL which
    cy.url().should('include', '/register')
  });
});

describe("Visit Register Banner Section", () => {
  it("Visits the app register url", () => {
    cy.visit("/");
    cy.get('.home-banner-left__btn').click()

    // Should be on a new URL which
    cy.url().should('include', '/register')
  });
});

describe("Visit Register Explore Section", () => {
  it("Visits the app register url", () => {
    cy.visit("/");
    cy.get('.explore-content__btn').click()

    // Should be on a new URL which
    cy.url().should('include', '/register')
  });
});