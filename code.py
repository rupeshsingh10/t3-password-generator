import random
import string

# Step 1: Get password length
length = int(input("Password length: "))

# Step 2: Define character pool
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display result
print(f"Generated Password: {password}")
