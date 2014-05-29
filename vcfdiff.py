#!/usr/lib/python
#-*- coding:utf-8 -*-
f0 = open('CS173.filtered.vcf')
f1 = open('CS66_2.filtered.vcf')
cs173 = set()
cs66 = set()
for i in f0:
    if i.startswith('#'):
        pass
    else:
        j = ''.join(i.split()[0:4])
        cs173.add(j)
for i in f1:
    if i.startswith('#'):
        pass
    else:
        j = ''.join(i.split()[0:4])
        cs66.add(j)
intersection = cs66 & cs173

print len(cs66),len(cs173),len(intersection)
