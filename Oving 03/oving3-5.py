for i in [a,b,c]:
	i = int("%s: " % i)

d = b*b-(4*a*c)

if d < 0:
	print("Ligningen %ix² + %ix + %i = 0 har to imaginære løsninger" % (a,b,c))
elif d > 0:
	print("Ligningen %ix² + %ix + %i = 0 har to reelle løsnigner" % (a,b,c))
elif d == 0:
	print("Ligningen %ix² + %ix + %i = 0 har én reell dobbelrot" % (a,b,c))