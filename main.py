import typer
from rich import print
import utils as utl


app = typer.Typer()

# default command for account activation
@app.callback(invoke_without_command=True)
def activate(account_id: str):
    utl.findConfig()
    utl.validateConfig()
    print(utl.config)




# @app.command()
# def menu():
#     pass



if __name__ == "__main__":
    app()