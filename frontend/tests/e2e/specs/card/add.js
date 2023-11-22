describe("Check Add Card", () => {
    beforeEach(() => {
        cy.viewport(1920, 1080)
    })

    it("Make login", () => {
      cy.visit("/");
      cy.contains('Login').click()
  
      // Should be on a new URL which
      cy.url().should('include', '/login')
  
      // Get an input, type into it
      cy.get('.login__input.username').type('pds_teste')
      
      // Get an input, type into it
      cy.get('.login__input.password').type('12345678')
      
      // Click on Login Button
      cy.get('.login__btn').click()
    });

    it("Cards Menu", () => {
        cy.get('.menu-link.cards').click()
        cy.get('.cards-add__btn').click()

        cy.get('.card-form__input.num_card').type('1111222233334444')
        cy.get('.card-form__input.username').type('PDS TESTE')
        cy.get('.card-form__input.card_validity').type('2026-02-14')
        cy.get('.card-form__input.security_code').type('123')
        cy.get('.add-card-header-btn').click()
    });
});