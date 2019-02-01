file = open("test_01.py","a+")

text = file.read()

text +="hahahaha"
file.write(text)
print(text)

file.close()
