# Overview


I started with a program that I had created before, the purpose of which was to read recipes from local json files. However, I wanted to read from a database instead of from local files, since I will not always have my local files on hand. I edited the past program to read and write to a cloud database in Firebase.

I liked my previous digital recipe book, however I wanted to improve it. I thought of cloud databases as a suitable improvement to implement, and went for it.


[Software Demo Video](https://youtu.be/e78-9jwcqiw)

# Cloud Database

I am using Firestore/Firebase, seeing as it is the easiest and most convenient option for this particular program.

The database is arranged into one collection, representing the recipe book. Much like a recipe book has pages with recipes on them, the database has documents with recipes on them. Inside a document, the recipe is arranged into a string field for the name, and three array fields for ingredients, instructions, and other materials needed for the recipe.

# Development Environment

I used Visual Studio Code to develop this program.

I coded this program in python, seeing as the source code I was working with was already in python. Because of this, I used the python libraries for json and firebase_admin.

# Useful Websites

* [Firestore Tutorial](https://www.youtube.com/watch?v=yylnC3dr_no)
* [Firebase Tutorial](https://firebase.google.com/docs/firestore/quickstart#python)
* [Python Module](https://github.com/Teetothejay13/CSE310-Python-Module)

# Future Work

* Deleting recipes
* Alternate credentials for viewing only