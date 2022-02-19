import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize using the application default credentials
cred = credentials.Certificate("C:/Users/teeto/hello/CSE310/cloud-database-module-firebase-adminsdk-x784k-bf11e67e05.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# create document reference
doc_ref = db.collection(u'Recipes').document(u'Banana Bread Recipe')

# write
doc_ref.update({
    u'Name': "Chocolate Chip Banana Bread"
})

# read
try:
    doc = doc_ref.get()
    data = doc.to_dict()
    print(data["Name"])
    
except:
    print("Not found")

