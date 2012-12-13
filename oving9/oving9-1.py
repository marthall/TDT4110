videoer = [
	'http://www.youtube.com/watch?v=oKI-tD0L18A',
	'http://www.youtube.com/watch?v=82LCKBdjywQ',
	'http://www.youtube.com/watch?v=GpNSip5gyKo',
	'http://www.youtube.com/watch?v=rHG-JO8gIGk',
	'http://www.youtube.com/watch?v=ZFngtBIxRPk',
	'http://www.youtube.com/watch?v=OZBWfyYtYQY'
]

def main():
	for item in range(len(videoer)):
		videoer[item] = ('youtu.be/%s' % videoer[item][31:])

	for i in videoer:
		print(i)

main()