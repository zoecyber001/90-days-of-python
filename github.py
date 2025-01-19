import requests

def fetch_github_user_data(username):
    """Fetch user data from GitHub API."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return user data as JSON
    else:
        print(f"Error: Unable to fetch data for user '{username}'. Status code: {response.status_code}")
        return None

def display_user_data(user_data):
    """Display user data in an organized manner."""
    print("User Data:")
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data.get('name', 'N/A')}")
    print(f"Bio: {user_data.get('bio', 'N/A')}")
    print(f"Public Repositories: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
    print(f"Profile URL: {user_data['html_url']}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    user_data = fetch_github_user_data(username)
    
    if user_data:
        display_user_data(user_data)
