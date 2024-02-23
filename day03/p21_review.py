## Q7
## rreadlines() 썼을때
f = open('./day-3/test.txt', mode='r', encoding='utf-8')
body = f.readline
()
f.close()

body = [body[0], body[1].replace('java','python')]
print(body)
f = open('./day-3/test.txt', mode='w', encoding='utf-8')
f.write(body[0]+body[1])
f.close()

## read()를 썼을때
f = open('./day-3/test.txt', mode='r', encoding='utf-8')
body = f.read()
f.close()


