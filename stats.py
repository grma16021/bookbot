def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

def count_chars(file_contents):
    lowerCaseWords = file_contents.lower()
    counts = {}
    for ch in lowerCaseWords:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1
    print_results(counts)
    

def sort_on(items):
    return items["num"]


def print_results(count_dict):
    someList = []
    for key in count_dict:
        someList.append({"char": key, "num": count_dict[key]})
        

    someList.sort(reverse=True, key=sort_on)
    for item in someList:
        if item["char"].isalpha():
            print(item["char"]+":" + " " + str(item["num"]))
        else:
            continue
    print("============= END ===============")




