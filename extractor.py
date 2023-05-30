import re

try:
    
    file = open("sip.txt")
    for line in file:
        line = line.strip()
        emails = re.findall(r"[\w\.-]+@[\w\.-]+", line)
        if(len(emails) > 0):
            mails = ", ".join(map(str, emails))
            g = open('Omails.txt', 'a')
            g.write(mails + '\n')
            g.close()
            
except FileNotFoundError as e:
    print(e)    
    
#My-THOT

 