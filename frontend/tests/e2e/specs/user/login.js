describe("Check Login", () => {
  beforeEach(() => {
    cy.viewport(1920, 1080)
  })
  
  it("Make login", () => {
    cy.visit("/");
    cy.contains('Login').click()

    // Should be on a new URL which
    cy.url().should('include', '/login')

    // Get an input, type into it
    cy.get('.login__input.username').type('fake@email.com')

    //  Verify that the value has been updated
    cy.get('.login__input.username').should('have.value', 'fake@email.com')
    
    // Get an input, type into it
    cy.get('.login__input.password').type('12345')

    //  Verify that the value has been updated
    cy.get('.login__input.password').should('have.value', '12345')
    
    // Click on Login Button
    cy.get('.login__btn').click()
  });
});