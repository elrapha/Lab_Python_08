import re

def isEmail(inp):
    if re.findall(r'^\w+@[A-Za-z0-9]+(\.[A-Za-z]{2,4})+$',inp)!=[]:
        return True

    return False

print isEmail('blah@hello.com')
print isEmail('sd$sd@hello.com')
def getTxts(inp):
    return re.findall(r'\w+\.txt',inp)

print getTxts('yo.html blah.txt woah.txt he ')

def percAwesome(inp):
    inplen= len(re.findall(r'\w+',inp))
    findlen=len(re.findall(r'awesome|awes0me',inp))
    return (findlen/float(inplen))*100

print percAwesome('iamawesomeblah and awes0me is as awesomeo does'),'%'
print percAwesome('hello my name is wayawesomedude'),'%'
