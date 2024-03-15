from invoke import task
import os

pty = os.sys.platform.startswith("linux")

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=pty)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=pty)

@task
def lint(ctx):
    ctx.run("pylint src", pty=pty)