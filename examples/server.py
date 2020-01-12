from pyinfra.modules import server

SUDO = True

# simple example for a crontab
server.crontab(
    {'Backup /etc weekly'},
    '/bin/tar cf /tmp/etc_bup.tar /etc',
    name='backup_etc',
    day_of_week=0,
    hour=1,
    minute=0,
)

server.group(
    {'Create docker group'},
    'docker',
)

server.hostname(
    {'Set the hostname'},
    'server1.example.com',
)

server.user(
    {'Ensure user is removed'},
    'kevin',
    present=False,
)

# multiple users
for user in ['kevin', 'bob']:
    server.user(
        {'Ensure user {} is removed'.format(user)},
        user,
        present=False,
    )

server.group(
    {'Create uberadmin group'},
    'uberadmin',
)

# multiple groups
for group in ['wheel', 'lusers']:
    server.group(
        {'Create the group {}'.format(group)},
        group,
    )

#server.user(
#    {'Ensure an admin user is present'},
#    'uberadmin',
#    shell='/bin/bash',
#    groups=['wheel', 'uberadmin'],
#)

# use "/sbin/sysctl -a | grep file-max" to check value
server.sysctl(
    {'Change the fs.file-max value'},
    'fs.file-max',
    '100000',
    persist=True,
)

server.modprobe(
    {'Silly example for modprobe'},
    'floppy',
)

# To see output need to run pyinfra with '-v'
server.script(
    {'Hello'},
    'files/hello.bash',
)
