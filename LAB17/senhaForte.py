#senha forte
#REGEX
import re
# * matches class 0 or more
# + matches class 1 or more
# ? matches class 0 or 1
regexsenha=re.compile(r'[A-Z][a-z]+[0-9]+[!@#$&*]..+')

if regexsenha.match('Gfm02@LGO'):
    print('a')
