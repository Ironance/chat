
#read file
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat


#convertion
def convert(chat_ori):
    name = None
    chat_new = []
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0

    for line in chat_ori:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
               for msg in s[2:]:
                    allen_word_count += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for msg in s[2:]:
                    viki_word_count += len(msg)
    print('Allen said', allen_word_count, 'words, sent', allen_sticker_count, 'stickers and', allen_image_count, 'images.')
    print('Viki said', viki_word_count, 'words, sent', viki_sticker_count, 'stickers and', viki_image_count, 'images.')


#write file
def write_file(filename, chat_new):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in chat_new:
            f.write(line)


def main():
    chat = read_file('-LINE-Viki.txt')
    chat = convert(chat)
    # write_file('output.txt', chat)


main()


