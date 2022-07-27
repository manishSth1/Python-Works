my_passport_info_dictionary = {                            #creating dictionary to store my passport info
"first_name": "Manish",
"middle_name": "n/a",
"last_name": "Shrestha",
"passport_number": "123456789",
"date_of_birth": "01/01/1996",
"expiry_date": "01/01/2025",
"place_of_birth": "Pokhara, Nepal",
"issuing_authority": "MOFA, Department of Passport",
"father": {                                                #creating dictionary within dictionary to store my father's info
    "first_name": "Thaman",
    "middle_name": "Kumar",
    "last_name": "Shrestha",
    "place_of_birth": "Pokhara, Nepal",
}

}
print(my_passport_info_dictionary)                           #printing out whole dictionary 
print(my_passport_info_dictionary["father"])                 #printing out dictionary named "father" inside of my dictionary
print(my_passport_info_dictionary["expiry_date"])            #checking expiry date of my passport
print(my_passport_info_dictionary["father"]["middle_name"])  #checking father's middle name
