def read_recipe(recipe_path):
    with open(recipe_path ,"r") as my_recipe:
        print(my_recipe.read())
    return
def read_ingredients(recipe_path):
    with open(recipe_path, "a") as my_recipe:
        recipe_list = my_recipe.readlines()
        for i in recipe_list:
            if "*ingredients*" in i:
                first_line = recipe_list(i)
            if "*Directions*" in i:
                last_line = recipe_list(i)
        print(recipe_list[first_line:last_line])
    return
def read_Directions(recipe_path):
    with open(recipe_path, "a") as my_recipe:
        recipe_list = my_recipe.readlines()
        for i in recipe_list:
            if "*Directions*" in i:
                first_line = recipe_list(i)
        print(recipe_list[first_line:])
    return
def read_Directions(recipe_path):
    with open(recipe_path, "a") as my_recipe:
        recipe_list = my_recipe.readlines()
        for i in recipe_list:
            if "*ingredients*" in i:
                last_line = recipe_list(i)
        print(recipe_list[:last_line])
    return
def add_yours_notes(recipe_path):
    my_note = input("write")
    with open(recipe_path, "a") as my_recipe:
        my_recipe.write(my_note)
    print ("Note written successfully.")
    return
def add_yours_line_notes(recipe_path):
    line_num = input("which line you want to write?")
    with open(recipe_path, "r") as my_recipe:
        recipe_list = my_recipe.readlines()
        recipe_list[line_num -1] = recipe_list[line_num -1] + '/n'
    with open(recipe_path, "w") as my_recipe:   
        my_recipe.writelines(recipe_list)
    print ("Note written successfully.")
    return
def allergies(ingredient):
        for i in all_recipes:
            

    