words = ["about","after", "again", "below", "could", "every", "first", "found",
         "great", "house", "large", "learn", "never", "other", "place", "plant",
         "point", "right", "small", "sound", "spell", "still", "study", "their",
         "there", "these", "thing", "think", "three", "water", "where", "which",
         "world", "would", "write"]


uhh = ["s","f","p","v","q","j","i","e","t","q","f","g","m","i","g","r","e","q",
       "l","y","x","c","f","j","f","a","p","r","t","l"]

def printList(num):
    for x in num:
        print (x)

def sumL(numbers):
    total = 0
    for x in numbers:
        total += 1
    return total

def compare(word, checker):
    index = 0

    c = 0
    for u in word:

        for x in checker[index]:
          
            if u == x:
                c += 1
                break

        index += 1
        if (c < index):
            return False
        
    if (c >= 5):
        return True



def check(arr):
    index = 0
    temp = 0
    counter = 0

    while sumL(words) != 1:
        word = words[0]

        temp = 0

  
        if (compare(word, arr)):
            break

        words.pop(0)
        counter = 0


    print("The word is:  ", words[0])

def getInput(arr, uhh):
    hey = []
    index = 0
    changed = False

    while (sumL(arr) != 5):

        hey = []
        index = 1
        while (sumL(hey) != 6):
            s = str(index) + "th number: "

            num = input(s)

            if (num == "oops"):
                last = hey[-1]
                changed = True
                index -= 1
                continue

            if (changed):
                print("Changed ", last, " to ", num)
                changed = False
            
            index += 1
            hey.append(num)


        arr.append(hey)


stuff = []

getInput(stuff,uhh)
check(stuff)


