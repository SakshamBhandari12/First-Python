def main():
    message= input("Enter user's message :")
    result= convert(message)
    print (result)

def convert(new_message):
    new_message= new_message.replace(":)","🙂").replace(":(", "🙁")
    return new_message

main()