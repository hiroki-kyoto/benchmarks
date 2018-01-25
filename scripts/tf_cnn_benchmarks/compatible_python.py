# compatible hacking job
def python_version():
    _ver = 0
    str_t = str(type('abc'))
    if str_t[1:5]=='type':
        print('Using python 2.x')
        _ver = 2
    elif str_t[1:6]=='class':
        print('Using python 3.x')
        _ver = 3
    else:
        raise ValueError('Unknown python version used!')
    return _ver

