#Betal Program
print('Welcome to Betal Calculate Program\n')

a=float(input('\nEnter 1st entries (Viss) : '))
a1=float(input('\nEnter 2nd entries (Viss) : '))
a2=float(input('\nEnter 3rd entries (If not exist enter 0) : '))
a3=float(input('\nEnter 4th entries (If not exist enter 0) : '))

aplus=a+a1+a2+a3

a4=float(input('\nEnter Basket weight (Viss) : '))

aplus1=aplus-a4

aplus2=aplus1*0.1

aplus3=aplus1-aplus2

a6=float(input('\033[1;32;40m\nEnter Betal Price (Kyats) : '))

result=aplus3*a6

print('')

print '\n\033[1;33;40mThe Total Weight is (Viss) : ',aplus

print('')

print '\n\033[1;33;40mThe Basket Weight is (Viss) : ',a4

print('')

print '\n\033[1;33;40mThe Water Weight is (Viss) : ',aplus2

print('')

print '\033[1;32;40m\nThe Value is (Kyats) : ',result

print('')

print('#END Program !')

#Complete
