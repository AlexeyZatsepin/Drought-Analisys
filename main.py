__author__ = 'aleksey'
#coding: utf-8
from functions import *

index = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
'22','23','24','25','26','27']

area = ["Cherkasy","Chernihiv","Chernivci","Crimea","Dnipropetrovs'k","Donets'k","Ivano-Frankivs'k","Kharkiv","Kherson",
"Khmel'nyts'kyy","Kiev","Kiev City","Kirovohrad","Luhans'k"," L'viv","Mykolayiv","Odessa","Poltava"," Rivne",
"Sevastopol'","Sumy","Ternopil'","Transcarpathia","Vinnytsya","Volyn","Zaporizhzhya","Zhytomyr"]

downloadTime=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
'22','23','24','25','26','27']

sort(area)
delete()
i = 0
while i < len(index):
    downloadTime[i] = download(index[i], area[i])
    i= i+ 1

i=0
while i<len(index):
    print(find_max("%s.csv"%(index[i]+" "+area[i]+" "+downloadTime[i]),2013))
    i=i+1
i=0
while i<len(index):
    print(find_min("%s.csv"%(index[i]+" "+area[i]+" "+downloadTime[i]),2013))
    i=i+1
i=0
while i<len(index):
    print(find_drought("%s.csv"%(index[i]+" "+area[i]+" "+downloadTime[i]),15))
    i=i+1

