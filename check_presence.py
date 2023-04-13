required = ["dushyant1.txt","dushyant2.txt","dushyant3.txt"]
for file in required:
    try:
        temp = open(file)
        temp.close()
    else:
        temp = open(file,"w")
        temp.close()