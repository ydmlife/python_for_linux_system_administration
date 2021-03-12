import pexpect

# spawn启动scp程序
child = pexpect.spawn('scp pexpect_scp.py root@10.8.100.3')

# expect方法等待子程序产生的输出，判断是否匹配期望的字符串
child.expect('Password:')

# 匹配到期望的字符串以后，发送密码串作为输入
child.sendline('Nsf0cus.')
