import typer
from rich import print, print_json
import utils as utl
from typing_extensions import Annotated


app = typer.Typer()

# default command for HubSwitch
@app.command()
def activate(id: str):
    
    # Find selected account
    accountFound = True
    try:
        details = utl.config["accounts"][id]
    except KeyError as err:
        print(f"[bold red]Error:[/bold red] Account {id} does not exist")
        accountFound = False

    if accountFound:
        try:
            account_name = details["account_name"]  
            username = details["username"]
            email = details["email"]  
            PAT = details["PAT"]
        except:
            print("[bold red]Error:[/bold red] Cannot extract account details. Make sure config file matches latest schema")

        # Update git credentials
        utl.update_credential(username, PAT)

        # Update git config file
        utl.run_command(f'git config --global user.name "{username}"')
        utl.run_command(f'git config --global user.email "{email}"')

        # Update current account property
        utl.config["current"] = id
        utl.saveConfig()
        
        print(f"[bold green]{account_name}[/bold green] account activated.")





@app.command()
def current(detailed: Annotated[bool, typer.Option(help="Display detailed information of activated account")] = False):
    id = utl.config["current"]

    # Fetch details of current account
    try:
        details = utl.config["accounts"][id]
        account_name = details["account_name"]  
    except KeyError as err:
        print(f"[bold red]Error:[/bold red] Could not fetch details of account {id}")
    
    # Display information
    if detailed:
        print(f"Current: [bold green]{account_name} ({id})[/bold green]")
        print_json(data=details)
        pass
    else:
        print(f"Current: [bold green]{account_name} ({id})[/bold green]")



if __name__ == "__main__":
    # Setup config file
    utl.findConfig()
    utl.validateConfig()
    app()