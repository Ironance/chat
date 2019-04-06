
#read file
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat

#convertion
def convert(chat_ori):
    name = ''
    chat_new = []
    for line in chat_ori:
        if line == 'Allen':
            name = 'Allen: '
        elif line == 'Tom':
            name = 'Tom: '
        else:
            chat_new.append(name + line + '\n')
    return chat_new

#write file
def write_file(filename, chat_new):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in chat_new:
            f.write(line)

def main():
    chat = read_file('input.txt')
    chat = convert(chat)
    write_file('output.txt', chat)

main()


