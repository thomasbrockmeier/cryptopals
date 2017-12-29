import string


def hex2bytes(h):
    """Convert to 'bytes': (00100101) and join"""
    return ''.join([
        bin(int(h[i * 2:i * 2 + 2], 16)).strip('0b').zfill(8)
        for i in range(len(h) // 2)
    ])


def hex2b64(h):
    """Convert bytes string to base64"""
    legend = (
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        '+/',
    )

    b = hex2bytes(h)

    return ''.join([legend[int(b[x*6:x*6+6], 2)] for x in range(len(b) // 6)])
