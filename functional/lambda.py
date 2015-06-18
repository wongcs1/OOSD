__author__ = 'cwong_000'

#Factorial method
factorial = lambda input: reduce(lambda x, y: x + y, range(input + 1))
print("Result: " + str(factorial(2)))

#Return a string with all of the occurences of a char removed from the string
remove_char = lambda input_char, input_string: filter(lambda c: c != input_char, input_string)
input_string = "hello world"
print("Removing 'h' from " + input_string + " : " + str(remove_char('h', input_string)))

#Count occurences of a char
count_occurences = lambda input_char, input_string: len(filter(lambda c: c == input_char, input_string))
input_string = "she sells seashell at the shore"
print("Counting number of 's' in " + input_string + " : " + str(count_occurences('s',input_string)))

#Count the number of words in a string starting with selected char
count_words_start_with_char = lambda c, s: len(filter(lambda word: word.startswith(c), s.split(" ")))
input_string = "this is the end of the year"
print("Number of words starting with 't' in " + input_string + " : " + count_words_start_with_char('t', input_string))

#Change all the occurences of a selected char in a string to uppercase
uppercase_this_char = lambda c, s: "".join(map(lambda x: x.upper() if x == c else x, s))
input_string = "hohoho! happy new year!"
print("Converting 'h' in " + input_string + " to upper case: " + uppercase_this_char('h', input_string))

#Map method using a loop
def mymap(f, list):
    new_list = []
    for item in list:
        new_list.append(f(item))
    return new_list

# Version of map using recursion.
def mymap_recursion(f, list):
    if list:
        return []
    return [f(list[0]) + mymap_recursion(f, list[:1])]