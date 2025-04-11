import requests

# Fetch data from the API
url = "https://dummyjson.com/posts"
response = requests.get(url)
data = response.json() if response.status_code == 200 else None

if data:
    # Ask the user for a search term
    search_term = input("Enter the search term: ")

    # Search for the term in the posts
    results = []
    for post in data['posts']:
        if search_term.lower() in post['title'].lower() or search_term.lower() in post['body'].lower():
            results.append({
                'title': post['title'],
                'body': post['body'][:50] + '...'  # Displaying first 50 characters of the body
            })

    # Display the results
    if results:
        print("Search Results:")
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Body: {result['body']}")
            print("-" * 40)
    else:
        print("No results found.")
else:
    print("Failed to retrieve data")
