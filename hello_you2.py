# Ask user for name

name = input("What is your name?: ")

# Ask user for age

age = input("How old are you?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

love = input("What do you love doing?: ")

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

# Print output to screen
print(output)
{"threads":[{"position":0,"start":0,"end":233,"connection":"open"},{"position":466,"start":234,"end":466,"connection":"closed"}],"url":"https://a.udemycdn.com/2018-07-09_00-04-07-9ec950fcf0c0fc6a84cbbc0db66951ce/original.py?nva=20200208153507&filename=hello-you.py&download=True&token=0d7a274cd790e94ba208f","method":"GET","port":443,"downloadSize":466,"headers":{"date":"Wed, 07 Aug 2019 04:06:23 GMT","content-type":"application/force-download","content-length":"466","connection":"close","etag":"\"8d33d6640d76a792d3d0672d83945612\"","last-modified":"Mon, 09 Jul 2018 00:04:08 GMT","server":"AmazonS3","x-amz-id-2":"Kl+0MUagD8RGLXohy2fhZ+YISSeqQU+tP0GlnXBW6305V2u3eh+stwWKJgyGfqxRfF6iwqluAa0=","x-amz-meta-qqfilename":"hello_you.py","x-amz-replication-status":"COMPLETED","x-amz-request-id":"C91883F1F5FD766A","x-amz-version-id":"texzIW9elmuNUQftmh7abE7wghirI5UK","access-control-allow-origin":"*","age":"16009262","content-disposition":"attachment; filename=\"hello-you.py\"","accept-ranges":"bytes"}}  

# Output
# What is your name?: Chaitali
# How old are you?: 21
# What city do you live in?: Pune
# What do you love doing?: I like to play Basketball
# Your name is Chaitali and you are 21 years old. You live in Pune and you love I like to play Basketball