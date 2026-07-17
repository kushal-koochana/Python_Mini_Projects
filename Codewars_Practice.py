def alternating_character(character):
    if character.isupper():
        character = character.lower()
    elif character.islower():
        character = character.upper()
    else:
        character = character
    return character


def alternating_string(string):
    result = ""
    for i in string:
        j = alternating_character(i)
        result += j
    return result



def return_five():
    result = len("fifty")
    return result



FIRST_NAME = {
    "A": "Alice",
    "B": "Brian",
    "C": "Claire",
    "D": "David",
    "E": "Emma",
    "F": "Frank",
    "G": "Grace",
    "H": "Henry",
    "I": "Ivy",
    "J": "James",
    "K": "Karen",
    "L": "Liam",
    "M": "Mia",
    "N": "Noah",
    "O": "Olivia",
    "P": "Peter",
    "Q": "Quinn",
    "R": "Rachel",
    "S": "Samuel",
    "T": "Tina",
    "U": "Ulysses",
    "V": "Vera",
    "W": "William",
    "X": "Xander",
    "Y": "Yara",
    "Z": "Zoe",
}

SURNAME = {
    "A": "Anderson",
    "B": "Bennett",
    "C": "Clark",
    "D": "Davis",
    "E": "Edwards",
    "F": "Foster",
    "G": "Garcia",
    "H": "Hughes",
    "I": "Ingram",
    "J": "Jackson",
    "K": "Klein",
    "L": "Lopez",
    "M": "Mitchell",
    "N": "Nelson",
    "O": "Owens",
    "P": "Parker",
    "Q": "Quincy",
    "R": "Reed",
    "S": "Smith",
    "T": "Turner",
    "U": "Underwood",
    "V": "Vargas",
    "W": "White",
    "X": "Xi",
    "Y": "Young",
    "Z": "Zimmerman",
}


def format_each_name(name_bit):
    name_bit = name_bit.strip()
    name_bit = name_bit.title()
    return name_bit


def alias_gen(f_name, l_name):
    f_name = format_each_name(f_name)
    l_name = format_each_name(l_name)
    if f_name[0].isalpha() and l_name[0].isalpha():
        first_name = FIRST_NAME[f_name[0]]
        last_name = SURNAME[l_name[0]]
        result = f"{first_name} {last_name}"
    else:
        result = "Your name must start with a letter from A - Z."
    return result



def verify_int(value, value_type):
    if value_type == str:
        try:
            if "." in value:
                value = float(value)
            else:
                value = int(value)
        except ValueError:
            return f"Error, sorry please ensure there are actual numbers in your list, i.e. unable to typecast string {value}"
        else:
            return value
    elif value_type == float or value_type == int:
        return value
    else:
        return f'Error, mate wot kind of data type we using again: "{value}"?'


def loop_through_list(random_list):
    empty_var = ""
    true_list = []
    if random_list:
        for i in random_list:
            j = type(i)
            check = verify_int(i, j)
            true_list.append(check)
            if type(check) == str:
                empty_var = check
        if empty_var:
            return empty_var
        else:
            return true_list
    else:
        true_list.append(0)
        return true_list


def calculate_average(a_list):
    a = loop_through_list(a_list)
    if type(a) != str:
        full_sum = 0
        length = len(a_list)
        for true_element in a:
            full_sum += true_element
        result = full_sum / length
        return result
    else:
        return a



def wrap(value):
    return {"value": value}



def summation(num):
    result = (num * (num + 1)) / 2
    return result



def move(org_pos, roll):
    new_pos = org_pos + 2 * roll
    return new_pos



def convert_lower(string):
    string = str(string)
    string = string.lower()
    return string


def test_english(a):
    if "english" in convert_lower(a):
        return True
    else:
        return False



def divisible_by_2(num):
    try:
        if num % 2 == 0:
            return "even"
        elif num % 2 != 0:
            return "odd"
        else:
            return "never happens..."
    except TypeError:
        return None


def simple_output(num_2):
    x = divisible_by_2(num_2)
    if x:
        if x == "even":
            return x * 8
        elif x == "odd":
            return x * 9
        else:
            return None
    else:
        return "incorrect input"



dict_hex_dec = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def determine_string(value):
    if type(value) == str:
        return True
    else:
        return False


def work_out_length(hex_num):
    if determine_string(hex_num):
        count = len(hex_num) - 1
        return count
    else:
        return None


def hex_to_dec(hex_num):
    if type(work_out_length(hex_num)) == int:
        result = 0
        count = work_out_length(hex_num)
        for i in hex_num:
            result += dict_hex_dec[i] * (16**count)
            count -= 1
        return result
    else:
        return "Sorry please input correct data type"



def verify_all_num(num_list):
    x = 1
    for i in num_list:
        if type(i) != int:
            x = 0
    if x:
        return True
    else:
        return False


def identify_different_number_in_consecutive_chain(num_list):
    length = len(num_list)
    if verify_all_num(num_list):
        if length < 1:
            return None
        else:
            for i in range(1, length):
                if num_list[i] - num_list[i - 1] != 1:
                    return num_list[i]
            return None
    else:
        return "Not all the numbers are of the integer data type..."



def sakura_fall(v):
    if v <= 0:
        return 0
    else:
        time_taken = 400 / v
        return time_taken



def ensure_time_correct(time):
    while not 0 <= time < 24:
        if time >= 24:
            time -= 24
        elif time < 0:
            time += 24
    return time


def was_package_received_yesterday(tz_from, tz_to, start, duration):
    x = "day b"
    y = "day b"
    if tz_to > tz_from:
        return False
    else:
        start_at_to = start - abs(tz_from - tz_to)
        if not 0 <= start_at_to < 24:
            y = "day a"
        start_at_to = ensure_time_correct(start_at_to)
        end_at_from = start + duration
        if not 0 <= end_at_from < 24:
            x = "day c"
        end_at_to = start_at_to + duration
        if not 0 <= end_at_to < 24:
            y = "day c"
        if x == "day b" and y == "day a":
            return True
        else:
            return False



class Hero(object):
    def __init__(self, name="Hero"):
        self.name = name
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0



def remove_char(s):
    altered = s[1:-1]
    return altered




def true_float_or_not(n):
    if n[-2:] == ".0":
        return True
    else:
        return False


def check_square(n):
    n **= 0.5
    n = str(n)
    return true_float_or_not(n)


def is_square(n):
    if type(n) != int:
        return False
    elif n < 0:
        return False
    else:
        return check_square(n)


def factor_through(n):
    for i in range(
        1,
        int(
            round(
                n * 0.5,
            )
        )
        + 1,
    ):
        if n % i == 0:
            if n / i == i:
                return True
            else:
                continue
    return False


def is_square_2(n):
    if type(n) != int:
        return False
    elif n < 0:
        return False
    elif n == 0:
        return True
    else:
        return factor_through(n)



def loopy_code(n):
    n = int(n)
    n **= 2
    return n


def square_digits(num):
    if type(num) != int:
        return "Wrong input..."
    elif num < 0:
        return "Wrong input..."
    else:
        result = ""
        num = str(num)
        for character in num:
            result += str(loopy_code(character))
        return int(result)



def two_decimal_places(number):
    string_num = f"{number}"
    important = string_num.index(".")
    return float(string_num[: important + 3])



def remove_all_instances(item, items_list):
    while item in items_list:
        items_list.remove(item)
    return items_list


def two_oldest_ages(ages):
    age_1 = max(ages)
    ages = remove_all_instances(age_1, ages)
    age_2 = max(ages)
    return [age_2, age_1]



def sum_two_smallest_numbers(numbers):
    num_1 = min(numbers)
    numbers = remove_all_instances(num_1, numbers)
    num_2 = min(numbers)
    return num_2 + num_1


def sum_two_smallest_numbers_2(numbers):
    numbers = sorted(numbers)
    numbers_2 = numbers[:2]
    return sum(numbers_2)



def calculate_product(num_list):
    full_product = 1
    for i in num_list:
        full_product *= i
    return full_product


def each_element_calculation(element, num_list):
    full_product = calculate_product(num_list)
    final_ans = int(full_product / element)
    return final_ans


def product_array(num_list):
    product_list = []
    for j in num_list:
        final_ans = each_element_calculation(j, num_list)
        product_list.append(final_ans)
    return product_list



def each_digit_computation(element, power):
    value = element * (2**power)
    return value


def binary_array_to_number(arr):
    power = len(arr) - 1
    result = 0
    for i in arr:
        result += each_digit_computation(i, power)
        power -= 1
    return result



def remove_used_elements(list_0, no_1, no_2):
    list_0.remove(no_1)
    list_0.remove(no_2)


def min_sum(arr):
    result = 0
    while arr:
        num_1 = max(arr)
        num_2 = min(arr)
        result += num_1 * num_2
        remove_used_elements(arr, num_1, num_2)
    return result



def detect_each_number(element, mixed_str):
    temp_index = mixed_str.index(element)
    true_value = mixed_str[:temp_index]
    return [true_value, temp_index]


def attaching_integer_element(empty_list, element):
    empty_list.append(int(element))
    return empty_list


def format_list(assorted_str):
    assorted_str += " "
    true_num_list = []
    for i in assorted_str:
        if i == " ":
            true_value = detect_each_number(i, assorted_str)[0]
            true_num_list = attaching_integer_element(true_num_list, true_value)
            temp_index = detect_each_number(i, assorted_str)[1]
            assorted_str = assorted_str[temp_index + 1 :]
        else:
            continue
    return true_num_list


def high_and_low(assorted_str):
    true_num_list = format_list(assorted_str)
    high_num = max(true_num_list)
    low_num = min(true_num_list)
    return f"{high_num} {low_num}"



def adding_up(result, integer):
    result += integer
    return result


def looping_and_summing(element):
    result = 0
    n_element = int(element)
    result = adding_up(result, n_element)
    return result


def comparison_check(result_a, result_b):
    if result_a == result_b:
        return "Balanced"
    else:
        return "Not Balanced"


def balanced_num(number):
    number = str(number)
    if len(number) == 1 or len(number) == 2:
        return "Balanced"
    else:
        if len(number) % 2 == 0:
            result_1, result_2 = 0, 0
            crit_val = int(len(number) / 2) - 1
            left_side = number[:crit_val]
            right_side = number[crit_val + 2 :]
            for i in left_side:
                result_1 = looping_and_summing(i)
            for i in right_side:
                result_2 = looping_and_summing(i)
            return comparison_check(result_1, result_2)
        else:
            result_3, result_4 = 0, 0
            crit_val = int((len(number) + 1) / 2) - 1
            left_side = number[:crit_val]
            right_side = number[crit_val + 1 :]
            for i in left_side:
                result_3 = looping_and_summing(i)
            for i in right_side:
                result_4 = looping_and_summing(i)
            return comparison_check(result_3, result_4)



def comparison_test(test_suit_a, test_suit_b):
    if test_suit_a != test_suit_b:
        return False
    else:
        return True


def is_flush(cards):
    result = True
    test_suit_1 = cards[0][-1]
    for card in cards:
        test_suit_2 = card[-1]
        result = comparison_test(test_suit_1, test_suit_2)
        if not result:
            break
        else:
            continue
    return result



def solution(pairs):
    result = ""
    for key, value in pairs.items():
        result += f"{key} = {value},"
    result = result[:-1]
    return result



def append_index(index, index_list):
    index_list.append(index)
    return index_list


def verifying_character_case(character, random_str, index_list):
    if character.isupper():
        temp_index = random_str.index(character)
        index_list = append_index(temp_index, index_list)
        return [True, index_list, temp_index]
    else:
        return False


def avoiding_duplicates(random_str, temp_index):
    random_str = random_str[:temp_index] + "1" + random_str[temp_index + 1 :]
    return random_str


def indexes_capitals(random_str):
    capital_index_list = []
    for i in random_str:
        a = verifying_character_case(i, random_str, capital_index_list)
        if a:
            capital_index_list = a[1]
            random_str = avoiding_duplicates(random_str, a[2])
        else:
            continue
    return capital_index_list



def dealing_with_single_vowel_occurrence_in_string(string__, vowel__):
    temp_index = string__.index(vowel__)
    string__ = string__[:temp_index] + string__[temp_index + 1 :]
    return string__


def dealing_with_single_vowel(vowel_, string_):
    while vowel_ in string_:
        string_ = dealing_with_single_vowel_occurrence_in_string(string_, vowel_)
    return string_


def disemvowel(string):
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowel_list:
        string = dealing_with_single_vowel(vowel, string)
    return string



def detect_word_lengths_in_string(string_):
    temp_index = string_.index(" ")
    word = string_[:temp_index]
    length = len(word)
    return [word, length, temp_index]


def add_word_with_length(dictionary, word, length):
    dictionary[word] = length
    return dictionary


def modify_string(temp_index_, s_):
    s_ = s_[temp_index_ + 1 :]
    return s_


def find_short(s):
    dict_lengths_words = {}
    s += " "
    while " " in s:
        three_outputs = detect_word_lengths_in_string(s)
        dict_lengths_words = add_word_with_length(
            dict_lengths_words, three_outputs[0], three_outputs[1]
        )
        s = modify_string(three_outputs[2], s)
    return min(dict_lengths_words.values())



def check_duplicate_character_in_string(character_, string__):
    if character_ in string__:
        return False
    else:
        return True


def dealing_each_character(character, string_):
    temp_index = string_.index(character)
    string_ = string_[:temp_index] + string_[temp_index + 1 :]
    verification_for_duplicates = check_duplicate_character_in_string(
        character, string_
    )
    return verification_for_duplicates


def is_isogram(string):
    string = string.lower()
    for i in string:
        character_verification = dealing_each_character(i, string)
        if not character_verification:
            return False
        else:
            continue
    return True



def vowel_count_of_one_vowel(sentence_, vowel_):
    temp_count = sentence_.count(vowel_)
    return temp_count


def add_key_value_pair_to_dict(dictionary, vowel_, temp_count):
    dictionary[vowel_] = temp_count
    return dictionary


def get_count(sentence):
    dict_count = {}
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        temp_count = vowel_count_of_one_vowel(sentence, vowel)
        dict_count = add_key_value_pair_to_dict(dict_count, vowel, temp_count)
    return sum(dict_count.values())



def each_employee_score(key_, value_, boss_, total_score_):
    if key_ != boss_:
        total_score_ += value_
    else:
        total_score_ += 2 * value_
    return total_score_


def check_happiness_rating(happiness_rating_):
    if happiness_rating_ <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"


def outed(meet, boss):
    number_of_people = len(meet)
    total_score = 0
    for key, value in meet.items():
        total_score = each_employee_score(key, value, boss, total_score)
    happiness_rating = total_score / number_of_people
    return check_happiness_rating(happiness_rating)



def each_member_categorisation(member_info, output_):
    if member_info[0] >= 55 and member_info[1] > 7:
        output_.append("Senior")
    else:
        output_.append("Open")
    return output_


def open_or_senior(data):
    output = []
    for i in data:
        output = each_member_categorisation(i, output)
    return output



def total_number_of_vowels(words_):
    vowel_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        vowel_count += words_.count(vowel)
    return vowel_count


def total_no_of_letters_of_alphabet(character, letters_count_):
    if character.isalpha():
        letters_count_ += 1
    return letters_count_


def get_count_2(words=""):
    vowel_count = 0
    consonant_count = 0
    letters_count = 0
    try:
        words = words.lower()
    except AttributeError:
        return {"vowels": vowel_count, "consonants": consonant_count}
    else:
        vowel_count = total_number_of_vowels(words)
        for i in words:
            letters_count = total_no_of_letters_of_alphabet(i, letters_count)
        consonant_count = letters_count - vowel_count
    return {"vowels": vowel_count, "consonants": consonant_count}



class User:
    def __init__(self, name, balance, checking_account=True):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        else:
            self.balance -= amount
            return f"{self.name} has {self.balance}."

    def check(self, other_user, money):
        if not other_user.checking_account:
            raise ValueError
        elif money > other_user.balance:
            raise ValueError
        else:
            self.balance += money
            other_user.balance -= money
            return f"{self.name} has {self.balance} and {other_user.name} has {other_user.balance}."

    def add_cash(self, cash):
        self.balance += cash
        return f"{self.name} has {self.balance}."



def replace_error_inducing_characters(word_):
    word_ = word_.lower()
    if ")" in word_:
        word_ = word_.replace(")", "1")
    if "(" in word_:
        word_ = word_.replace("(", "2")
    return word_


def each_character_consideration(character, d_set, w_copy, w):
    if character in d_set:
        return False
    elif w_copy.count(character) != 1:
        d_set.add(character)
        w = w.replace(character, ")")
        return w
    else:
        w = w.replace(character, "(")
        return w


def duplicate_encode(word):
    duplicates = set()
    word = replace_error_inducing_characters(word)
    word_copy = word[:]
    for i in word:
        word = each_character_consideration(i, duplicates, word_copy, word)
        if word == False:
            continue
    return word



def splitting_and_joining_using_capital_indexes(s__, result__, temp_index_):
    result__ += s__[:temp_index_] + " " + s__[temp_index_]
    s__ = s__[temp_index_ + 1 :]
    return [result__, s__]


def capital_in_camel_case(char, s_, result_):
    if char.isupper():
        temp_index = s_.index(char)
        result_, s_ = splitting_and_joining_using_capital_indexes(
            s_, result_, temp_index
        )
    return [result_, s_]


def solution_2(s):
    if s.isalpha() and s[0].islower() and " " not in s.strip() and not s.islower():
        result = ""
        for i in s:
            two_outputs = capital_in_camel_case(i, s, result)
            result, s = two_outputs[0], two_outputs[1]
        result += s
        return result
    return s



def edge_cases(a_, b_):
    if not a_:
        return []
    elif not b_:
        return a_
    else:
        return None


def consider_each_element_in_a(char, b_, c_):
    if char not in b_:
        c_.append(char)
        return c_
    else:
        return c_


def array_diff(a, b):
    result = edge_cases(a, b)
    if result is None:
        c = []
        for i in a:
            c = consider_each_element_in_a(i, b, c)
        return c
    else:
        return result



def remove_odds_in_source_array(source_array__, char_):
    temp_index = source_array__.index(char_)
    source_array__[temp_index] = ""
    return source_array__


def consider_odd_number_in_array(char, odds_list, source_array_):
    if char % 2 != 0:
        odds_list.append(char)
        source_array_ = remove_odds_in_source_array(source_array_, char)
    return [source_array_, odds_list]


def add_corrected_odds_into_source_array(source_array__, odd_no_):
    temp_index = source_array__.index("")
    source_array__[temp_index] = odd_no_
    return source_array__


def replace_indirect_indexes_with_correct_odd_order(
    list_of_odds_,
    index_,
    source_array_,
):
    odd_no = list_of_odds_[index_]
    source_array_ = add_corrected_odds_into_source_array(source_array_, odd_no)
    index_ += 1
    return [source_array_, index_]


def sort_array(source_array):
    list_of_odds = []
    for i in source_array:
        two_outputs = consider_odd_number_in_array(i, list_of_odds, source_array)
        source_array, list_of_odds = two_outputs[0], two_outputs[1]
    list_of_odds = sorted(list_of_odds)
    index = 0
    while "" in source_array:
        three_outputs = replace_indirect_indexes_with_correct_odd_order(
            list_of_odds, index, source_array
        )
        source_array, index = three_outputs[0], three_outputs[1]
    return source_array



def check_two_adjacent_elements_in_alphabet(check_, alphabet_, chars_, loop_no):
    if check_ not in alphabet_:
        temp_index = alphabet_.index(chars_[loop_no - 1]) + 1
        return alphabet_[temp_index]
    else:
        return None


def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, len(chars)):
        check = f"{chars[i - 1]}{chars[i]}"
        return check_two_adjacent_elements_in_alphabet(check, alphabet, chars, i)
    return "Unreachable code (for code warriors)."



def queue_time(customers, n):
    if not customers:
        return 0
    elif len(customers) <= n:
        return max(customers)
    else:
        time_at_each_till, customers = customers[:n], customers[n:]
        for i in range(1, len(customers) + 1):
            quick_customer = min(time_at_each_till)
            temp_index = time_at_each_till.index(quick_customer)
            time_at_each_till[temp_index] += customers[0]
            customers = customers[1:]
        return max(time_at_each_till)


def assign_customer_to_till(time_at_each_till, customer_time):
    quick_customer = min(time_at_each_till)
    temp_index = time_at_each_till.index(quick_customer)
    time_at_each_till[temp_index] += customer_time
    return time_at_each_till


def queue_time_2(customers, n):
    if not customers:
        return 0
    elif len(customers) <= n:
        return max(customers)
    else:
        time_at_each_till, customers = customers[:n], customers[n:]
        for customer in customers:
            time_at_each_till = assign_customer_to_till(time_at_each_till, customer)
        return max(time_at_each_till)



def test_new_num(seq_, char, used_num_):
    count = seq_.count(char)
    if count % 2 != 0:
        return char
    used_num_.append(char)
    return used_num_


def find_it(seq):
    used_num = []
    for i in seq:
        if i in used_num:
            continue
        used_num = test_new_num(seq, i, used_num)
        if used_num == i:
            return used_num
    return "Unreachable code"



def verify_unique_character(sequence_, char, result_):
    if sequence_[char - 1] != sequence_[char]:
        result_.insert(char, sequence_[char - 1])
    return result_


def unique_in_order(sequence=""):
    if not sequence:
        return []
    else:
        result = []
        for i in range(1, len(sequence)):
            result = verify_unique_character(sequence, i, result)
        result.append(sequence[-1])
        return result



def duplicate_count(text):
    dup_char, text = [], text.lower()
    for i in text:
        if i in dup_char or text.count(i) == 1:
            continue
        elif text.count(i) > 1:
            dup_char.append(i)
    return len(dup_char)


def duplicate_count_2(text):
    dict_dup_char, text = [], text.lower()
    for i in text:
        if i in dict_dup_char or text.count(i) == 1:
            continue
        elif text.count(i) > 1:
            dict_dup_char[i] = text.count(i)
    return len(dict_dup_char)



def find_uniq(arr):
    arr = sorted(arr)
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[-1]



class WordDictionary:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def search(self, word):
        same_length_words = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        word = [char for char in word]
        for old_word in self.words:
            if len(word) == len(old_word):
                same_length_words.append(old_word)
        if not same_length_words:
            return False
        else:
            while "." in word:
                temp_index = word.index(".")
                word[temp_index] = letters
            for old_word in same_length_words:
                x = True
                for i in range(1, len(word) + 1):
                    if old_word[i - 1] in word[i - 1]:
                        continue
                    else:
                        x = False
                        break
                if x:
                    return True
            return False



class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        scaled_volume_for_self, scaled_volume_for_other = (
            [c_vol * self.volume for c_vol in self.color],
            [c_vol * other.volume for c_vol in other.color],
        )
        total_volume, result = self.volume + other.volume, tuple()
        for i in range(1, 4):
            element = -(
                -(scaled_volume_for_self[i - 1] + scaled_volume_for_other[i - 1])
                // total_volume
            )
            result += (int(element),)
        return Potion(result, total_volume)



def dealing_with_empty_spaces_and_multiple_strings_in_a_binary_string(
    binary_, list_of_binary_
):
    while " " in binary_:
        temp_index = binary_.index(" ")
        list_of_binary_.append(binary_[:temp_index])
        binary_ = binary_[temp_index + 1 :]
    return list_of_binary_


def looking_for_errors(binary_, result_):
    if (binary_[:7].count("1") % 2 == 0) and (binary_[7] == "0"):
        result_ += binary_[:7] + " "
    elif (binary_[:7].count("1") % 2 == 1) and (binary_[7] == "1"):
        result_ += binary_[:7] + " "
    else:
        result_ += "error" + " "
    return result_


def parity_bit(binary):
    try:
        binary += " "
        result = ""
        list_of_binary = []
        list_of_binary = (
            dealing_with_empty_spaces_and_multiple_strings_in_a_binary_string(
                binary, list_of_binary
            )
        )
        for binary in list_of_binary:
            result = looking_for_errors(binary, result)
    except TypeError:
        return "Ensure Correct Data Type"
    else:
        return result.rstrip()



def check_error_char_exist_and_attach_it_and_number_to_dict(s_, char_, dict_of_errors_):
    if s_.count(char_) > 0:
        dict_of_errors_[char_] = s_.count(char_)
    return dict_of_errors_


def adding_each_error_in_presentable_form_for_histogram(j_, result_, i_):
    space_no = 6 - len(str(j_))
    result_ += f"{i_}  {j_}{' ' * space_no}{'*' * j_}\r"
    return result_


def hist(s):
    dict_of_errors, result, error_char = {}, "", ["u", "w", "x", "z"]
    for char in error_char:
        dict_of_errors = check_error_char_exist_and_attach_it_and_number_to_dict(
            s, char, dict_of_errors
        )
    for i, j in dict_of_errors.items():
        result = adding_each_error_in_presentable_form_for_histogram(j, result, i)
    return result[:-1]



def to_fen(board):
    if len(board) != 8 or any(len(row) != 8 for row in board):
        return "Invalid"

    if (
        sum([row.count("K") for row in board]) != 1
        or sum([row.count("k") for row in board]) != 1
    ):
        return "Invalid"

    w_k_pos = [(r, c) for r in range(8) for c in range(8) if board[r][c] == "K"]
    b_k_pos = [(r, c) for r in range(8) for c in range(8) if board[r][c] == "k"]
    w_k_r, w_k_c = w_k_pos[0]
    b_k_r, b_k_c = b_k_pos[0]

    if abs(w_k_r - b_k_r) <= 1 and abs(w_k_c - b_k_c) <= 1:
        return "Invalid"

    if "P" in board[0] + board[7] or "p" in board[0] + board[7]:
        return "Invalid"
    if (
        sum([small_list.count("p") for small_list in board]) > 8
        or sum([small_list.count("P") for small_list in board]) > 8
    ):
        return "Invalid"

    w_p_count, b_p_count = 0, 0
    for row in board:
        for i in row:
            if i.isupper():
                w_p_count += 1
            elif i.islower():
                b_p_count += 1
    if w_p_count > 16 or b_p_count > 16:
        return "Invalid"

    result = ""
    for row in board:
        count = 0
        for i in row:
            if " " == i:
                count += 1
            else:
                if count == 0:
                    result += i
                else:
                    result += f"{count}" + i
                    count = 0
        if count > 0:
            result += f"{count}"
        result += "/"
    return result[:-1]



class Robot:
    def __init__(self):
        self.words_learned = []
        self.in_built_words()

    def in_built_words(self):
        known_string = "Thank you for teaching me I already know the word I do not understand the input "
        for i in known_string:
            if i == " ":
                temp_index = known_string.index(i)
                self.words_learned.append(known_string[:temp_index].lower())
                known_string = known_string[temp_index + 1 :]

    def learn_word(self, word):
        if not word.isalpha() or word.count(" ") > 0:
            return "I do not understand the input"
        elif word.lower() in self.words_learned:
            return f"I already know the word {word}"
        elif word.lower() not in self.words_learned:
            self.words_learned.append(word.lower())
            return f"Thank you for teaching me {word}"
        else:
            return None



def select_subarray(arr):
    dict_sub_arr, abs_val, prod = {}, "", 1
    for i in range(1, len(arr) + 1):
        arr_copy = arr[:]
        arr_copy.pop(i - 1)
        if sum(arr_copy) == 0:
            continue
        else:
            for element in arr_copy:
                prod *= element
            temp_abs_val = abs(prod / sum(arr_copy))
            prod = 1
            if abs_val == "":
                dict_sub_arr[f"list {i}"] = [i - 1, arr[i - 1], temp_abs_val]
                abs_val = temp_abs_val
            elif temp_abs_val < abs_val:
                dict_sub_arr.clear()
                dict_sub_arr[f"list {i}"] = [i - 1, arr[i - 1], temp_abs_val]
                abs_val = temp_abs_val
            elif temp_abs_val == abs_val:
                dict_sub_arr[f"list {i}"] = [i - 1, arr[i - 1], temp_abs_val]
            else:
                continue
    result = [x[:-1] for x in dict_sub_arr.values()]
    if len(result) == 1:
        return result[0]
    return result



def even_odd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        if (i + 1) % 2 == 0:
            result *= arr[i]
        else:
            result += arr[i]
    return result
