# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message 

print(output)

# Output
# What is your email address?: chaitali@gmail.com
# Your username is chaitali and your domain name is gmail.com