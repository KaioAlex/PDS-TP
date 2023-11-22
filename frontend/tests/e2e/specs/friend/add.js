describe("Check Add Friend", () => {
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

    it("Friends Menu", () => {
        cy.get('.menu-link.friends').click()
        cy.get('.friends-add__btn').click()

        cy.get('.friends-form__input').type('ennes')
        cy.get('.friends-add__btn').click()
    });
});