__author__ = 'aleksey'
from time import *
import pandas as pd
import urllib2
import os
import glob
#coding: utf-8




def download(index,area):
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R%s.txt" %index
    vhi_url = urllib2.urlopen(url)
    time=strftime("%Y-%m-%d.%H-%M-%S", gmtime())
    out = open('Downloads/%s.csv'%(index+' '+area+' '+time), 'wb')
    out.write(vhi_url.read())
    out.close()
    #print "Ae%s"%index
    return time

def read (fileName):
    df = pd.read_csv("Downloads/%s"%fileName ,index_col=False, header=1)
    return df

def write(df):
    print list(df.columns.values)

def sort(area):
    area.sort()

def delete():
    for file in glob.glob('Downloads/*.csv'):
        os.remove(file)


def find_max(fileName,year):
    df = read(fileName)
    yr=df[df['year']==year]
    print "in %s max value VHI in this area:"%year
    maximum = max(yr.VHI)
    return maximum

def find_min(fileName,year):
    df = read(fileName)
    yr=df[df['year']==year]
    print "in %s min value VHI in this area:"%year
    minimum = min(yr.VHI)
    return minimum


def find_drought(fileName,percent):
    df = read(fileName)
    tr=df[(df['VHI']<=percent) & (df['VHI']>=0)]
    print "drought on this area - %s" %fileName
    return tr

