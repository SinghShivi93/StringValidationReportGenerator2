# String Validation Report Generator ✅

A Python mini-project that takes:
- Comma-separated names
- Email IDs
- Phone numbers

It validates them, cleans the data, and prints a summary report.

## Features:
- Name validation (alphabets only, spaces allowed)
- Email validation (basic format check)
- Phone number validation (10-digit numbers)
- Clean output with summary counts

## Run:
Paste the code in any Python IDE or online compiler and run.


## 🧪 Sample Input:

```
Shivika, 123, geeta sharma  
shivika@gmail.com, shivika@@gmail.com, abc@.com  
9876543210, 12345, 88888a8888  
```

---

## ✅ Sample Output:

```
Valid names are: Shivika, Geeta Sharma  
Invalid names are: 123  

Valid email ids are: shivika@gmail.com  
Invalid email ids: shivika@@gmail.com, abc@.com  

Valid phone numbers are: 9876543210  
Invalid phone numbers: 12345, 88888a8888  
```

---

## ✨ Summary:
```
Valid Names: 2 | Invalid Names: 1  
Valid Emails: 1 | Invalid Emails: 2  
Valid Phones: 1 | Invalid Phones: 2
```

