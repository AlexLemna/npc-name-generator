# Rosevomit's style guide

In general, Rosevomit's code should be written to whatever standards are generally accepted by the relevant language community. Since right now all of Rosevomit is written in Python, this is easy - Python's style guide, [PEP8](https://www.python.org/dev/peps/pep-0008/), is both official and widely accepted, so all of Rosevomit's code should be compared against it. There are a few areas where I do *not* follow PEP8 (yet) - these will be explored later.

## Python naming conventions

**Functions**, **variables**, **methods**, and **instances** should be lowercase. Separating words with underscores to increase readibility is welcomed, especially if some of the words are abbreviations or acronyms. *See: [snake_case](https://en.wikipedia.org/wiki/Snake_case)*

Since Python does not support **constants** natively, is it considered best practice to write variables you expect to be constant in all capital letters. Like all other variables, constants should be written with underscores when it improves readibility.

**Classes** should have the first letter of each word capitalized, and should have no spaces. *See: [CamelCase](https://en.wikipedia.org/wiki/Camel_case)*

**Modules** and **packages** intended for distribution on PyPI should be lowercase. Modules and packages *not* intended for distribution (which is most, if not all, Python files in this repository) should be written with the first letter capitalized and without underscores. *Again, see: [CamelCase](https://en.wikipedia.org/wiki/Camel_case)*

### tl;dr

- `menu_choice` and `menuchoice` might be variables or functions, but `MenuChoice` is definitely a class.
- `MENU_CHOICE` and `MENUCHOICE` are constants.

