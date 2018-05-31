#!/sw/bin/python

import airspeed as A

alts=range(39000,-1,-1000)
CASs=range(100,381,10)

print " EAS |                                                                         CAS"
print " hp  |",
for CAS in CASs:
    print " %i|" % (CAS),
print "\n",
for alt in alts:
    print "%5i|" % (alt),
    for CAS in CASs:
        print "%4.0f|" % (A.cas2eas(CAS, alt)),
    print "\n",