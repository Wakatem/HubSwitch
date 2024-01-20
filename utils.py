import os
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rich import print

path_variable = "HubSwitch"     # Environment Variable
config_version = 1.0
config = None                   # Config content

config_schema = {
    "type": "object",
    "properties": {
        "version": {"type": "number"},
        "accounts": {"type": "object"},
    },
    "required": ["version", "accounts"]
}


def findConfig():
    global config

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
        print(f"[bold red]Error:[/bold red] Config file is not in json")
        return False
    except json.decoder.JSONDecodeError as err:
        print(f"[bold red]Error:[/bold red] Config file contains incorrect JSON format")
        return False
    except ValidationError as err:
        print(f"[bold red]Error:[/bold red] Schema of config file does not match config schema {config_version}")
        if err.validator == 'required':
            print(f"Missing properties: {err.validator_value}")
        return False
