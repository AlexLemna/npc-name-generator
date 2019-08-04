import difflib
import os
import pathlib
import pprint
import subprocess
import traceback

import findimports


def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print ("EXCEPTION MESSAGE: ", e)
        print ()
        traceback.print_exc()
    finally:
        input()  # Waits for user to press 'enter' before moving on (closing).
