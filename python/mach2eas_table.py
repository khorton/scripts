#!/sw/bin/python

import airspeed as A

alts=range(39000,-1,-1000)
Ms=range(30, 79, 2) + [79] + [80, 82, 84, 85]

print " EAS |                                                                                        Mach                                                                                       |"
print " hp  |",
for M in Ms:
    print "%0.2f|" % (M / 100.),
print "\n",
for alt in alts:
    print "%5i|" % (alt),
    for M in Ms:
        CAS = A.mach_alt2cas(M/100., alt)
        print "%4.0f|" % (A.cas2eas(CAS, alt)),
    print "\n",