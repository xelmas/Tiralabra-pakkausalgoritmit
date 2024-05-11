from invoke import task
import os

pty = os.sys.platform.startswith("linux")

@task
def start(ctx, function):
    ctx.run(f"python3 src/main.py {function}", pty=pty)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=pty)

@task
def lint(ctx):
    ctx.run("pylint src", pty=pty)

@task
def test(ctx):
    ctx.run("pytest src", pty=pty)

@task
def unit_tests(ctx):
    ctx.run("pytest src/tests/unit", pty=pty)

@task
def automatic_tests(ctx):
    ctx.run("pytest src/tests/automatic", pty=pty)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=pty)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty)