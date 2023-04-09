##list down the state of India and print one by one wthe state name ###

State_of_India = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu", "Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "West Bengal"]

#modify the spelling of 3rd state.
State_of_India[2] = "Assaam"

#print the 3rd state.
#print(State_of_India[2])

#add one new state at the end
State_of_India.append("pranitaland")

#entend the list
State_of_India.extend(["shilpaland", "Delhi", "Pondicherry"]) 


print(State_of_India)

