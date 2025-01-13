#Python Credit card validator program...
#Steps for credit card validation:
'''
1.Remove any '-' and ' '.
2.Add all digits from the odd places from right to left.
3.Double every second digit from left to right.
         (If result is a two-digit number,
         add the two digit numbers together to get a single digit.)
4.Sum the totals of step 2 and 3.
5.If the sum is divisible by 10, then the credit card number is valid.
'''

sum_odd_digits = 0
sum_even_digits = 0
total = 0

#Step 1:
card_number = input("Enter a valid credit card number#: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

#Step 2:
card_number = card_number[::-1]
for x in card_number[::2]:
    sum_odd_digits = sum_odd_digits + int(x)

#Step 3:
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x%10))    #+= means that sum_even_digits = sum_even_digits + variable
    else:
        sum_even_digits += x

#Step 4:
total = sum_odd_digits + sum_even_digits

#Sesp 5:
if total % 10 == 0:
    print("Credit card number is valid.\nWelcome to Lateerol financial corp.")
else:
    print("Credit card number is invalid.\nPlease try entering the credit card number again:")

'''
Also here are some trial credit card numbers in it:
378282246310005
371449635398431
378734493671000
5610591081018250
30569309025904
38520000023237
6011111111111117
6011000990139424
3530111333300000
3566002020360505
5555555555554444
5105105105105100
4111111111111111
4012888888881881'''