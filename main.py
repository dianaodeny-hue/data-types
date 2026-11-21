name = input("enter your name :")
gadget = input("enter your favourite gadget:")

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_Active = True

print("Name:", name, "->type:", type(name))
print("gadget:", gadget, "->type:", type(gadget))
print("agent number:", agent_number, "->type:", type(agent_number))
print("speed rating:", speed_rating, "->type:", type(speed_rating))
print("is active:", is_Active, "->type:", type(is_Active))

#secret agent name
first_three = name[0:3]
last_letter = name [-1:]

# string concatenation
code_name = first_three + last_letter
print("secret code name:", code_name)

print()
print("=====SECRET AGENT BADGE=====")
print("agent: ", code_name.upper())
print("ID:", agent_number," |", "missions:", mission_count)
print("speed:", speed_rating,"|", "Acticve", is_Active)
print("==========================")