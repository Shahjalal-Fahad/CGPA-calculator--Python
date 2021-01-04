#Student Information
print("\t Student Information")
print("\t -------------------")
StudentName=str(input("Student's Name: \t"))
Class=str(input("Student's Class: \t"))
Roll=str(input("Student's Roll: \t"))

#Subject Number
print("\n")
print("\t Subject Number")
print("\t -------------------")
Bangla=int(input("Bangla number: \t\t"))
English=int(input("English number: \t"))
Math=int(input("Math number: \t\t"))
Physics=int(input("Physics number: \t"))
Ict=int(input("Ict number: \t\t"))
Islam = int(input("Islam number: \t\t"))
print("=================================")


result=["Bangla","English","Math","Physics","Ict","Islam","cgpa"]
#Subjects
def subject(result):
    

    if result>=80 and result<=100:
        Result="A+"
        return Result
    elif result>=75 and result<=79:
        Result="A"
        return Result
    elif result>=70 and result<=74:
        Result="A-"
        return Result
    elif result>= 65 and result <=69:
        Result="B+"
        return Result
    elif result>=60 and result<=64:
        Result="B"
        return Result
    elif result>=55 and result<=59:
        Result="B-"
        return Result
    elif result>=50 and result<=54:
        Result="C+"
        return Result
    elif result>=45 and result<=49:
        Result="C"
        return Result
    elif result>=40 and result<=44:
        Result="D"
        return Result
    else:
        Result="F"
        return Result

FinalResult=subject(Bangla)
print("Bangla: \t\t",FinalResult)
FinalResult=subject(English)
print("English: \t\t", FinalResult)
FinalResult=subject(Math)
print("Math: \t\t\t", FinalResult)
FinalResult=subject(Physics)
print("Physics: \t\t", FinalResult)
FinalResult=subject(Ict)
print("ICT: \t\t\t", FinalResult)
FinalResult=subject(Islam)
print("Islam: \t\t\t", FinalResult)

TotalNumber=Bangla+English+Math+Physics+Ict+Islam
AverageNumber=TotalNumber//6

print("=================================")
print("Student's Name: \t"+ StudentName)
print("Class: \t\t\t",Class)
print("Roll: \t\t\t",Roll)



if Bangla<40 or English<40 or Math<40 or Physics<40 or Ict<40 or Islam<40:
    print("Failed")
else:
    print("=================================")
    print("TotalNumber: \t\t",TotalNumber)
    print("Average Number: \t",AverageNumber)
    print("=================================")
    
    cgpa=AverageNumber
    FinalResult=subject(cgpa)
    print("CGPA: \t\t\t", FinalResult)
    print("=================================")