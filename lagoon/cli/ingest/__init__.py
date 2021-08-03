
import typer
app = typer.Typer()

from .git import app as git_app
app.add_typer(git_app, name='git')

from .ocean_pickle import app as ocean_pickle_app
app.add_typer(ocean_pickle_app, name='ocean_pickle')

if __name__ == '__main__':
    app()

