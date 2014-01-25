balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0

monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = balance*monthlyPaymentRate
previousBalance = balance
unpaidBalance = previousBalance - monthlyPayment
updatedBalance = (unpaidBalance)+(monthlyInterestRate*unpaidBalance)

while month < 12:
    print ('Month: ' + str(month))
    month += 1
    print ('Minimum monthly payment: ' + str("%0.2f"%monthlyPayment))
    monthlyPayment = updatedBalance*monthlyInterestRate
    print ('Remaining balance: ' + str("%0.2f"%updatedBalance))
    updatedBalance = updatedBalance-monthlyPayment

else:
    print ('Total Paid: ' + str("%0.2f"%(balance-updatedBalance)))
    print ('Remaining balance: ' + str("%0.2f"%updatedBalance))
