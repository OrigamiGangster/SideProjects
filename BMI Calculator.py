w = int(input("Insert weight in KG"))
h = float(input("Insert height in Meters"))
if(w/h//2 <= 18.4):
    print("Underweight")
elif(w/h//2 >= 18.5 and w/h//2 <= 24.9):
    print("Normal")
elif(w/h//2 >=25 and w/h//2 <= 29.9):
    print("Overweigt")
else:
    print("Obese") 