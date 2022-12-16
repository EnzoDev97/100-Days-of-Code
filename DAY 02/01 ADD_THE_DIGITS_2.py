# 01 - Write a program that adds the digits in a 2 digit number. if the input was 35, then the output should be 3 + 5 = 8


two_digit_number = input("Type a two digit number: ")
lista = list(two_digit_number)
r = int(lista[0]) + int(lista[1])
print(r)
print('-'*100,'\n')
#OU

first_number = two_digit_number[0]
second_number = two_digit_number[1]

result = int(first_number) + int(second_number)
print (first_number + " " + "+" + " " + second_number )
print(result)