### v0.10.1

- **General documentation improvements**. Docstrings, more READMEs, naming conventions, etc.
- **Cleaner code according to PEP8**.
- **Future-proofing for Sphinx**. Make sure modules have proper "__main__" name conditions for future Sphinx stuff.
- **Support for versioning, distribution.** For PyPI.
	- "About" section (including version stuff)

### v0.11.0

- **Multiple processes**. Startup + CLI + LogicController (+ datacontroller?)
- **Improved CLI**. Switch from the current numbered menu to something involving argparse. Add a "help" functionality. Integrate with the error classes (let's do some ```try...except...``` statements!).
- **Debugging and logging support**.
- **Support for error classes**.
- **Testing support**.

### v0.12.0

- **Create installation files/binary files/exe files**.

### v0.13.0

- **A GUI using WPF**. This means piped processes, right? Woo!

### v0.14.0

- **Documentation update!** Sphinx.

### Medium-term features (introduce/polish before v1.0.0)

- Unisex names
- Ability to consider "weighted" name lists, like in the US census data.
- Ability to save names and view saved names
	- Ability to check for duplicate names
- Ability to differentiate between multiple cultural name lists, added by users

### Long-term features (introduce/polish before v1.0.0)

- SQLite? MySQL? PostgreSQL?
- Ability to handle different cultural naming traditions
- Save NPC files, track NPC data

### v1.0.0

- Stable release