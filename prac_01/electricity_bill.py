TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator 2.0")

tariff = int(input("Which Tariff are you using (11 or 31)? "))
while tariff != 11 and tariff != 31:
    print("Invalid Tariff")
    tariff = int(input("Which Tariff are you using? (11 or 31)? "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31


daily_use = float(input("Daily use in kWh: "))
number_of_days = int(input("Number of billing days: "))


print(f"Estimated bill: ${(tariff * daily_use) * number_of_days:.2f}")

