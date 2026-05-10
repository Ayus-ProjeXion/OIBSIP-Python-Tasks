#Project:BMI Calculator
#Name:Ayusman Mishra
def main():
    print("BMI Calculator by Ayusman")
    weight=float(input("enter weight in kg: "))
    height=float(input("enter height in meters: "))
    bmi=weight/(height*height)
    print(f"BMI:{bmi:.2f}")
    if bmi<18.5:
        print("Status: Underweight")
    elif 18.5<=bmi and bmi<24.9:
        print("Status:Normal")
    elif 25<=bmi and bmi<29.9:
        print("Status:Overweight")
    else:
        print("Status: Obese") 
main()        
