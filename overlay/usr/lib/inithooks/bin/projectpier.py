#!/usr/bin/python
"""Set ProjectPier admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache
import random
import hashlib
import uuid

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "ProjectPier Password",
            "Enter new password for the ProjectPier 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "ProjectPier Email",
            "Please enter email address for the ProjectPier 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    pos = random.randrange(25)
    salt = hashlib.sha1(str(uuid.uuid4())).hexdigest()[pos:pos+13]

    token = hashlib.sha1(salt + password).hexdigest()

    x = [str(i) for i in range(10)]
    random.shuffle(x)
    twister = ''.join(x)

    m = MySQL()
    m.execute('UPDATE projectpier.users SET email = "%s", token = "%s", salt = "%s", twister = "%s", updated_on = NOW() WHERE id = 1;' % (email, token, salt, twister))
    m.execute('UPDATE projectpier.contacts SET email="%s", updated_on=NOW() WHERE user_id = 1;')

if __name__ == "__main__":
    main()


