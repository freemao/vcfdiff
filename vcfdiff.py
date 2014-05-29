#!/usr/lib/python
#-*- coding:utf-8 -*-
f0 = open('C17.BQSR.vcf')
f1 = open('C17.vcf')
f2 = open('statistic_outcome.txt', 'w')
BQSRsite= set()
C17site = set()

BQSRsite_and_type = set()
C17site_and_type = set()


C17zerozero = 0
C17zerone = 0
C17oneone = 0
C17other = 0
for i in f0:
    if i.startswith('#'):
        pass
    else:
        j = ''.join(i.split()[0:4])
        BQSRsite.add(j)
        k = ''.join(i.split()[0:4]) + '-' + i.split()[9].split(':')[0]
        BQSRsite_and_type.add(k)
        m = i.split()[9].split(':')[0]
        if m == '0/0':
            C17zerozero += 1
        elif m == '0/1':
            C17zerone += 1
        elif m == '1/1':
            C17oneone += 1
        else:
            C17other += 1
BQSRzerozero = 0
BQSRzerone = 0
BQSRoneone = 0
BQSRother = 0
for i in f1:
    if i.startswith('#'):
        pass
    else:
        j = ''.join(i.split()[0:4])
        C17site.add(j)
        k = ''.join(i.split()[0:4]) + '-' + i.split()[9].split(':')[0]
        C17site_and_type.add(k)
        m = i.split()[9].split(':')[0]
        if m == '0/0':
            BQSRzerozero += 1
        elif m == '0/1':
            BQSRzerone += 1
        elif m == '1/1':
            BQSRoneone += 1
        else:
            BQSRother += 1

site_intersection = C17site & BQSRsite
siteandtype_intersection = BQSRsite_and_type & C17site_and_type
zerozero = 0
zerone = 0
oneone = 0
other = 0
for i in siteandtype_intersection:
    j = i.split('-')[-1]
    if j == '0/0':
        zerozero += 1
    elif j == '0/1':
        zerone += 1
    elif j == '1/1':
        oneone += 1
    else:
        other += 1

f2.write('\ttotal\t0/0\t0/1\t1/1\tother\nC17\t'+str(len(C17site_and_type))+'\t'+str(C17zerozero)+'\t'+str(C17zerone)+'\t'+str(C17oneone)+'\t'+str(C17other)+'\n'+'C17BQSR\t'+str(len(BQSRsite_and_type))+'\t'+str(BQSRzerozero)+'\t'+str(BQSRzerone)+'\t'+str(BQSRoneone)+'\t'+str(BQSRother)+'\n'+'Intersection\t'+str(len(siteandtype_intersection))+'\t'+str(zerozero)+'\t'+str(zerone)+'\t'+str(oneone)+'\t'+str(other)+'\n')
