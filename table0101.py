li2 = []
l = int(input("Enter length : "))
n = 2**l

for i in range(n):
	temp = []*l
	li2.append(temp)

c = 2
d = 1
for x in range(l):
	t=0
	for y in range(t, n, c):
		t = y
		if t<n:
			for p in range(d):
				li2[t].insert(0,0)
				t+=1
			for j in range(d):
				li2[t].insert(0,1)
				t+=1
	c*=2
	d *= 2

for x in li2:
	print(x)