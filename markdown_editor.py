# Mikhail Anikin
# 2021

available_formatters = ['plain', 'bold', 'italic', 'header', 'link',
                        'inline-code', 'ordered-list', 'unordered-list', 'new-line']


def save_and_exit():
    exit()


while True:
    income = input('Choose a formatter: ')
    if income == '!help':
        print('Available formatters: ' + ' '.join(available_formatters))
        print('Special commands: !help !done')

    elif income == '!done':
        save_and_exit()

    elif income in available_formatters:
        pass

    else:
        print('Unknown formatting type or command')
