import json
from sys import exit
from os.path import isdir, exists
from os import getenv

AppData = getenv('APPDATA')

this_config_loc = f"{AppData}\\ChangeChargeLimitPy"
g_helper_config_loc = f"{AppData}\\GHelper"
# test = "C:\\Users\\bourbon\\Downloads\\Files"
# this_config_loc = f"{test}\\ChangeChargeLimitPy"
# g_helper_config_loc = f"{test}\\GHelper"

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
    if directory_check(this_config_loc) == False:
        print_exit(f"Config directory for this program does not exist at {this_config_loc}", 1)
    if file_check(f"{this_config_loc}\config.json") == False:
        print_exit(f"Config file from this program does not exist at {this_config_loc}\config.json", 1)    

    try:
        with open(f"{this_config_loc}\config.json") as file:
            json_this_config = json.load(file)
    except json.decoder.JSONDecodeError as error:
        print_exit("The config file does not contain any json data it in.", 1)
    if len(json_this_config) == 0:
        print_exit("The config file for this program does not contain anything", 1)
    print(json_this_config)
