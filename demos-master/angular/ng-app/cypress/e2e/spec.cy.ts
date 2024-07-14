describe('template spec', () => {
  it('passes home page', () => {
    cy.visit('http://localhost:4200/');
    cy.contains('My Application');
    cy.contains('Hello');
    cy.contains('Welcome');
    cy.contains('Parent');
    cy.contains('Favs');
    cy.contains('ToDo');
    cy.contains('Logout').should('not.exist');
  });

  it('passes Hello page', () => {
    cy.visit('http://localhost:4200/emps');
    cy.contains('Error fetching data.. Check server is running or not..');
    cy.url().should('include', '/emps');
  });

  it('passes Welcome page', () => {
    cy.visit('http://localhost:4200/welcome');
    cy.contains('Login');
    cy.url().should('include', '/login');
    cy.get(':button').should('be.disabled');
    cy.get('#userid').type('admin');
    cy.get('#passwd').type('admin');
    cy.get(':button').should('be.enabled');
    cy.get('#btnLogin').click();
    cy.url().should('include', '/welcome');
    cy.contains('Logout');

    cy.contains('a', 'Logout').click();
    cy.contains('Are you sure to Logout?');

    cy.get('#b1').click();
    cy.contains('Logout').should('not.exist');
  });
});
