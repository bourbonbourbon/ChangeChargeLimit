from json import load, decoder, dumps
from sys import exit
from os.path import isdir, exists
from os import getenv, makedirs
from datetime import datetime

import start_kill_gh as skg

AppData = getenv('APPDATA')

ccl_loc = f"{AppData}\\ChangeChargeLimit"
gh_loc = f"{AppData}\\GHelper"


def get_config(type):
    loc = ""
    config = ""
    if type == "ccl":
        loc = ccl_loc
    else:
        loc = gh_loc

    if isdir(loc) == False:
        print(
            f"Config directory for this program does not exist at {loc}.")
        print("Creating directory...")
        makedirs(loc)

    if exists(f"{loc}\\config.json") == False:
        print(
            f"Config file from this program does not exist at {loc}\\config.json.")
        print("Creating file...")
        open(f"{loc}\\config.json", "w").close()

    try:
        with open(f"{loc}\\config.json", "r") as file:
            config = load(file)
    except decoder.JSONDecodeError as err:
        print_exit("The config file does not contain any json data it in.", 1)

    if len(config) == 0:
        print_exit(
            "The config file for this program does not contain anything.", 1)

    return config


def check_day_return_charge(current_day, schedule):
    day = ""
    charge = 0
    for i in range(0, len(schedule)):
        day = schedule[i]["day"]
        charge = schedule[i]["charge"]
        if day == current_day:
            return True, int(charge)
    return False, int(charge)


def check_dupli_day(schedule):
    week = []
    for i in range(0, len(schedule)):
        day = schedule[i]["day"]
        if day not in week:
            week.append(day)
        else:
            return True
    return False


def print_exit(message, error_code):
    print(message)
    exit(error_code)


def main():
    config_ccl = get_config("ccl")
    if not isinstance(config_ccl, dict):
        config_ccl = {}

    schedule = config_ccl.get("schedule")

    if check_dupli_day(schedule) == True:
        print_exit("There is a duplicate entry of a day in the config.", 1)

    current_day = datetime.now().strftime("%A")

    check, charge = check_day_return_charge(current_day, schedule)

    if charge % 5 != 0:
        print_exit("Value of charge is not divisible by 5.", 1)

    if check == True:
        gh_config_cl = get_config("gh")
        if not isinstance(gh_config_cl, dict):
            gh_config_cl = {}

        edit = False

        if gh_config_cl["charge_limit"] != charge:
            edit = True

        if edit == True:
            gh_config_cl["charge_limit"] = charge

            skg.kill_gh()

            with open(f"{gh_loc}\\config.json", "w") as file:
                file.write(dumps(gh_config_cl, indent=2))

            skg.start_gh()
        else:
            print_exit(
                "Not changing config since the charge limits are the same.", 0)


if __name__ == "__main__":
    main()
    exit(0)
