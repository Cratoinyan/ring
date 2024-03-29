from email.policy import default
import os
import click
import subprocess

@click.group()
def cli():
    pass

@cli.command()
@click.option("-d/-p", default= False, help='enable or disable debug mode(default is disabled)')
def run(d):
    """Runs the ring bot on an avaliable port (default is :5000)"""
    os.environ["FLASK_APP"] = "app"
    if d:
        os.environ["FLASK_ENV"] = "development"
    else:
        os.environ["FLASK_ENV"] = "production"
    subprocess.run(os.path.dirname(__file__) + "/CLI/algrun.sh")
    
@cli.command()
def backtest():
    """Starts the backtesting process using the set strategy in backtrader.py"""
    import backtraderTest
    backtraderTest.run()
    