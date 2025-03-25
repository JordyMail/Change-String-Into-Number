def words_to_number(words):
    num_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000
    }
    words = words.lower().replace('-', ' ').split()
    total, current = 0, 0
    
    for word in words:
        if word in num_words:
            value = num_words[word]
            if value >= 100:
                current *= value
            else:
                current += value
        elif word == "and":
            continue
        else:
            return "Invalid input. Please enter a valid number in words."
    
    total += current
    return total
