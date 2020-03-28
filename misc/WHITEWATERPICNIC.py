
"""
brute force solving 'WHITE' + 'WATER' = 'PICNIC'

"""
for i0 in range(10): # A
    for i1 in range(10): # C
        for i2 in range(10): # E
            for i3 in range(10): # H
                for i4 in range(10): # I
                    for i5 in range(10): # N
                        for i6 in range(10): # P
                            for i7 in range(10): # R
                                for i8 in range(10): # T
                                    for i9 in range(10): # W
                                        if i9*2*10**4+(i3+i0)*10**3+(i4+i8)*10**2+(i8+i2)*10+i2+i7==\
                                        i6*10**5+i4*(10**4+10)+i1*(10**3+1)+i5*10**2 \
                                        and i9 not in [i0,i1,i2,i3,i4,i5,i6,i7,i8] \
                                        and i8 not in [i0,i1,i2,i3,i4,i5,i6,i7,i9] \
                                        and i7 not in [i0,i1,i2,i3,i4,i5,i6,i9,i8] \
                                        and i6 not in [i0,i1,i2,i3,i4,i5,i9,i7,i8] \
                                        and i5 not in [i0,i1,i2,i3,i4,i9,i6,i7,i8] \
                                        and i4 not in [i0,i1,i2,i3,i9,i5,i6,i7,i8] \
                                        and i3 not in [i0,i1,i2,i9,i4,i5,i6,i7,i8] \
                                        and i2 not in [i0,i1,i9,i3,i4,i5,i6,i7,i8] \
                                        and i1 not in [i0,i9,i2,i3,i4,i5,i6,i7,i8] \
                                        and i0 not in [i9,i1,i2,i3,i4,i5,i6,i7,i8] :
                                            print(''.join([str(i9),str(i3),str(i4),str(i8),str(i2)]) + ' + ' +\
''.join([str(i9),str(i0),str(i8),str(i2),str(i7)]) + " = " +\
''.join([str(i6),str(i4),str(i1),str(i5),str(i4),str(i1)]))