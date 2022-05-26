
import re

new_id = re.sub(pattern='[^a-z|0-9|-|_|.]|', string=input().lower(), repl='')
new_id = re.sub(pattern='\.\.+', string=new_id, repl='.')
new_id = re.sub(pattern='^\.|\.$', string=new_id, repl='')

if new_id == '':
    new_id = 'a'

new_id = re.sub(pattern='^\.|\.$', string=new_id[0:15], repl='')

while len(new_id) < 3:
    new_id += new_id[-1:]

print(new_id)
