import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Iterate through the posts and print the titles
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

# Function to fetch posts and save them to a CSV file
def fetch_and_save_posts():
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Prepare data for CSV
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data to CSV file
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
    else:
        print("Failed to fetch posts")
