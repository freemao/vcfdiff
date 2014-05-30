#!/usr/lib/python
#-*- coding:utf-8 -*-
def diffvcf(x, y):
    f0 = open(x, 'r')
    f1 = open(y, 'r')
    newfile = x.split('.')[0] + '-' + y.split('.')[0] + '.txt'
    f2 = open(newfile, 'w')

    xsite_and_type = set()
    ysite_and_type = set()

    xzerozero = 0
    xzerone = 0
    xoneone = 0
    xother = 0
    for i in f0:
        if i.startswith('#'):
            pass
        else:
            k = ''.join(i.split()[0:4]) + '-' + i.split()[9].split(':')[0]
            xsite_and_type.add(k)
            m = i.split()[9].split(':')[0]
            if m == '0/0':
                xzerozero += 1
            elif m == '0/1':
                xzerone += 1
            elif m == '1/1':
                xoneone += 1
            else:
                xother += 1

    yzerozero = 0
    yzerone = 0
    yoneone = 0
    yother = 0
    for i in f1:
        if i.startswith('#'):
            pass
        else:
            k = ''.join(i.split()[0:4]) + '-' + i.split()[9].split(':')[0]
            ysite_and_type.add(k)
            m = i.split()[9].split(':')[0]
            if m == '0/0':
                yzerozero += 1
            elif m == '0/1':
                yzerone += 1
            elif m == '1/1':
                yoneone += 1
            else:
                yother += 1

    siteandtype_intersection = xsite_and_type & ysite_and_type

    ISzerozero = 0
    ISzerone = 0
    ISoneone = 0
    ISother = 0
    for i in siteandtype_intersection:
        j = i.split('-')[-1]
        if j == '0/0':
            ISzerozero += 1
        elif j == '0/1':
            ISzerone += 1
        elif j == '1/1':
            ISoneone += 1
        else:
            ISother += 1

    f2.write('\ttotal\t0/0\t0/1\t1/1\tother\n' + x + '\t' + \
str(len(xsite_and_type)) + '\t'+str(xzerozero) + '\t' + str(xzerone) + \
'\t' + str(xoneone) + '\t' + str(xother) + '\n' + y + '\t' + \
str(len(ysite_and_type)) + '\t' + str(yzerozero) + '\t' + str(yzerone) + \
'\t' + str(yoneone) + '\t' + str(yother) + '\n' + 'Intersection\t' + \
str(len(siteandtype_intersection)) + '\t' + str(ISzerozero) + '\t' + \
str(ISzerone) + '\t' + str(ISoneone) + '\t' + str(ISother) + '\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print 'Please assign your files that need to analyze!'
    if len(sys.argv) == 2:
        print 'Please input at least 2 files!'
    diffvcf(str(sys.argv[1]), sys.argv[2])



