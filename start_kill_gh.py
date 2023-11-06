from sys import exit
from subprocess import Popen

PROCNAME = "GHelper"


def kill_gh():
    Popen(["powershell", f"Stop-Process -Name {PROCNAME}"])


def load_config():
    config = ""
    with open(".env", "r") as file:
        config = str(file.readline().strip("\n").replace(
            "\"", "").rstrip().lstrip().split("=")[-1])
    return config


def start_gh():
    config = load_config()
    if len(config) == 0:
        print(".env is either not create or does not have any variables.")
        exit(1)
    Popen(
        ["powershell", f"Start '{config}\\{PROCNAME}.exe'"])
