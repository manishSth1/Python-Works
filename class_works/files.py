file = open('class_works/test.txt', 'r')          # open file in read mode -> 'r'
print(file.read())                                # read the 'file'
file.close()                                      # close the file

file = open('class_works/test.txt', 'w')          # open the file in write mode -> 'w'
file.write('This is a new content\n')             # write in the file
file.close()                                      # close the file

file = open('class_works/test.txt', 'a', encoding='utf-8')      # open the file in append mode -> 'a', 'utf -8' -> an encoding method, supports emojis(windows key + dot ket to get the emojis keyboard)
file2 = open('class_works/test.txt', 'a', encoding='utf-8')
file.write('This is a new content')                             # writes in the file                                
file.write('\n😄\n')
file.close()

with open('class_works/test.txt', 'a', encoding='utf-8') as file:
    file.write('This is a new content')
    file.write('\n😄')

file = open('class_works/test.txt', 'r+', encoding='utf-8')
lines =file.readlines()
print(lines)                     # prints contents of file in the list
del lines[2]                   # del lines 2
file.seek(0)                   # go to the first character -> T
file.truncate()                # delete all
file.writelines(lines)         # save rest
file.close()
