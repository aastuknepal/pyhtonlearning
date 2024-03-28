def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any inputs"
    formatted_fname = f_name.title()
    formatted_lname = (l_name.title())
    return f"{formatted_fname}  {formatted_lname}"

print(format_name("astuk", "nepal"))   
