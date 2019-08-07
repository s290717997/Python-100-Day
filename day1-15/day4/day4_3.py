"""打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""
#(1)
for col in range(1, 6):
    for raw in range(1, 6):
        if raw <= col:
            print("*", end='')
        pass
    print("")
    pass
pass

#(2)
for col in range(1, 6):
    for raw in range(1, 6):
        if raw < (6 - col):
            print(' ', end='')
        else:
            print("*", end='')
        pass
    print("")
    pass
pass

#(3)
for col in range(1, 6):
    for raw in range(1, 10):
        if raw > 5 - col and raw  < 5 + col:
            print("*", end='')
        else:
            print(' ', end='')
    print("")
    pass
pass