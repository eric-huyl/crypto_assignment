# -*- coding:utf-8 -*-

# 通过爆破的方法得出符合要求的密码
# 最后完成整个程序需要的时间为9s

import re
from Crypto.Hash import SHA
import hashlib
import itertools
import datetime
starttime = datetime.datetime.now()
hash1="67ae1a64661ac8b4494666f58c4822408dd0a3e4"
str2=[['Q', 'q'],[ 'W', 'w'],[ '%', '5'], ['8', '('],[ '=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]
def sha_encrypt(str):
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts
st3="0"*8
str4=""
str3=list(st3)
for a in range(0,2):
    str3[0]=str2[0][a]
    for b in range(0,2):
        str3[1]=str2[1][b]
        for c in range(0,2):
            str3[2]=str2[2][c]
            for d in range(0,2):
                str3[3] = str2[3][d]
                for e in range(0,2):
                    str3[4] = str2[4][e]
                    for f in range(0,2):
                        str3[5] = str2[5][f]
                        for g in range(0,2):
                            str3[6] = str2[6][g]
                            for h in range(0,2):
                                str3[7] = str2[7][h]
                                newS="".join(str3)
                                for i in itertools.permutations(newS, 8):
                                    str4 = sha_encrypt("".join(i))
                                    if str4==hash1:
                                        print "".join(i)
                                        endtime = datetime.datetime.now()
                                        print (endtime - starttime).seconds
                                        exit(0)