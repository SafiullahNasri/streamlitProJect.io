file = open("outube.txt", 'w')

try:
    file.write('cahi or pro')

finally:
    file.close()


with open('youtube.txt', 'w') as file:
    file.write('cahi or python')