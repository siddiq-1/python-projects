from pytube import YouTube


link="https://youtu.be/dNCWe_6HAM8"

youtube_1=YouTube(link)

videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)

strm=int(input("\nEnter the index no of list: "))
videos[strm].download()
print("\n Succesfully downloaded your video")






