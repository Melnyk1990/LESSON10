import re
text = 'To be, or not to be, that is the question, Whether tis nobler in the mind to suffer \n' \
       'The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, \n' \
       'And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache \n' \
       'and the thousand natural shocks That flesh is heir to, tis a consummation Devoutly to be wish d. To die, to sleep'

print('*'*10, 'TASK 1', 10*'*')
words = ''
with open("text_first.txt", 'w') as save_file:
    save_file.write(text)

with open("text_first.txt", 'r') as my_file_search:
    result = my_file_search.read()
    search_word = re.findall(r'[A-Za-z]{7,}\s', result)
    for i in search_word:
        words +=i
with open("text_second.txt", 'w') as my_file_result:
    my_file_result.write(words)


with open("text_second.txt", 'r') as seven_words:
    read = seven_words.read()
    print(f'Quantity words: {read}')
print()
print()