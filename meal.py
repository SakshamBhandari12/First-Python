def main():
    user_time = input ("What time is it? ").strip()
    hours = convert (user_time)
    if 7.0 <= hours <=  8.0:
        print ("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print ("lunch time")
    elif 18.0 <= hours <= 19.0:
        print ("dinner time")
    else:
        print ()

def convert(time):
    hours, minutes = time.split(":")
    return float (hours) + (float(minutes) / 60) 

if __name__ == "__main__":
    main()





