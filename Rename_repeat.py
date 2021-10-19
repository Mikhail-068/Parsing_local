a = []
name = 'link.txt'
count = 0


def fun_copy(a, count=count, name=name):
    while count < 10:
        if name in a:
            if f'{count - 1}'.join(name.split('.')) in a:
                name = name.replace(f'({count - 1})', '.')
                name = f'({count})'.join(name.split('.'))
            else:
                name = f'({count})'.join(name.split('.'))

            a.append(name)
        else:
            a.append(name)
        count += 1
    return a


fun_copy(a)
print(a)
