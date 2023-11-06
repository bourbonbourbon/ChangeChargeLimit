import json
from sys import exit
from os.path import isdir, exists
from os import getenv, makedirs

AppData = getenv('APPDATA')

ccl_loc = f"{AppData}\\ChangeChargeLimitPy"
ghc_loc = f"{AppData}\\GHelper"


def check_day_dupli(schedule):
    week = []
    for i in range(0, len(schedule)):
        day = schedule[i]["day"]
        if day not in week:
            week.append(day)
        else:
            return True
    return False


def directory_check(location):
    if isdir(location):
        return True
    return False


def file_check(location):
    if exists(location):
        return True
    return False


def print_exit(message, error_code):
    print(message)
    exit(error_code)


if __name__ == "__main__":
    if directory_check(ccl_loc) == False:
        print(
            f"Config directory for this program does not exist at {ccl_loc}.")
        print("Creating directory...")
        makedirs(ccl_loc)
    if file_check(f"{ccl_loc}\config.json") == False:
        print(
            f"Config file from this program does not exist at {ccl_loc}\config.json.")
        print("Creating file...")
        open(f"{ccl_loc}\config.json", "w").close()

    try:
        with open(f"{ccl_loc}\config.json") as file:
            ccl_config = json.load(file)
    except json.decoder.JSONDecodeError as error:
        print_exit("The config file does not contain any json data it in.", 1)
    if len(ccl_config) == 0:
        print_exit(
            "The config file for this program does not contain anything.", 1)

    schedule = ccl_config["schedule"]

    if check_day_dupli(schedule) == True:
        print_exit("There is a duplicate entry of a day in the config.")

    