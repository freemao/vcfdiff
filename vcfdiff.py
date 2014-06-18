#!/usr/lib/python
#-*- coding:utf-8 -*-
def diff2vcf(x, y):
    '''Argument x and y are vcf files you want to analyze.
       Count the number between them in some field such as total number,
       0/0, 0/1, 1/1 number and the intersection between them.
    '''
    f1 = open(x, 'r')
    f2 = open(y, 'r')
    newfile = ''.join(x.split('.')[0]) + '-' + ''.join(y.split('.')[0]) + '.txt'
    f0 = open(newfile, 'w')

    xsite_and_type = set()
    ysite_and_type = set()

    xzerozero = 0
    xzerone = 0
    xoneone = 0
    xother = 0
    for i in f1:
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
    for i in f2:
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

    f0.write('\ttotal\t0/0\t0/1\t1/1\tother\n' + x + '\t' + \
str(len(xsite_and_type)) + '\t'+str(xzerozero) + '\t' + str(xzerone) + \
'\t' + str(xoneone) + '\t' + str(xother) + '\n' + y + '\t' + \
str(len(ysite_and_type)) + '\t' + str(yzerozero) + '\t' + str(yzerone) + \
'\t' + str(yoneone) + '\t' + str(yother) + '\n' + 'Intersection\t' + \
str(len(siteandtype_intersection)) + '\t' + str(ISzerozero) + '\t' + \
str(ISzerone) + '\t' + str(ISoneone) + '\t' + str(ISother) + '\n')

def diff3vcf(x, y, z):
    '''Argument x, y, z are vcf files you want to analyze.
       Count the number between them in some field such as total number,
       0/0, 0/1, 1/1 number and the intersection between them.
    '''
    f1 = open(x, 'r')
    f2 = open(y, 'r')
    f3 = open(z, 'r')

    newfile = ''.join(x.split('.')[0:-1]) + '-' + \
''.join(y.split('.')[0:-1]) + '-' + ''.join(z.split('.')[0:-1]) + '.txt'
    f0 = open(newfile, 'w')

    xsite_and_type = set()
    ysite_and_type = set()
    zsite_and_type = set()


    xzerozero = 0
    xzerone = 0
    xoneone = 0
    xother = 0
    for i in f1:
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
    for i in f2:
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

    zzerozero = 0
    zzerone = 0
    zoneone = 0
    zother = 0
    for i in f3:
        if i.startswith('#'):
            pass
        else:
            k = ''.join(i.split()[0:4]) + '-' + i.split()[9].split(':')[0]
            zsite_and_type.add(k)
            m = i.split()[9].split(':')[0]
            if m == '0/0':
                zzerozero += 1
            elif m == '0/1':
                zzerone += 1
            elif m == '1/1':
                zoneone += 1
            else:
                zother += 1

    xy_siteandtype_intersection = xsite_and_type & ysite_and_type
    xz_siteandtype_intersection = xsite_and_type & zsite_and_type
    yz_siteandtype_intersection = ysite_and_type & zsite_and_type
    xyz_siteandtype_intersection = xsite_and_type & ysite_and_type & zsite_and_type

    xyISzerozero = 0
    xyISzerone = 0
    xyISoneone = 0
    xyISother = 0
    for i in xy_siteandtype_intersection:
        j = i.split('-')[-1]
        if j == '0/0':
            xyISzerozero += 1
        elif j == '0/1':
            xyISzerone += 1
        elif j == '1/1':
            xyISoneone += 1
        else:
            xyISother += 1

    xzISzerozero = 0
    xzISzerone = 0
    xzISoneone = 0
    xzISother = 0
    for i in xz_siteandtype_intersection:
        j = i.split('-')[-1]
        if j == '0/0':
            xzISzerozero += 1
        elif j == '0/1':
            xzISzerone += 1
        elif j == '1/1':
            xzISoneone += 1
        else:
            xzISother += 1

    yzISzerozero = 0
    yzISzerone = 0
    yzISoneone = 0
    yzISother = 0
    for i in yz_siteandtype_intersection:
        j = i.split('-')[-1]
        if j == '0/0':
            yzISzerozero += 1
        elif j == '0/1':
            yzISzerone += 1
        elif j == '1/1':
            yzISoneone += 1
        else:
            yzISother += 1

    xyzISzerozero = 0
    xyzISzerone = 0
    xyzISoneone = 0
    xyzISother = 0
    for i in xyz_siteandtype_intersection:
        j = i.split('-')[-1]
        if j == '0/0':
            xyzISzerozero += 1
        elif j == '0/1':
            xyzISzerone += 1
        elif j == '1/1':
            xyzISoneone += 1
        else:
            xyzISother += 1

    f0.write('\ttotal\t0/0\t0/1\t1/1\tother\nx\t' + \
str(len(xsite_and_type)) + '\t' + str(xzerozero) + '\t' + str(xzerone) + \
'\t' + str(xoneone) + '\t' + str(xother) + '\ny\t' + \
str(len(ysite_and_type)) + '\t' + str(yzerozero) + '\t' + str(yzerone) + \
'\t' + str(yoneone) + '\t' + str(yother) + '\nz\t' + \
str(len(zsite_and_type)) + '\t' + str(zzerozero) + '\t' + str(zzerone) + \
 '\t' + str(zoneone) + '\t' + str(zother) + '\n'+ 'x&y\t' + \
str(len(xy_siteandtype_intersection)) + '\t' + str(xyISzerozero) + '\t' + \
str(xyISzerone) + '\t' + str(xyISoneone) + '\t' + str(xyISother) + '\nx&z\t' + \
str(len(xz_siteandtype_intersection)) + '\t' + str(xzISzerozero) + '\t' + \
str(xzISzerone) + '\t' + str(xzISoneone) + '\t' + str(xzISother) + '\ny&z\t' + \
str(len(yz_siteandtype_intersection)) + '\t' + str(yzISzerozero) + '\t' + \
str(yzISzerone) + '\t' + str(yzISoneone) + '\t' + str(yzISother) + '\nx&y&z\t' + \
str(len(xyz_siteandtype_intersection)) + '\t' + str(xyzISzerozero) + '\t' + \
str(xyzISzerone) + '\t' + str(xyzISoneone) + '\t' + str(xyzISother) + '\n' + '\nx: '
+ x + '\n' + 'y: ' + y +'\n' + 'z: ' + z)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print 'Please assign your files that need to analyze!'
    if len(sys.argv) == 2:
        print 'Please input at least 2 files!'
    if len(sys.argv) == 3:
        diff2vcf(str(sys.argv[1]), str(sys.argv[2]))
    if len(sys.argv) == 4:
        diff3vcf(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))



