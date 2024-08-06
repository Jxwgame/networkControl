import pexpect

PROMPT = '#'
IP_R1 = '172.31.106.3'
IP_R2 = '172.31.106.4'
USERNAME = 'admin'
PASSWORD = 'cisco'

child = pexpect.spawn('telnet ' + IP_R1)
child.expect('Username')
child.sendline(USERNAME)
child.expect('Password')
child.sendline(PASSWORD)
child.expect(PROMPT)
child.sendline('int loopback 0')
child.sendline('ip address 172.16.1.1 255.255.255.255')
result = child.before
print(result)
print()
print(result.decode('UTF-8'))
child.sendline('exit')

child_2 = pexpect.spawn('telnet ' + IP_R2)
child_2.expect('Username')
child_2.sendline(USERNAME)
child_2.expect('Password')
child_2.sendline(PASSWORD)
child_2.expect(PROMPT)
child_2.sendline('int loopback 0')
child_2.sendline('ip address 172.16.2.2 255.255.255.255')
result = child_2.before
print(result)
print()
print(result.decode('UTF-8'))
child_2.sendline('exit')

