from pymongo import MongoClient
def get_database():

# Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tomfyfe:Batdad66696@offical.owwmlam.mongodb.net/?retryWrites=true&w=majority&appName=offical"
    
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']