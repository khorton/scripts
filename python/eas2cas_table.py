#!/sw/bin/python

import airspeed as A

alts=range(39000,-1,-1000)
EASs=range(100,261,10) + [265] + range(270,381,10)

print " CAS |                                                                                     EAS                                                                                     |"
print " hp  |",
for EAS in EASs:
    print " %i|" % (EAS),
print "\n",
for alt in alts:
    print "%5i|" % (alt),
    for EAS in EASs:
        print "%4.0f|" % (A.eas2cas(EAS, alt)),
    print "\n",