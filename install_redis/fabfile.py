#!/usr/bin/python
from fabric import task, SerialGroup as Group


@task
def test(c):
    with c.local("cd redis-6.2.1"):
        result = c.local("make test", capture=True)
        if result.failed and not c.confirm("Tests failed. Continue anyway?"):
            c.abort("Aborting at user request.")
        else:
            c.green("All tests passed without errors!")

    with c.local("cd redis-6.2.1"):
        c.local("make clean")
    c.local("tar -czf redis-3.2.8.tar.gz redis-3.2.8")

@task
def deploy(c):
    c.put("redis-3.2.8.tar.gz",  "/tmp/redis-3.2.8.tar.gz")
    with c.cd("/tmp"):
        c.run("tar xzf redis-3.2.8.tar.gz")
        with c.cd("redis-3.2.8"):
            c.sudo("make install")

@task
def clean_file(c):
    with c.cd("/tmp"):
        c.sudo("rm -rf redis-3.2.8.tar.gz")
        c.sudo("rm -rf redis-3.2.8")

@task
def clean_local_file(c):
    c.local("rm -rf redis-3.2.8.tar.gz")

@task
def install(c):
    test(c)


for c in Group('10.8.100.3'):
    install(c)
