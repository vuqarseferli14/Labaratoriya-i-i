weight=int(input("cekini daxil edin-"))
height=float(input("boyu daxil edin-"))
BMI=weight/(height*height)
if BMI<18.5 :
    print("Underweight")
elif 18.5<=BMI<24.9 :
    print("Normal Weight")
elif 25.0<=BMI<=29.9 :
    print("Overweight")
else :
    print("Obese")
