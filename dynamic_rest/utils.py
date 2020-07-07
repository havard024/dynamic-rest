
FALSEY_STRINGS = (
    '0',
    'false',
    '',
)


def is_truthy(x):
    if isinstance(x, str):
        return x.lower() not in FALSEY_STRINGS
    return bool(x)


def unpack(content):
    if not content:
        # empty values pass through
        return content

    keys = [k for k in content.keys() if k != 'meta']
    unpacked = content[keys[0]]
    return unpacked
