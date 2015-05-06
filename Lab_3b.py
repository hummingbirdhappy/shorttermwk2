
for c in 'hello':
	print c

for i in range(len('hello')):
	print i


for i in range(len('hello')):
	print 'hello'[i]


for i in range(1, len('hello'), 2):
	print 'hello'[i]

	

print range(len('hello'))

for c in 'HousE':
	if c in 'hello':
		print 'hello'.replace(c,'-')
	else:
		print c+' is not in hello.'

		

for c in 'HousE':
	c=c.lower()
	if c in 'hello':
		print 'hello'.replace(c,'-')
	else:
		print c+' is not in hello.'

		

s = 'hello'
 
for c in 'HigheR':
	c=c.lower()
	if c in s:
		s=s.replace(c,'-')
		print s
	else:
		print c+' is not in hello.'

j = 0
while 'hello'[j] != 'l':
        print 'value of j is '+str(j)
        print 'The letter at position '+str(j)+' in hello is '+'hello'[j]
        j=j+1



