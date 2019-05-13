import cmd  # "Simple framework for writing CLIs"
import shlex  # "Lexical analysis for simple syntaxes resembling Unix shell"
import sys  # "System-specific parameters and functions"
if sys.platform == "win32" or sys.platform == "cygwin":
    try:
        import pyreadline  # "A Python implementation of GNU readline" (necessary for autocomplete)
    except ImportError:
        raise ImportError("Please install the 'pyreadline' module from pypi.")
else:
    import readline  # Available as part of the standard library on most non-Windows systems.


class CLIv2(cmd.Cmd):
    """Creates instance of 'Cmd' framework, which we modify."""
    intro = "Starting CLIv2 prompt..."
    prompt = "> "
    # ----- Quick guide to Cmd -----
    # Any method we define below using the 'do_*' prefix will be interpreted by Cmd as a command it can offer the user. Anything the user types following a recognized command (before pressing 'enter') is passed to that command's 'do_*' method via the user_input parameter. If I want cool parsing functionality, then I need to build it around each method's user_input parameter. If the user requests help-text for the command, then that help-text is either automatically generated via a docstring or using the corresponding method with a 'help_*' prefix. The benefit of having an explicit 'help_*' method instead of a docstring is that, while Cmd already has a solid foundation of built-in ways for the user to request help-text, adding additional ways for the user to request help-text is easier when I have a help function to point to.
    # Additionally: I suspect (but have not tested) that if both a docstring and a matching 'help_*' method are available, Cmd will use the 'help_*' method to generate the help-text. Just something I should keep in mind.

    def do_about_program(self, user_input):
        """Displays version and license information about the program."""
        if user_input == "?":
            return self.help_about_program()
        else:
            pass

    def help_about_program(self):
        print ("Displays version and license information about the program.")

    def do_generate(self, user_input):
        """Generates random information according to a given set of parameters."""
        if user_input == "?":
            return self.help_generate()
        else:
            pass

    def help_generate(self):
        print ("Generates random information according to a given set of parameters.")

    # ----- Formatting request -----
    # Keep the following methods at the end of the class.
    def do_quit(self, user_input):
        """Quits the program."""
        if user_input == "?":
            return self.help_quit()
        else:
            print ("Quitting.")
            raise SystemExit

    def help_quit(self):
        print("Quits the program.")

    # "Ctrl-D" is a common way to exit many CLIs. Cmd interprets 'Ctrl-D' as as EOF signal by default, and does not know what to do with it. We can fix this by simply telling Cmd to interpret EOF as 'quit'.
    do_EOF = do_quit
    help_EOF = help_quit

    def default(self, user_input):
        """The 'default' method runs if the input is not a recognized command."""

        if user_input == "q" or user_input == "qu" or user_input == "qui" or user_input == "quitt":
            return self.do_quit(user_input)
        elif user_input == "exit" or user_input == "end":
            return self.do_quit(user_input)
        else:
            print (f"'{user_input}' is not a recognized command.")
            print()


if __name__ == "__main__":
    try:
        myprompt = CLIv2()
        myprompt.prompt = "(testing)> "
        print()
        myprompt.cmdloop(intro="Starting CLIv2 testing prompt...")
        # Note that the intro argument here overrides CLIv2's "intro" attribute
    except SystemExit:
        SystemExit()
