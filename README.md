<p align="center">
    <img src="logo.png" alt="drawing" width="200"/>
</p>

<h1 align="center"> HubSwitch </h1>

<p align="center">Command-line tool for seamlessly managing and switching between multiple GitHub accounts on a single machine, ideal for developers with both personal and professional profiles.</p>

## How to Use

Before using HubSwitch, ensure that your GitHub accounts' details are properly set up in the configuration file (`sampleConfig.json`). The configuration should include the GitHub username, email, and Personal Access Token (PAT) for each account. <br/>
***Note: store the config in a secure place as it contains sensitive information.***

### Setup

1. Define the `HubSwitch` environment variable on your system, pointing to the location of your configuration file.
2. Edit `sampleConfig.json` to include your GitHub account details and rename file to preference.

Example `sampleConfig.json`:
```json
{
    "version": 1.0,
    "accounts": {
        "work1": {
            "account_name": "Work",
            "username": "work_username",
            "email": "work_email@example.com",
            "PAT": "your_personal_access_token"
        }
        // ... Add other accounts as needed
    },
    "current": "work1"  // Set the default activated account ID
}  
```

### Basic Commands
#### Activate an Account
To activate an account, use the command activate followed by the account ID specified in your config file.
```bat
python main.py activate work1
```

#### View Current Account
To view the currently activated account, use the command current
```bat
python main.py current
```

#### List All Accounts
To list all accounts available in your configuration file, use the command accounts.
```bat
python main.py accounts
```

#### View Config Schema
To view the expected schema of your configuration file, use the command schema.
```bat
python main.py schema
```

## Modules Used

To build the CLI tool, this project leverages the following python modules:

- **Win32Cred**: To access windows credentials.
- **Typer**: For creating the command-line interface.
- **Rich**: For enhanced printing in the console, including JSON.
- **jsonschema**: To validate JSON data against a predefined schema.


