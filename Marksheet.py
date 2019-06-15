subject1 = (int(input("Enter Marks in Maths : ")))

if subject1 < 0 or subject1 > 100 :
    print ("Invalid Number In Maths")


subject2 = (int(input("Enter Marks in Islamiat : ")))
if subject2 < 0 and subject2 > 100 :
        print ("Invalid Number In Islamiat")
        

subject3 = (int(input("Enter Marks in Physics : ")))
if subject3 < 0 and subject3 > 100 :
        print ("Invalid Number In Physics")

subject4 = (int(input("Enter Marks in Urdu : ")))
if subject4 < 0 and subject4 > 100 :
        print ("Invalid Number In Urdu")

subject5 = (int(input("Enter Marks in English : ")))
if subject5 < 0 and subject5 > 100 :
        print ("Invalid Number In English")

totalmarks = subject1+subject2+subject3+subject4+subject5
percentage = totalmarks * 100 / 500
 

print ("Total Marks =", totalmarks)
print ("Your Percentage =", percentage,"%")


if percentage < 20 :
    print ("Grade F")

if percentage > 20 and percentage < 40 :
    print ("Grade C")

if percentage > 40 and percentage < 60 :
    print ("Grade B")

if percentage > 60 and percentage < 80 :
    print ("Grade A")

if percentage > 80 and percentage < 100 :
    print ("Grade A+")
