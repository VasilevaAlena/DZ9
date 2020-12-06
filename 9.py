def read_files_json(name):
    import json
    with open(name, 'rb') as f:
        data = json.load(f)
        description_text = str()
        for items in data['rss']['channel']['items']:
            description_text += items['description']
        return description_text

def read_files_xml(name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(name, parser)
    root = tree.getroot()
    news_xml = root.findall("channel/item")
    all_descr = []
    for news in news_xml:
        descr = news.find("description")
        all_descr.append(descr.text)
        description_text = str(all_descr)
    return description_text


def count_word(description_text):
    to_list = description_text.split(' ')
    word_dict = {}
    for word in to_list:
        if len(word) > 6:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


def sort_top(word_dict):
    sorted_by_value = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)
    count = 0
    top_10 = {}
    for word in sorted_by_value:
        top_10[count] = word
        count += 1
        if count == 10:
            break
    return top_10


def main():
    while True:
        name = input('Введите имя файла (newsafr.json или newsafr.xml): ')
        if name == 'newsafr.json':
            top_10 = sort_top(count_word(read_files_json(name)))
            for i in top_10.values():
                print(f'{i[0]} : {i[1]}')
        elif name == 'newsafr.xml':
            top_10 = sort_top(count_word(read_files_xml(name)))
            for i in top_10.values():
                print(f'{i[0]} : {i[1]}')
        else:
            break

main()