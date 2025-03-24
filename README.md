# Notes

A pattern for writing tests

- Arrange
- Act
- Assert

What are Pytest Fixtures?

- Fixtures are functions
- Run before/after each test function to which the fixture is applied.

Why are fixtures important?

- Fixtures are used to feed data to the tests such as database connections, URLs to test and input data.

What is Factory Boy?

- Fixture replacement tool
- Factories are defined in a nice, clean and readable manner.
- Easy-to-use factories for complex objects.
- Class-based approach
  - SubFactories
  - ForeignKey, reverses ForeignKey, ManyToMany
