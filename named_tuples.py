import collections

City = collections.namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (36.689722, 139.691667))
for key, val in tokyo._asdict().items():
    print(f'{key}: {val}')
