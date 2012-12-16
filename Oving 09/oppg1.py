videos = [
        'http://www.youtube.com/watch?v=oKI-tD0L18A',
        'http://www.youtube.com/watch?v=82LCKBdjywQ',
        'http://www.youtube.com/watch?v=GpNSip5gyKo',
        'http://www.youtube.com/watch?v=rHG-JO8gIGk',
        'http://www.youtube.com/watch?v=ZFngtBIxRPk',
        'http://www.youtube.com/watch?v=OZBWfyYtYQY'
]

cut_list = []
split_list = []

# If the ID of the videos have the same length.
def cut_last_eleven():
    for item in videos:
        cut_list.append('youtu.be/%s' % item[-11:])
    for i in cut_list:
        print(i)

# To be sure to get everything, you can split every element at the equal sign.
def split_at_equal_sign():
    for item in videos:
        split_list.append('youtu.be/%s' % item.split('=')[1])
    for i in split_list:
        print(i)

# Both fucntions can be implemented in list-comprehention.
def list_comprehention():
    for i in [('youtu.be/%s' % item[-11:]) for item in videos]:
        print(i)

cut_last_eleven()
split_at_equal_sign()
list_comprehention()