# Mikhail Anikin
# 2021

available_formatters = ['plain', 'bold', 'italic', 'header', 'link',
                        'inline-code', 'ordered-list', 'unordered-list', 'new-line']

result_string = ''


def save_and_exit():
    exit()


def formatter_plain(text):
    return text


def formatter_bold(text):
    return '**{}**'.format(text)


def formatter_italic(text):
    return '*{}*'.format(text)


def formatter_header(level, text):
    out = ''
    for _ in range(level):
        out += '#'
    out += ' ' + text + '\n'
    return out


def formatter_link(label, url):
    return '[{}]({})'.format(label, url)


def formatter_inline(text):
    return '`{}`'.format(text)


def formatter_new_line():
    return '\n'


def process_format(formatter):
    if formatter == 'plain':
        return formatter_plain(input('Text: '))

    elif formatter == 'bold':
        return formatter_bold(input('Text: '))

    elif formatter == 'italic':
        return formatter_italic(input('Text: '))

    elif formatter == 'header':
        level = int(input('Level: '))
        if level > 6 or level < 1:
            print('The level should be within the range of 1 to 6')
            return ''
        else:
            return formatter_header(level, input('Text: '))

    elif formatter == 'link':
        return formatter_link(input('Label: '), input('URL: '))

    elif formatter == 'inline-code':
        return formatter_inline(input('Text: '))

    elif formatter == 'ordered-list':
        pass
    elif formatter == 'unordered-list':
        pass
    elif formatter == 'new-line':
        return formatter_new_line()


while True:
    income = input('Choose a formatter: ')
    if income == '!help':
        print('Available formatters: ' + ' '.join(available_formatters))
        print('Special commands: !help !done')

    elif income == '!done':
        save_and_exit()

    elif income in available_formatters:
        result_string += process_format(income)
        print(result_string)

    else:
        print('Unknown formatting type or command')
