# Environmental setup

* [venv](#venv)
* [VS Code](#vscode)
  * [.vscode/](#.vscode/)
  * [.for-vscode.env](#.for-vscode.env)

## venv

*See: [Official documentation and tutorial](https://docs.python.org/3/tutorial/venv.html)*

First, navigate to the directory that will contain the project repository or directories.

````shell
> cd project_folder_path
> python -m venv name-of-desired-venv
````

In order to activate the virtual environment in Windows, run:

````shell
> venv/Scripts/activate.ps1
````

or, in Mac or Unix, run:

````shell
source name-of-desired-venv/bin/activate
````

This should result in something looking like this:

### updating with pip

From within the virtual environment, you can now modify/install/update Python modules without affecting your "base" installation. The pip version that is automatically installed in the virtual environment might be out of date. We can try to install an upgrade first with

```shell
> python -m pip install --upgrade pip
```

Note that setuptools might also be installed and out of date, so feel to type ```pip install --upgrade setuptools``` as well. No need for the `python -m` when we aren't trying to have pip upgrade itself.

Then, install the required

```python
>>> pip install --upgrade setuptools
```

If you ever want to quickly upgrade all out-of-date modules (not necessarily recommended), try the following (shamelessly stolen from [here](https://simpleit.rocks/python/upgrade-all-pip-requirements-package-console-commands/)):

```shell
> pip list --outdated --format columns | cut -d' ' -f1 | xargs -n1 pip install --upgrade
```

This might look a big complex, but here's what each command does:

* `pip list --outdated` lists the outdated packages
  * `--format columns` makes sure that the outdated packages are printed in a nice column layout
* `cut -d' '` splits the results from the earlier commands into "fields" at each space character it encounters
  * `f1` takes the first field of each line
* `xargs -n1` is basically "use at most 1 arg by command line". No idea what this means. Again, I'm just copying this from [here](https://simpleit.rocks/python/upgrade-all-pip-requirements-package-console-commands/).
  * `pip install --upgrade` upgrades all the packages

## VS Code

### `.vscode/`

For `.launch.json`, copy and paste...

````json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Rosevomit: Run",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/rosevomit/rosevomit.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Rosevomit: Test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/devtests/_runtests.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Rosevomit: Deep Test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/devtests/_runtests.py",
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
    ]
}
````

For `.settings.json`, copy and paste:

````json
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.envFile": "<SOMETHING>\\rosevomitrepo\\for-vscode.env", // <-- CHANGE to the appropriate absolute path
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--argument-rgx=ARG_[a-z_][a-z0-9_]{2,30}$",
        "--enable=all",
        "--disable=C0301,C0326,R1705",
    ],
    "python.linting.pylintCategorySeverity.refactor": "Information",
    "python.linting.mypyEnabled": true,
}
````

### `for-vscode.env`

````text
# regarding VSCode issue 3840 https://github.com/Microsoft/vscode-python/issues/3840

PYTHONPATH = ./rosevomit

# Problem here: https://github.com/PyCQA/pylint/issues/859
# Solution here: https://stackoverflow.com/questions/4374455/how-to-set-sys-stdout-encoding-in-python-3
PYTHONIOENCODING = utf-8
````