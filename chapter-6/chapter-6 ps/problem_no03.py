#spam filter
p1="buy now"
p2="click here"
p3="make money"
p4="free gift"

message=input("Enter your message: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a spam message")
else:
    print("This is not a spam message")