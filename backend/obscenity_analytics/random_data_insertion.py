import pymongo
from datetime import datetime, timedelta
import random

# Connect to MongoDB Atlas
client = pymongo.MongoClient('mongodb+srv://admin:admin@nsfw.crfx0tb.mongodb.net/')
db = client['NSFW']
collection = db['NSFW']

# Function to add data to the collection
def add_data(link, size, date_of_acquisition, source, result, type_of_file):
    data = {
        'link': link,
        'size': size,
        'date_of_acquisition': date_of_acquisition,
        'source': source,
        'result': result,
        'type_of_file': type_of_file
    }
    collection.insert_one(data)

# Example usage - adding multiple random documents
num_documents = 10  # Number of random documents to add

# Generate and add random documents
for _ in range(num_documents):
    link = 'https://example.com_{}/'.format(random.randint(1, 10000))
    size = random.uniform(100, 1000)
    date_of_acquisition = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 180))
    source = 'Example Source {}'.format(random.randint(1, 10))
    result = random.choice(['SFW', 'NSFW'])
    type_of_file = random.choice(['image', 'video', 'text'])
    # print(date_of_acquisition)

    add_data(link, size, date_of_acquisition, source, result, type_of_file)

print('Data added successfully.')