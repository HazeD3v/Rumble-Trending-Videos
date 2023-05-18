import requests
from bs4 import BeautifulSoup

#Rumbles Trending Page
URL = "https://rumble.com/videos?sort=views&date=today"
#Get the page content
page = requests.get(URL)

#Parse the page content through bs
soup = BeautifulSoup(page.content, "html.parser")

#Create a variable 'videos' that hold a list of each video 
videos = soup.find_all('li', class_='video-listing-entry')

#Iterate over each video and store the details
for k, vid in reversed(list(enumerate(videos))):
    title = vid.find("h3", class_="video-item--title").text.strip()
    author = vid.find("div", class_="ellipsis-1").text.strip()
    likes = vid.find("div", class_="rumbles-vote-up").text.strip()
    dislikes = vid.find("div", class_="rumbles-vote-down").text.strip()
    views = vid.find("div", class_="video-item--views").text.strip()
    comments = vid.find("div", class_="video-item--comments")
    duration = vid.find("span", class_="video-item--duration")
    time = vid.find("time", class_="video-item--time").text.strip()
    link = vid.find("a", class_="video-item--a", href=True)['href']
	
	#Output each videos details to the user
    print(f"#{k + 1} on Trending!")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Likes: {likes}")
    print(f"Dislike: {dislikes}")
    print(f"Views: {views}")
	#If there is no comments we get a NoneType Error
    if comments is not None:
        print(f"Comments: {comments.text.strip()}")
    print(f"Uploaded: {time}")
	#Check if this video is currently live
    if duration is None:
        print("LIVE!")
    else:
        print(f"Duration: {duration['data-value']}")
    print(f"Link: https://rumble.com{link}\n")
