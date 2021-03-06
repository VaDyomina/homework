#coding = utf-8

def opening(name):
    words = []
    with open (name, 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def counting(words):
    count_with = 0
    count_without = 0
    omnis = []
    non_omnis = []
    omnis_samples = []
    non_omnis_samples = []
    for i in range(len(words)):
        if words[i].startswith("omni"):
            count_with += 1
            omnis.append(words[i])
            if words[i] not in omnis_samples:
                omnis_samples.append(words[i])
    for word in omnis_samples:
        word_new = word[4:]
        non_omnis_samples.append(word_new)
        for i in range(len(words)):
            if word_new == words[i]:
                count_without += 1
                non_omnis.append(words[i])
    print("С приставкой -omni встретилось", count_with, "слов(а).")
    print("---------------------------------------------------------")
    for word in omnis_samples:
        a = omnis.count(word)
        print("Для слова", word, "встретилось", a, "примера(ов).")
    print("----------------------------------------------------------")
    print("Тех же слов, но без приставки -omni встретилось", count_without, "штук(и).")
    if count_without != 0:
        print("----------------------------------------------------------")
        for word in non_omnis_samples:
            a = non_omnis.count(word)
            if a != 0:
                print("Для слова", word, "встретилось", a, "примера(ов).")

def main():
    counting(opening(input('Введите имя файла: ')))

main()
