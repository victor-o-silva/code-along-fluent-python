metro_areas = [
    ('Tokyo', 'JP', 36.993, (35.689722, 139.691667))
]

fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
