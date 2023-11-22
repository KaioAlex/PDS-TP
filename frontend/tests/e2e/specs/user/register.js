describe("Check Register", () => {
  beforeEach(() => {
    cy.viewport(1920, 1080)
  })

  it("Register User", () => {
    cy.visit("/");
    cy.contains('Cadastrar').click()

    // Should be on a new URL which
    cy.url().should('include', '/register')

    // Get an input, type into it
    cy.get('.register-fields__input.name').type('João Pedro')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.name').should('have.value', 'João Pedro')
    
    // Get an input, type into it
    cy.get('.register-fields__input.email').type('fake@email.com')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.email').should('have.value', 'fake@email.com')
  
      // Get an input, type into it
    cy.get('.register-fields__input.username').type('test_pds')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.username').should('have.value', 'test_pds')
    
    // Get an input, type into it
    cy.get('.register-fields__input.birthday').type('2000-02-14')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.birthday').should('have.value', '2000-02-14')
     
    // Get an input, type into it
    cy.get('.register-fields__input.password').type('12345')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.password').should('have.value', '12345')
    
    // Get an input, type into it
    cy.get('.register-fields__input.passwordConfirm').type('12345')

    //  Verify that the value has been updated
    cy.get('.register-fields__input.passwordConfirm').should('have.value', '12345')
    
    // Click on Login Button
    cy.get('.register__btn').click()
  });
});