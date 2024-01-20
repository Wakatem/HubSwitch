import typer
from rich import print
from utils import *


app = typer.Typer()

# default command for account activation
@app.callback(invoke_without_command=True)
def activate(account_id: str):
    global config
    configExists = findConfig()
    configValid = None
    
    if configExists:
        configValid = validateConfig
    
    if configValid:
        print(config)



# @app.command()
# def menu():
#     pass



if __name__ == "__main__":
    app()