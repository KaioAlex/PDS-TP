describe("Check Send Money", () => {
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

    it("Make transaction", () => {
        cy.get('.dashboard-buttons__btn.app-btn-primary').click()

        cy.get('.first-step-form__input').type('ennes')
        cy.get('.first-step-btn').click()

        cy.get('.second-step-amount__value').type('100')
        cy.get('.second-step-btn').click()

        cy.get('.third-step-btn').click()
        cy.get('.conclusion-btn').click()
      });
});