def mergesort(l):
	n = len(l)
	if n == 1:
		return(l)
	else:
		d = mergesort(l[0:n//2])
		e = mergesort(l[n//2:])
		return(merge(d,e))

def more(s,d):
	for i in range(min(len(s) , len(d))):
		if s ==d:
			return(2)
		elif s[i] < d[i]:
			return(1)
		elif s[i] > d[i]:
			return(0)
		else:
			if i == min(len(s) , len(d)) - 1 and len(s) < len(d):
				return(1)
			elif i == min(len(s) , len(d)) - 1 and len(s) > len(d):
				return(0)
			else:
				pass

def merge(l ,r):
	(c,m ,n) = ([] , len(l) , len(r))
	(i,j) =(0,0)
	while i+j < m+n:
		if i ==m:
			c.append(r[j])
			j += 1
		elif j == n:
			c.append(l[i])
			i+=1
		elif more(l[i] , r[j]) == 1:
			c.append(l[i])
			i+=1
		elif more(l[i] , r[j]) == 0:
			c.append(r[j])
			j+=1
		elif more(l[i] , r[j]) == 2:
			c.append(l[i])
			c.append(r[j])
			i+=1
			j+=1
		else:
			pass
	return(c)

def ans(l):
	a = 1
	d={}
	for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		d[i] = a
		a+=1 
		maincount = 0
	for i in range(len(l)):
		count = 0
		for j in range(len(l[i])):
			count = count + d[l[i][j]]
		maincount = maincount + (count * (i+1)) 
	return(maincount)