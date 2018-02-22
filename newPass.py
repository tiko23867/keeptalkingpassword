
uhh = ["s","f","p","v","q","j","i","e","t","q","f","g","m","i","g","r","e","q",
       "l","y","x","c","f","j","f","a","p","r","t","l"]


def printList(num, s=""):
    print(s,end='')
    for x in num:
        print (x)

def compare(words, inpu, index):
    match = []
    for word in words:
        if word[index] in inpu:
            match.append(word)

    return match


words = ["about","after", "again", "below", "could", "every", "first", "found",
         "great", "house", "large", "learn", "never", "other", "place", "plant",
         "point", "right", "small", "sound", "spell", "still", "study", "their",
         "there", "these", "thing", "think", "three", "water", "where", "which",
         "world", "would", "write"]

inpu = []
delete = 0
index = 0
changed = False

oops = ["oops", "ooops", "oooops", "opps"]

while len(words) != 1:
    inpu = []
    count = 1
    print("\nPosition",index + 1)

    while len(inpu) != 6:
        s = str(count) + "th number: "
        letter = input(s)

        if letter in oops and changed == False:
            if len(inpu) < 1:
                print("Cannot change something you did not enter")
                continue

            last = inpu[-1]
            changed = True
            count -= 1
            continue

        if len(letter) > 1 or letter.isalpha() is False:
            print("Needs to be one alphabet charcter")
            continue

        if changed:
            print("Changed", last, "to", letter)
            changed = False

        inpu.append(letter)
        #inpu.append(uhh[delete])
        #print("Input = ",uhh[delete])
        delete += 1
        count += 1

    words = compare(words, inpu,index)
    printList(words,'\n')
    index += 1
