# ===== Name Validation =====

name = input("Enter the names, comma separated: ").split(",") 
validnames = []
invalidnames = []

for i in range(len(name)):
    name[i] = name[i].strip()
    if name[i].replace(" ", "").isalpha():
        name[i] = name[i].title()
        validnames.append(name[i])
    else:
        invalidnames.append(name[i])

print("\n=== Name Validation Result ===")
if not validnames:
    print("No valid names.")
else:
    print(f"Valid names are: {', '.join(validnames)}")

if not invalidnames:
    print("No invalid names.")
else:
    print(f"Invalid names are: {', '.join(invalidnames)}")


# ===== Email Validation =====

email = input("\nEnter the email IDs, comma separated: ").split(",") 
validemailids = []
invalidemailids = []

for i in range(len(email)):
    email[i] = email[i].strip()
    if "@" in email[i] and "." in email[i] and " " not in email[i] and not email[i].startswith("@"):
        validemailids.append(email[i])
    else:
        invalidemailids.append(email[i])

print("\n=== Email Validation Result ===")
if not validemailids:
    print("No valid email IDs.")
else:
    print(f"Valid email IDs are: {', '.join(validemailids)}")

if not invalidemailids:
    print("No invalid email IDs.")
else:
    print(f"Invalid email IDs are: {', '.join(invalidemailids)}")


# ===== Summary =====

print("\n=== Summary ===")
print(f"Total valid names: {len(validnames)}")
print(f"Total invalid names: {len(invalidnames)}")
print(f"Total valid email IDs: {len(validemailids)}")
print(f"Total invalid email IDs: {len(invalidemailids)}")

#====== Phone number validation=====
phone_number=input("Enter phone numbers (comma separated): ").split(",") 
validphonenumbers = []
invalidphonenumbers = [] 
for i in range(len(phone_number)):
  phone_number[i]=phone_number[i].strip()
  if phone_number[i].isdigit() and len(phone_number[i])==10:
    validphonenumbers.append(phone_number[i])
  else:
    invalidphonenumbers.append(phone_number[i])
if not validphonenumbers:
  print("No valid number")
else:
  print(f"Valid numbers are : {', '.join (validphonenumbers)}")
if not invalidphonenumbers:
  print("No invalid numbers")
else:
  print(f"Invalid numbers are: {', '.join(invalidphonenumbers)}")


