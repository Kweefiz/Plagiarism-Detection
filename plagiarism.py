from difflib import SequenceMatcher

with open ('text1.txt') as file_one,  open ('text2.txt') as file_two:
    data_file1 = file_one.read()
    data_file2 = file_two.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f" The plagiarised content is {matches*100}%")