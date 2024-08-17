#a
print("a".center(110, "-"))
tuple1: tuple[int] = (99,)
print(tuple1)

#b
print("b".center(110, "-"))
tuple2: tuple[int] = (77,88,99)
print(tuple2)

#c
print("c".center(110, "-"))
def tuple_len (tuple3:tuple = "") -> int:
    tuple3:tuple = tuple(input("Please enter a string"))
    return len(tuple3)

print(tuple_len())

#d
print("d".center(110, "-"))
def two_tuples (first_tuple: tuple = "", second_tuple: tuple = "") -> tuple:
    first_tuple:tuple = tuple(input("Please enter your first tuple"))
    second_tuple:tuple = tuple(input("Please enter your second tuple"))
    tuple_combined: tuple = first_tuple+second_tuple
    return tuple_combined
print(two_tuples())

#e
print("e".center(110, "-"))
def tuple_identical (tuple_one: tuple = "", tuple_two: tuple = "") -> tuple:
    tuple_one:tuple = tuple(input("Please enter a string or some numbers"))
    tuple_two:tuple = tuple(input("Again please"))
    tuple_identical = f"The identical digits or characters you entered are:",tuple(filter(lambda x: x in tuple_one, tuple_two))
    return tuple_identical
print(tuple_identical())

#f
print("f".center(110, "-"))

def different_tuple (first_tuple: tuple = "", second_tuple: tuple = "") -> tuple:
    first_tuple: tuple = tuple(input("Please enter a string or some numbers"))
    second_tuple: tuple = tuple(input("Again enter a string or some numbers"))
    different_tuple_first = tuple(filter(lambda x: x not in first_tuple , second_tuple))
    different_tuple_second = tuple(filter(lambda x: x not in second_tuple, first_tuple))
    different_tuple: tuple = f"The numbers or characters that are different in your tuples are:", different_tuple_first+different_tuple_second
    return different_tuple
print(different_tuple())

#g
print("g".center(110, "-"))

def tuple_index (input_tuple: tuple = "", input_index: int = 0) -> str:
    try:
        input_tuple: tuple = tuple(input("Please enter your word or numbers"))
        input_index: int = int(input("In which index number do you choose?"))
        tuple_index: str = f"The value in index no. {input_index} is: {input_tuple[input_index]}"
        return tuple_index
    except:
        return "None"

print(tuple_index())

#h
print("h".center(110, "-"))

def reverse_tuple (the_tuple: tuple = "") -> tuple:
    tuple_input:tuple = tuple(input("Please enter your tuple!!"))
    reverse_tuple:tuple = tuple(reversed(tuple_input))
    return reverse_tuple
print(reverse_tuple())

#i
print("i".center(110, "-"))


def divisable_tuple (number: int = 0, tuple_input: tuple = "") -> int:
    try:
        number:int = int(input("Please enter a number"))
        user_input:str = str(input("please enter some numbers divided by spaces, baby!"))
        tuple_input:tuple = tuple(map (int,user_input.split()))
        divisable: int = sum ( 1 for x in tuple_input if number % x == 0)
    except:
        return "Only numbers please"
    return divisable

print(divisable_tuple())


#j
print("j".center(110, "-"))
def multiply_tuple (mul: int = 0, a_tuple: tuple = "") -> tuple:
    try:
        num:int = int(input("Enter a number please"))
        a_tuple:tuple = tuple(input("Please enter a tuple..."))
        mul_tuple =num*a_tuple
        return mul_tuple
    except:
        return "something went wrong..."
print(multiply_tuple())

#k
print("k".center(110, "-"))

def enumerate_tuple (the_tuple: tuple = "") -> tuple:
    user_input:str = str(input("Please enter a tuple of fruits divided by spaces"))
    the_tuple:tuple = tuple(user_input.split())
    enumerate_tuple:tuple = tuple(enumerate(the_tuple))
    return enumerate_tuple
print(enumerate_tuple())

#l
print("l".center(110, "-"))

def tuple_to_dict (nums: str = "") -> dict:
    import statistics
    try:
        nums:str = str(input("Please enter a list of numbers divided by spaces"))
        numbers = tuple(map(int, nums.split()))
    except:
        return "Only numbers please!"

    max_nums = max(numbers)
    min_nums = min(numbers)
    avg_nums = statistics.mean(numbers)
    nums_len = len(numbers)
    nums_sorted = sorted(numbers)
    sorted_descend = sorted(numbers, reverse = True)

    analysis:dict =  {
        "Max Number": max_nums,
        "Min Number": min_nums,
        "Numbers Average": avg_nums,
        "Numbers Quantity": nums_len,
        "Numbers Sorted": nums_sorted,
        "Numbers Sorted Backwards": sorted_descend,
        "Numbers Repetition": {nums: numbers.count(nums) for nums in numbers}
    }

    return analysis
print(tuple_to_dict())


#m
print("m".center(110, "-"))

def letters_to_word (letters: tuple = ("")) ->tuple:
    letters:str = str(input("Please enter a tuple of characters divided by spaces"))
    word:tuple = tuple(letters.split())
    word = letters.replace(" ", "")
    return word

print(letters_to_word())


#n
print("n".center(110, "-"))

def letters_to_word (letters: str = "") ->tuple:
    letters:str = str(input("Please enter a string of characters"))
    word:tuple = tuple(letters)
    return word

print(letters_to_word())


#o
print("o".center(110, "-"))
def tuple_without_number (my_tuple:str = "", num:int = 0) -> tuple:
    my_tuple:str = str(input("Please enter a tuple of numbers divided by spaces"))
    my_tuple_revised:tuple = tuple(my_tuple.split())
    num:str = str(input("Please enter a number. Make sure your number is in the tuple you entered before"))
    finished_tuple:tuple = tuple(filter(lambda x:  x !=num, my_tuple_revised))
    return finished_tuple

print(tuple_without_number())


#p
print("p".center(110, "-"))

def no_duplicate_tuple (a_tuple: str = "") -> tuple:
    a_tuple:str = str(input("please enter a list of characters"))
    a_tuple_list = list(a_tuple.split())
    a_tuple_set = set(a_tuple_list)
    finished_tuple:tuple = tuple(a_tuple_set)
    return print(finished_tuple)

print(no_duplicate_tuple())


#q
print("q".center(110, "-"))

def indexing_tuple (user_tuple: str = "", user_num:int = 0) -> tuple:
    user_tuple: str = str(input("Please enter a tuple of numbers"))
    user_num: int = int(input("Now please enter a number. Make sure your number exists in the original tuple"))
    user_tuple_fixed = tuple(map(int, user_tuple.split()))
    tuple_index: tuple = tuple(i for i,v in enumerate(user_tuple_fixed) if v == user_num)
    return tuple_index

print(indexing_tuple())


#r
print("r".center(110, "-"))

def names_and_grades (names: tuple = "", grades: str = 0):
    names_list = []
    grades_list = []
    while True:
        names = input("Enter a name (type 'done' to finish):")
        if names.lower() == 'done':
            break
        names_list.append(names)

    while True:
        grades: str = str(input("Plese enter the grades for your students (type '-999' to finish):"))
        if grades == "-999":
            break
        grades_list.append(grades)

    names_tuple: tuple = tuple(names_list)
    grades_tuple: tuple = tuple(grades_list)
    names_and_grades = zip(names_tuple, grades_tuple)
    return tuple(names_and_grades)

print(names_and_grades())




