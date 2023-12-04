# 2.2
print("Hello", input("Enter your name"))

# 2.3
print('Pay:', float(input("Enter Hours:"))*float(input('Enter Pay:')))

# 3.1
hrs = float(input("Enter Hours:"))
pay = float(input("Enter Pay"))
if (hrs <= 40):
    print(hrs*pay)
else:
    print(40*pay + (hrs-40)*pay*1.5)

# 3.3
score = float(input("Enter Score:"))
if (score > 1 or score < 0):
    print('Error')
else:
    if (score >= 0.9):
        print('A')
    elif (score >= 0.8):
        print('B')
    elif (score >= 0.7):
        print('C')
    elif (score >= 0.6):
        print('D')
    else:
        print('F')

# 4.6
def computepay(h, r):
    return h*r if h <= 40 else 40*r + (h-40)*r*1.5
print("Pay", computepay(float(input("Enter Hours:")), float(input("Enter rate:"))))

# 5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            if largest is None: largest = int(num)
            elif largest < int(num): largest = int(num)
            if smallest is None: smallest = int(num)
            elif smallest > int(num): smallest = int(num)
        except:
            print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)
