def ntot(mNumber):
    number1 = {
            "0":"",
            "1":"one",
           "2":"two",
           "3":"three",
           "4":"four",
           "5":"five",
           "6":"six",
           "7":"seven",
           "8":"eight",
           "9":"nine"}
           
    number2 = {"10":"ten",
           "11":"eleven",
           "12":"twelve",
           "13":"thirteen",
           "14":"fourteen",
           "15":"fifteen",
           "16":"sixteen",
           "17":"seventeen",
           "18":"eighteen",
           "19":"nineteen"}

    number3 = {
            "2":"twenty",
           "3":"thirty",
           "4":"forty",
           "5":"fifty",
           "6":"sixty",
           "7":"seventy",
           "8":"eighty",
           "9":"ninety"}

    ourNumb = mNumber
    ourNumb = str(ourNumb)
    numb = ""
    if(len(ourNumb)==1):
        numb = number1[ourNumb]

    elif(len(ourNumb)==2):
        if(int(ourNumb)<20):
            numb = number2[ourNumb]
        elif(int(ourNumb)>=20):
            numb += number3[ourNumb[0]] + number1[ourNumb[1]]

    elif(len(ourNumb)==3):
        numb += number1[ourNumb[0]] + "hundredand"
        if(ourNumb[1]!="0"):
                if(ourNumb[1]!="1"):
                    numb += number3[ourNumb[1]]
                else:
                    numb += number2[ourNumb[1:3]]
        elif(int(ourNumb[1:3])>=20):
            numb += number1[ourNumb[2]]
        if(ourNumb[2]!="0" and ourNumb[1]!="1"):
                numb += number1[ourNumb[2]]
    elif(len(ourNumb)==4):
        numb = "onethousand"
    return numb

sum=0
for i in range(0,1000):
    sum+=len(ntot(i))