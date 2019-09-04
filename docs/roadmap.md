# *Rosevomit* roadmap

## v0.10.3

### Internal and development

- **Testing improvements**. More tests.
  - **Include list of tests 'run' vs 'not run'**?
- **Include venv in path, when running outside out VSCode**?

### Features

- **Ability to change settings from inside program**.
- **Ability to customize names of saved files.**
- **Improvements to Suncalc:**
  - **Ability to view a list of sunrise/local-noon/sunset times by day.** Much less data to look through.
  - **Ability to include internal variables in Suncalc results files.** Basically, a debug mode.

### Tweaks

- **Exit dialog should only be displayed if unsaved temp files exist.**

## v0.10.4

### Internal and development

- **Debugging and logging support**.
- **Basic, usable developer-defined error classes and messages**.

### Documentation

- **Helpful READMEs scattered throughout filesystem.**
- **Better (or any) docstrings**.

### Features

- **Improvements to random event generation**. Tentative? I don't really know what improvements I want to make.
- **Integrate Matplotlab (or some other plotting library?) into Suncalc so we can see results graphically.** Additionally, I'd like to be able to see graphs of saved data.

## v0.11.0

### Internal and development

- **Multiple processes**. Startup + CLI + LogicController (+ datacontroller?)? Could help speed up some list generation.

### Features

- **Sunlight calculator**. Enter some planetary variables and find the relevant info regarding sunrise and sunset on any particular day for any particular location, using the [sunrise equation](https://en.wikipedia.org/wiki/Sunrise_equation). AT THIS POINT, THE RESULTS SHOULD ACTUALLY BE ACCURATE ENOUGH FOR GAMEPLAY USE.

## v0.12.0

- **Improved CLI**. Switch from the current numbered menu to something involving argparse. Add a "help" functionality. Integrate with the error classes (let's do some ```try...except...``` statements!).
- **Name generation improvements**. Ability to view saved names. Ability to check for duplicate names.

## v0.13.0

- **Create installation files/binary files/exe files**.

## v0.14.0

- **A GUI using WPF**. This means piped processes, right? Woo!

## v0.15.0

- **Documentation update?** Sphinx.

## Medium-term features (introduce/polish before v0.20.0)

- Unisex names
- Ability to consider "weighted" name lists, like in the US census data.
- Ability to differentiate between multiple cultural name lists, added by users

## Long-term features (introduce/polish before v1.0.0)

- SQLite? MySQL? PostgreSQL?
- Ability to handle different cultural naming traditions
- Save NPC files, track NPC data

## v1.0.0

- Stable release