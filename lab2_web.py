import xlrd
import numpy
import matplotlib.dates
from matplotlib import pylab
from pylab import *
from datetime import datetime

workbook = xlrd.open_workbook('c:/data/Analytics 3 Raw Data View test 20170201-20170228.xlsx')
worksheet = workbook.sheet_by_index(0)
rows_number = worksheet.nrows-1
dtype = ["desktop","mobile","tablet"]
utype = ["New Visitor","Returning Visitor"]

def parse_date(d):
    dd = datetime.strptime(d,'%Y%m%d%H')
    return dd

def date_str(d):
    dd = datetime.strftime(d,'%d %b %Y %H:00')
    return dd

def pretty_date_list():
    d_lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        dd = parse_date(row[0])#.date()
        d_lst.append(date_str(dd))
    return d_lst

def date_list():
    d_lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        dd = parse_date(row[0])#.date()
        d_lst.append(dd)
    return d_lst

def rows():
    rows = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        rows.append(row)
    return rows

def dtype_list():
    dev_lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        dev_lst.append(row[2])
    return dev_lst

def print_attr():
    i=0
    while i<11:
        a = worksheet.cell(0, i).value
        print (a)
        i=i+1

def prob(n):
    lst=[]
    pb=[]
    i=0
    sum = 0
    for rownum in range(1,worksheet.nrows):
        row=worksheet.row_values(rownum)
        lst.append(row[n])
    s = set(lst)
    r = list(s)
    for i in range(len(r)):
        p = lst.count(r[i])/rows_number
        pb.append(p)
        #print("x={}; p(x)={}".format(r[i],p))
        sum = sum+p
        i=i+1
    #print (i)
    #print (sum)
    return r,pb

'''
#n between (5,10) - number values
def stat(n)
    lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        lst.append(row[n])
    ev = "expected value = {}".format(numpy.mean(lst))
    v = "variance = {}".format(numpy.var(lst))
    std = "standart deviation = {}".format(numpy.std(lst))
    print (ev)
    print (v)
    print (std)
'''
def for_line_country_loadtime():
    d_lst = []
    c_lst = []
    ltime_lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        dd = parse_date(row[0])
        d_lst.append(dd.date())
        c_lst.append(row[1])
        ltime_lst.append(row[8])
    return d_lst,c_lst,ltime_lst

def dtype_matrix():
    desktop_list = []
    mobile_list = []
    tablet_list = []
    for i in range(len(r)):
        desktop = mobile = tablet = 0
        r1 = r[i]
        desktop = desktop + r1.count(dtype[0])
        desktop_list.append(desktop)
        mobile = mobile + r1.count(dtype[1])
        mobile_list.append(mobile)
        tablet = tablet + r1.count(dtype[2])
        tablet_list.append(tablet)
    return desktop_list,mobile_list,tablet_list
'''
r=rows()
M = dtype_matrix()
d = date_list()
set_d = set(d)
list_d = list(set_d)
for i in range(len(set_d)):
    desktop = mobile = tablet = 0
    for j in range(len(r)):
        if r[j][0]==list_d[i]:
'''

#for j in range(len(d)):
#    index = [i for i,x in gen if x==date_list[j]]
#    print (index)

#m=matplotlib.dates.date2num(date_list())
def date_axis():
    d_lst = []
    for rownum in range(1, worksheet.nrows):
        row = worksheet.row_values(rownum)
        dd = row[0]
        d_lst.append(dd)
    return d_lst

dev = [5,6,7]
date = [datetime(2017, 2, 10, 12, 0),datetime(2017, 2, 12, 12, 0),datetime(2017, 2, 16, 12, 0)]
plot(date,dev,linewidth=0.5)
xlabel('Oscilation x')
ylabel('Oscilation y')
title("bbb")
grid(True)
show()

'''
M = dtype_matrix()
print (M[0])
print (M[1])
print (M[2])
date_list = date_list()
d = list(set(date_list))
for i in range(len(d)):
'''
#print (for_line_country_loadtime())
#print(prob(1))
# prob_distribution_c_lt()