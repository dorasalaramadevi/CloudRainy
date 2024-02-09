def convert_list(number_is):
    number=""
    for i in number_is:
        if i.isdigit():
            number+=i
        else:
            number+=i+"-"
    number=list(number.split("-"))
    if number[0]=="":
        number=number[1:]
    if number[len(number)-1]=="":
        number=number[:len(number)]
    return number
    
    
sequence=list(input("Enter Sequence :").split(","))
list_num=[]
list_alpha=[]
for i in sequence:
    if i.isdigit():
        list_num.append(int(i))
    else:
        list_alpha.append(i)
if len(list_num)==0:
    if len(list_alpha[0])<=1:
        alpha1=ord(list_alpha[1])-ord(list_alpha[0])
        or_num=list_alpha[len(list_alpha)-1]
        last_ord=ord(or_num)+alpha1
        alpha=chr(last_ord)
        print(alpha)
    else:
        list_a1=""
        number=convert_list(list_alpha[0])
        number1=convert_list(list_alpha[1])
        number2=convert_list(list_alpha[len(list_alpha)-1])
        for i in range(len(number)):
            if number[i].isdigit():
                n=int(number1[i])-int(number[i])
                n=int(number2[i])+n
                list_a1+=str(n)
            else:
                alpha_1=ord(number1[i])-ord(number[i])
                last_ord_1=ord(number2[i])+alpha_1
                alpha_1=chr(last_ord_1)
                list_a1+=alpha_1
        print(list_a1)       
            
else:
    num1=list_num[1]-list_num[0]
    num=list_num[len(list_num)-1]+num1
    print(num)
