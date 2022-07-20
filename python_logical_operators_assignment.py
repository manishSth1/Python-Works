# 1
# "If you have a passcode or face id, you can access your phone otherwise not."

has_passcode = True
has_faceid = True
print(not(has_passcode or has_faceid))  # result -> False

# with if-else statement and input from user

passcode = input("Do you have passcode, True/False: ")
faceid = input("Do you have faceid, True/False: ")          
if (passcode == 'True' or faceid == 'True'):
    print("You can access your phone")

else:
    print("You cannot access your phone")

# 2
# "If you woke up on time and had breakfast, you will reach to office on time otherwise you will be late."

woke_up_on_time = True
had_breakfast = True
print(woke_up_on_time and had_breakfast) # result -> True

# 3
# "If you are joining class on time and participating, you're most likely to pass otheerwise you will fail."

joining_class_on_time = True
participating = True
print(not(joining_class_on_time and participating)) # result -> False

# 4
# "If you put downy or dryer sheets while doing laundry, your clothes will have fragrance otherwise not."

put_downy = False
put_dryer_sheets = True
print(put_downy or put_dryer_sheets) # result -> True

# 5
# "If your eyes are weak and you have glasses, you will see things clearly othwerise it will be unclear."

eyes_weak = True
have_glasses = True
print(eyes_weak and have_glasses) # result -> True 