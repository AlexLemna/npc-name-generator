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

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


if __name__ == "__main__":
    try:
        myprompt = CLIv2()
        myprompt.prompt = "(testing)> "
        print()
        myprompt.cmdloop(intro="Starting CLIv2 testing prompt...")
        # Note that the intro argument here overrides CLIv2's "intro" attribute
    except SystemExit:
        SystemExit()
