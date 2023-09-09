#w.a.p to read PCM and CET score of a student. Determine eligiblity of a student for engineering admission
#Criteria :- PCM >=150, CET>=100.

pcm = int(input('Enter PCM score: '))
if pcm >= 150:
    cet = int(input('Enter CET score: '))
    if cet >= 100:
        print('Student is eligible')
    else:
        print('Student is not eligible')
else:
    print('Student is not eligible')