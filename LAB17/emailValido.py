#email valido
#REGEX

import re

regexmail=re.compile(r'[\w\-\+\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')

if regexmail.match('ramos_cassio@ic.commm'):
    print('a')
else:
    print('b')
