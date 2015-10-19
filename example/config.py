# pyinfra
# File: example/config.py
# Desc: entirely optional config file for the CLI deploy
#       see: pyinfra/api/config.py for defaults

from pyinfra import local

# These can be here or in deploy.py
TIMEOUT = 1
FAIL_PERCENT = 81


# Deploy hook, can also be in deploy.py
def before_connect(data, state):
    # Check something local is correct, etc
    branch = local.shell('git rev-parse --abbrev-ref HEAD')
    app_branch = data.app_branch

    if branch != app_branch:
        # Raise SystemExit for pyinfra to handle
        raise SystemExit('We\'re on the wrong branch (want {0}, got {1})!'.format(
            branch, app_branch
        ))


def before_deploy(data, state):
    print 'Before deploy hook', data


def after_deploy(data, state):
    print 'After deploy hook:', data
