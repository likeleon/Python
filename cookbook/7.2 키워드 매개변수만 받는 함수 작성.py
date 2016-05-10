def recv(maxsize, *, block):
    'Receives a message'
    pass

#recv(1024, True)
recv(1024, block=True)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))