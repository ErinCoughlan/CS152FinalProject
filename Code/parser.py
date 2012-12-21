# Will take out the relevant matrix from an xml file

myFile = open("example.xml", "r")
array = []
foundData = False
count = 0

while count <200:
    line = myFile.readline()
    if not line:
        break
    elif "data" in line:
        foundData = True
    elif foundData:
        array.append(line.rstrip())
    elif ("data" in line) and foundData:
        line.replace("</data></name>", "")
        array.append(line.rstrip())
        foundData = False
    count += 1

for i in array:
    
myFile.close()
print (array)

