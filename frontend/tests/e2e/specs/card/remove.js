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
        cy.get('.card-remove').click({ multiple: true, force: true })
    });
});