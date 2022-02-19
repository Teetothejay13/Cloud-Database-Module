# 1. Name:
#      TJ Putnam
# 2. Program Name:
#      Recipe Book
# 3. Program Description:
#      This program will take an input in the form of a file name, and look for a json file with that name. If it exists,
#      then it will open the file and read it. If it doesn't, then the program will ask if the user wants to create the
#      file, and comply if they do. If the file exists/once it is created, the user can select an input to read the recipe,
#      edit the recipe, or open a new recipe.
#       
#      The added functionality is the access to cloud databases.
# 4. What was the hardest part?
#      
# 5. How long did it take for me to complete the assignment?
#      

# we'll need this
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("C:/Users/teeto/hello/CSE310/cloud-database-module-firebase-adminsdk-x784k-bf11e67e05.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# main will run the show
def main():
    # first, we need an input loop the user can quit from
    userInput = ""
    print("Welcome to your personal recipe book!")
    while userInput != "q":
        print()
        print("Open a recipe (o)")
        print("Edit a recipe (e)")
        print("Create new recipe (n)")
        print("Quit (q)\n")
        userInput = input("Please select what you would like to do: ")
        # now we can have if/else statements calling the functions for each input
        # opening the file should be pretty simple, as long as we have safeguards against missing or unreadable files
        if userInput == "o":
            fileName = input("Please enter the file name of the recipe you would like to open: ")
            # here we will open the file, and store the json data into separate lists that can be displayed
            contents = readFile(fileName)
            if contents == False:
                print("There was a problem reading the file. Please try again or choose another recipe.")
            else:
                display(contents)
        # if there is something wrong with the recipe, we want to be able to edit it and fix it
        elif userInput == "e":
            fileName = input("Please enter the name of the file you would like to edit: ")
            editRecipe(fileName)
        # we don't want to have to manually create new json files, so we have a function to do that for us
        elif userInput == "n":
            newFileName = input("Please enter the name you would like to call the new file: ")
            createFile(newFileName)
        elif userInput == "q":
            print("Thank you for cooking with me!")

# this function will open the file and read it after checking if it's there, prompting to create the file if it isn't
def readFile(fileName):
        # if the file exists and is readable, the try will succeed and return the information
        try:
            # we need to reference the right document
            doc_ref = db.collection(u'Recipes').document(u'{}'.format(fileName))
            # and then get the data from the document
            doc = doc_ref.get()
            data = doc.to_dict()
            # and then split it out into the separate parts
            name = data["Name"]
            ingredients = data["Ingredients"]
            other = data["Other Materials"]
            instructions = data["Instructions"]
            return name, ingredients, other, instructions
        # if it isn't, then we will ask if the user wants a new file, and proceed from there
        except:
            createNew = input("Either the file is missing, or the recipe is not readable. Would you like to create a new recipe? (y/n): ")
            # if they want a new file, we ask for the file name and call the createFile() function
            if createNew == "y":
                newFileName = input("Please enter the name you would like to call the new file: ")
                createFile(newFileName)
            # if they don't want a new file, we just return False so main knows not to display anything
            else:
                return False
        
# this function will allow the user to edit the recipe and save the changes
def editRecipe(fileName):
    print("Function not implemented yet. If you would like to change a recipe, you must create a new recipe\nand delete the old one.")

# this function will create a new recipe, whether called from readFile() or main()
def createFile(newFileName):
    # before creating the file, we might as well get the information to put in it first
    name = input("\nWhat would you like to name the recipe? ")
    # for ingredients, other materials, and instructions, we will have to make a list and append additional items to it
    print("Great! Now lets get some ingredients recorded.")
    ingredients = []
    addIngredient = ""
    # we want to keep adding ingredients until the user is done
    while addIngredient != "n":
        newIngredient = input("What ingredient would you like to add? Include amounts: ")
        ingredients.append(newIngredient)
        addIngredient = input("Would you like to add another ingredient? (y/n): ")
    # now we need instructions, it will work similarly to the ingredients
    print("Awesome! Now that we have ingredients, how do we prepare this dish?")
    instructions = []
    addInstruction = ""
    while addInstruction != "n":
        newInstruction = input("Please type the instruction you would like to add: ")
        instructions.append(newInstruction)
        addInstruction = input("Would you like to add another instruction? (y/n): ")
    # we can't forget other materials like pans or utensils if there are any
    print("Splendid! What kind of other materials or cooking utensils will we need?")
    other = []
    addOther = ""
    while addOther != "n":
        newOther = input("Enter the material you would like to add: ")
        other.append(newOther)
        addOther = input("Would you like to add another material? (y/n): ")

    # now that we have what we need, we can create the file and write the information in
    doc_ref = db.collection(u'Recipes').document(u'{}'.format(newFileName))
    
    doc_ref.set({
        u'Name': f"{name}",
        u'Ingredients': ingredients,
        u'Instructions': instructions,
        u'Other Materials': other
    })
   

# this function will display the information that the user needs displayed
def display(contents):
    # first we have to sort out the contents
    name = contents[0]
    ingredients = contents[1]
    other = contents[2]
    instructions = contents[3]
    print(f"\n{name}\n")
    print("For this recipe, you will need:")
    # we can loop through the list of ingredients to print them out
    for ingredient in ingredients:
        print(f"\t{ingredient}")
    print("\nAs well as: ")
    # same with other materials
    for material in other:
        print(f"\t{material}")
    print("\nInstructions:")
    # and the same with instructions
    for instruction in instructions:
        print(f"\t{instruction}")
    print()
    

# We need to include this part otherwise it won't run automatically.
if __name__ == "__main__":
  main()