'''
@Author         : Sp4ce
@Date           : 2020-02-18 19:17:59
@LastEditors    : Sp4ce
@LastEditTime   : 2020-02-19 23:27:40
@Description    : Challenge Everything.
'''

import random
import binascii

###################################
# 全程包含4个-
# 第一位必须：F
# 第3位转为int后必须小于16
# 第4位转为int后必须小于16
# 5~9位必须为I:ALV
# 第11~13位必须为int型
# 长度必须大于22位
# 第16位必须为2或3
# 1~16位每位进行模2，若为0，num3+1
# num3向上取整并转为字符串后，与16位之后的值比较
###################################
def banner():
    print(r"""
          _ __      __  _  __           _____            
    /\   | |\ \    / / | |/ /          / ____|           
   /  \  | | \ \  / /  | ' / ___ _   _| |  __  ___ _ __  
  / /\ \ | |  \ \/ /   |  < / _ \ | | | | |_ |/ _ \ '_ \ 
 / ____ \| |___\  /    | . \  __/ |_| | |__| |  __/ | | |
/_/    \_\______\/     |_|\_\___|\__, |\_____|\___|_| |_|
                                  __/ |                  
                                 |___/     

                Apache Log Viewer 5.X KeyGen
                                                  By:Sp4ce
    """)

def checkValidCode(data):
    try:
        hexdata = data.replace('-', ':')
        data = "".join(data.split('-'))
        num = 0
        for i in hexdata:
            a = binascii.b2a_hex(i.encode('utf-8')).decode('utf-8')
            if int(a, 16) % 2 == 0:
                num = num+1
        hexData = binascii.b2a_hex((data+str(num)).encode('utf-8')) .decode('utf-8')
        hexData = list(hexData)
        hexData.insert(2, '-')
        hexData.insert(9, '-')
        hexData.insert(16, '-')
        hexData.insert(23, '-')
        licenseCode = ''.join(hexData)
        print("[+] License Code Generate Success!\nYour License Code: ->["+licenseCode.upper()+"]<-")
    except:
        print("[-] License Code Generate Failed!")



def main():
    banner()
    data = []
    data.append('F')  # 第一位必须：F
    data.append('-')  # 第一个-
    data.append(random.randint(1, 9))  # 第3位转为int后必须小于16
    data.append(random.randint(1, 9))  # 第4位转为int后必须小于16
    data.append('I')  # I
    data.append('-')  # 第二个-
    data.append('ALV')  # ALV
    data.append('-')  # 第三个-
    data.append(random.randint(100, 999))  # 第11~13位必须为int型
    data.append('-')  # 第四个-
    data.append(random.randint(1, 9))  # 第14位随机
    data.append(random.randint(2, 3))  # 第15位必须为2或3
    data = "".join('%s' % i for i in data).upper()
    checkValidCode(data)

if __name__ == "__main__":
    main()
