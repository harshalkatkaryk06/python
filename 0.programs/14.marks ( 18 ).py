# w.a.p to read percentage marks from users and print appropriate message as follows.
# 100 to 80 distinction
# 60 to <80 frist class
# 50 to <60 second class
# 40 to <50 third class

marks=eval(input("Enter your percentage marks: "))
if 0< marks <=100:
    if 80 <= marks <= 100:
        print("Distinction")
    elif 60 <= marks < 80:
        print("First Class")
    elif 50 <= marks < 60:
        print("Second Class")
    elif 40 <= marks < 50:
        print("Third Class")
    else:
        print("Fail")
else:
    print('invalid marks have been provided')
