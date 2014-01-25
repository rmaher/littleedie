balance = 2222
annualInterestrate = 1.2

monthlyInterestrate = annualInterestrate/12.0
monthlyBalance = balance/12+monthlyInterestrate

while balance > 0:
    return monthlyBalance ('Month: ' + str(month))
    month += 1
    print ('Minimum monthly payment: ' + str(monthlyPayment))
    monthlyPayment = updatedBalance*monthlyInterestrate
    print ('Remaining balance: ' + str(updatedBalance))
    updatedBalance = updatedBalance-monthlyPayment 
else:   
    print ('Total Paid: ' + str(monthlyPayment*12)) 
    print ('Remaining blance: ' + str(updatedBalance))