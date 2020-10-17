#Importing Required modules
from os import system
try:
	from pytube import YouTube
	from pytube import Playlist
	import urllib.request
	import re
except Exception as e:
	print("Some modules are missing {}".format(e))

	#installing required modules
	try:
		system("pip3 install pytube3 regex urllib3")	#for ubuntu
	except:
		system("pip install pytube3 regex urllib3")	#for windows
	

	


#Starting instruction for the user
def start():

	try:	#making directories to save file

		system("mkdir -p youtube/video")	
		system("mkdir -p youtube/audio")

	except:	#directories already exists
		pass


	print("\nWelcome To Simple YouTube Downloader\n")
	print("1. Search and Download ")
	print("2. Download Using URL ")

	option = int(input("Enter your option : "))
	run(option)

#options to choose search/download
def run(option):
	if option == 1:
		search()
	elif option == 2:
		get_url()
	else:
		print("Wrong input\n")		#if the user entered a wrong number 
		start()						#program starts from the begining

#this will return the first video link
def search():
	search_keyword = input("Search : ")
	search_keyword = search_keyword.replace(" ", "+")
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
	
	if video_ids == []: #if no video is found , the list will be empty
		print("\nNo Video Found , Try Again !! \n")
		search()
	else:
		url ="https://www.youtube.com/watch?v=" + video_ids[0]


	get_details(url)

#getting the url of the video
def get_url():
	url = input("Please Paste the url : ")

	if "https://www.youtube.com" in url:
		get_details(url)
	else:
		print("\nInvalid url / Please paste the entire URL\n")
		get_url()

def get_details(url):

	video = YouTube(url)
	
	print(video.title)		#show the title of the video

	print("\n1. Get Video\n2. Get Audio\n")
	option = int(input("Choose 1 or 2 : "))

	if option ==1:
		get_video(video)		#download video file //passing the pytube object
	elif option ==2:
		get_audio(video)		#download audio file //passing the pytube object
	else:
		get_details(url)		#wrong option 

def get_video(video):

	for x in video.streams.filter(file_extension = "mp4"):
		res = x.resolution
		tag = x.itag

		#some files doesnt show filesize , it creates a traceback error , therefore using try and except
		try:
			size = video.streams.get_by_itag(tag).filesize /1000000
		except Exception:
			size ="Null"


		print("tag : {} || resolution : {} || size : {} MB ".format(tag,res,size))

	tag = int(input("Enter the tag number of resolution needed: "))

	video.streams.get_by_itag(tag).download(output_path='youtube/video')

def get_audio(video):

	for x in video.streams.filter(type ='audio'):
		abr = x.abr
		tag = x.itag

		#some files doesnt show filesize , it creates a traceback error , therefore using try and except
		try:
			size = video.streams.get_by_itag(tag).filesize /1000000
		except Exception:
			size = "Null "

		print("tag : {} || bitrate : {} || size : {} MB ".format(abr,tag,size))

	tag = int(input("Enter the tag number of bitrate needed: "))

	video.streams.get_by_itag(tag).download(output_path='youtube/audio')



start()
	


