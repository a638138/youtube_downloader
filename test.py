str = 'https://www.youtube.com/watch?v=KdeqA3eduOs&list=RDKdeqA3eduOs&start_radio=1'

# print(str[str.find('v=')+2:])

counter = 0

for i in str[str.find('v=')+2:]:
    if i.isalnum():
        # print(i)
        counter += 1
    else:
        break
print(str[str.find('v=')+2:str.find('v=')+2+counter])