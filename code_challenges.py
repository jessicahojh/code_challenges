# Determine if a number is "happy"
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def is_happy(number):

    # if number == 1:
    #     return True

    # else:
    #     number = list(number)
    #     for num in number:

    pass



# Show indexes of even numbers
# [1, 2, 3, 4, 6, 8] ----> [1, 3, 4, 5]

def show_even(lst):

    answer = []
    index = 0 

    for num in lst:
        if num % 2 == 0:
            answer.append(index)
            index = index + 1
        else:
            index = index + 1

    return answer

print(show_even([1, 2, 3, 4, 6, 8]))

# convert snake case to camel case
# 'hello_there' ----> helloThere

def convert_to_camel(string):

    answer = []

    string = string.split("_")
    print(string)

    answer.append(string[0])

    for word in string[1:]:
        word = word.title()
        answer.append(word)


    return ''.join(answer)

print(convert_to_camel("hello_there"))

# find the mode. the mode is the most reoccurring item

def find_mode(lst):

    dictionary = {}

    for num in lst:
        dictionary[num] = dictionary.get(num, 0) + 1

    highest_count = max(dictionary.values())

    mode = set()

    for num, count in dictionary.items():
        if count == highest_count:
            mode.add(num)

    return mode


print(find_mode([1, 2, 2, 2, 3]))  # {2}
print(find_mode([3]))              # {3}
print(find_mode([1, 1, 2, 2]))     # {1, 2}



# find the range of a given list of numbers

def find_range(lst):

    smallest = [lst[0]]
    biggest = [0]

    for num in lst[1:]:
        if num < smallest:
            del smallest[0]
            smallest.append(num)

    for num in lst[1:]:
        if num > biggest:
            del biggest[0]
            biggest.append(num)

    return("(" + smallest + ", " + biggest + ")")


print(find_range([3, 4, 2, 5, 10]))  # (2, 10)
print(find_range([43, 3, 44, 20, 2, 1, 100])) # (1, 100)
print(find_range([7])) # (7, 7)

