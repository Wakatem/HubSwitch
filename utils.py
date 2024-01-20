import os
import subprocess
import win32cred
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rich import print

path_variable = "HubSwitch"     # Environment Variable
config_version = 1.0
config_path = ""
config = None                   # Config content

config_schema = {
    "type": "object",
    "properties": {
        "version": {"type": "number"},
        "accounts": {"type": "object"},
    },
    "required": ["version", "accounts"]
}

config_schema_example = """{
    "version":<version number>,
    "accounts":{
        "<Any id for the account, e.g work1>":{
            "account_name":"<Any descriptive name, e.g Work>",
            "username":"<github username here>",
            "email":"<gitub email here>",
            "PAT":"<Your PersonalAccessToken here>"
        }
    },
    "current":"<activated account ID>"
}"""

def findConfig():
    global config
    global config_path

    # Retrieve HubSwitch variable value from system environment
    path = os.environ.get(path_variable)
    if path is not None:

        # If file is not json 
        if path.lower().endswith(".json") == False:
            print("[bold red]Error: [/bold red][bold blue]HubSwitch[/bold blue] path references non-json file")
            return False
        
        # Read config file
        try:
            config_file = open(path, 'r')
            config = config_file.read()
            config_file.close()

            config_path = path
            return True
        except:
            print("[bold red]Error:[/bold red] Cannot read config file")
            return False
    
    else:
        # If system environment is not found
        print("[bold red]Error:[/bold red] Cannot find [bold blue]HubSwitch[/bold blue] variable")
        return False



def validateConfig():
    global config

    try:
        config = json.loads(config)
        validate(instance=config, schema=config_schema)
        return True
    except TypeError as err:
        print(f"[bold red]Error:[/bold red] Config is not a JSON file")
        return False
    except json.decoder.JSONDecodeError as err:
        print(f"[bold red]Error:[/bold red] Config file contains incorrect JSON format")
        return False
    except ValidationError as err:
        print(f"[bold red]Error:[/bold red] Schema of config file does not match config schema {config_version}")
        if err.validator == 'required':
            print(f"Missing properties: {err.validator_value}")
        return False


def saveConfig():
    global config
    global config_path

    # Save config json
    with open(config_path, 'w', encoding='utf-8') as config_file:
        json.dump(config, config_file)


# Function to run shell commands and suppress output
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode


def update_credential(username, PAT):
    credential = dict(
        Type=win32cred.CRED_TYPE_GENERIC,
        TargetName="git:https://github.com",
        UserName=username,
        CredentialBlob=PAT,
        Persist=win32cred.CRED_PERSIST_LOCAL_MACHINE
    )
    
    win32cred.CredWrite(credential, 0)