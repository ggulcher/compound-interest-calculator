# \\\ UNDER CONSTRUCTION ///
# A financial investment calculator using the compound interest formula

print("How much is currently in your account?")
p = float(input("Principle here: "))

print("How much do you invest on a regular basis?")
pmt = float(input("Contribution here: "))

print("What is your anticipated interest rate? (Decimals only)")
rate = float(input("Interest here: "))

print("How many times will your interest compound annually?")
n = int(input("Compound type here: "))

print("How many years will you invest income?")
time = int(input("Number of years here: "))

print(" ")

z = rate/n
m = n*time

amount1 = p*((1 + z)**m)
amount2 = (pmt*((1 + z)**m) - 1) / z

final_amount = round(amount1 + amount2, 2)

print(f"Your final amount after {time} years will be ${final_amount}. Congratulations!")
