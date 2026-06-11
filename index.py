import func as f


check = input("Enter Password :=")

# scoring it 

score , feedback = f.analyze_p(check)

print(f" Score := {score} / 10")

# Strength Teller
if score <= 3:
    strength = "Weak"
elif score <= 6:
    strength = "Medium"
elif score <= 8:
    strength = "High"
else:
    strength = "Extremely High"
print(f" Strength := {strength}")

# Printing Feedback , if it exist
if feedback:
    print(f" Errors/ Problems := ")
    for i in feedback:
        print(f"- {i}")
