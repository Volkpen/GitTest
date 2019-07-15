print("How many miles did you run/walk today?")
miles = input()
kms = float(miles)/1.60934
kms = round(kms, 2)
print(f"That is equal to {kms} kms ")