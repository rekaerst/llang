import re


def message(msg):
    print("\033[94m[" + msg + "]\033[0m")


def sub_ansi_escape(test: str):
    rc = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return rc.sub("", test)
