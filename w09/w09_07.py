text = input()
mod_text = str()
count = 0
       
while count < len(text):
    if text[count].isalpha():
        mod_text += text[count]
    count += 1

print(mod_text)