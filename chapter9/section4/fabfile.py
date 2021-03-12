from fabric import SerialGroup as Group 



def hostname(c):
    c.run('hostname')

def ls(c, path='.'):
    c.run('ls {}'.format(path))

def tail(c, path='/etc/passwd', line=10):
    c.sudo('tail -n {0} {1}'.format(line, path))


for c in Group('10.8.100.3', '10.8.100.6'):
    hostname(c)
    ls(c)
    tail(c)
