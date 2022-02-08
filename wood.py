print 'Welcome to my Program.'
a=400
b=float(input('\n\033[1;33;40mPrice of 1 ton in Kyats \033[1;32;40m >> '));
d=float(input('\033[1;33;40mArea of wood in Inches \033[1;32;40m >> '));
e=float(input('\033[1;33;40mLength of wood in Feets \033[1;32;40m >> '));
g=d*e/18
h=g*(b/a)
print '\n\033[1;33;40mInches is \033[1;32;40m>> ',g, '\033[1;33;40mand Prices is \033[1;32;40m>> ',h
i=float(input('\n\033[1;33;40mNumber of wood Items \033[1;32;40m >> '));
j=i*h
print '\n\033[1;33;40mThe prices of ',i,'is \033[1;32;40m>> ',j
print '\nThank for using.'
