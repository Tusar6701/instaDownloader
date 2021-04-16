import instaloader

ig= instaloader.Instaloader()
dp= input("Enter the instagram username : ")

ig.download_profile(dp, profile_pic_only=True)
print("The profile was downloaded successfully, ENJOYYYYY!!!")