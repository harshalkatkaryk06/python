# w.a.p to read basic salary of an employee and calculate Gross salary as per below policy....
#01. If basic salary is less than 1500 then HRA=10% of basic and DA=25% of basic.
#02. If basic salary is 1500 or above then HRA=500 and DA=50% of basic.

basic = eval(input('enter basic salary'))
if basic <1500:
    hra = basic * 0.10           #10%
    da = basic * 0.25            #25%
else:
    hra =500
    da = basic*0.50               #50%

gross=basic+hra+da
print(f'Gross salary = {gross}')