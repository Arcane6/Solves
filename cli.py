import typer
import subprocess

cli = typer.Typer()



@cli.command()
def start_worker():
    """Inicia o worker Celery."""
    subprocess.run([
        "celery", 
        "-A", "app.core.celery_app:celery", 
        "worker", 
        "--loglevel=info", 
        "--pool=solo"
    ])

@cli.command()
def make_migrations():
    """Busca as migrações"""
    subprocess.run(["aerich", "migrate"])

@cli.command()
def migrate():
    """Executa as migrações do Tortoise ORM com Aerich."""
    subprocess.run(["aerich", "upgrade"])

@cli.command()
def init_db():
    """Inicializa o banco de dados e cria as tabelas iniciais."""
    subprocess.run(["aerich", "init-db"])

@cli.command()
def runserver( host: str = "0.0.0.0", port: int = 8000, reload: bool = True ):
    """Inicializa o servidor com Uvicorn."""
    command = [
        "uvicorn",
        "app.main:app",
        "--host", host,
        "--port", str(port),
    ]
    if reload:
        command.append("--reload")

    subprocess.run(command)

if __name__ == "__main__":
    cli()
