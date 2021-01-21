email = input("Please enter your email address : ").strip()

index = email.index('@')

uname = email[:index]
domain = email[index+1:]

print("\nEmail Address : ", email)
print("Username : ", uname)
print("Domain name : ", domain)