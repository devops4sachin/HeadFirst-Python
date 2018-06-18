paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t'*3, char)

""" gives output as below
         M
         a
         r
         v
         i
         n

                 A
                 n
                 d
                 r
                 o
                 i
                 d

                         P
                         a
                         r
                         a
                         n
                         o
                         i
                         d
"""
