# Triple-quoted strings (ala Python docstrings) provide a possible to use large text section (separated by semi colon)
# as step parameter. Normally, so much text would not fit on one line."""

Feature: Large text processing in steps

  Scenario: Large text section as step parameter
    Given a sample text is loaded into the frobulator:
        """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    When frobulator is activated
    Then the text language is English