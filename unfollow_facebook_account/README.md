# Unfollow Facebook accounts.


1 - Open [Facebook.com](https://www.facebook.com)

2- Follow those steps
- Tap Setting & Privacy
- Tap News Feed Preferences
- Tap Unfollow
- Scroll to the end of the list of following
- Right Click on follow button and Inspect it.

3- At Consol Part.
Type Those lines of code

`````javascript
    document.querySelectorAll('[aria-label="Toggle to follow"]')
    var list_of_following = [...document.querySelectorAll('[aria-label="Toggle to follow"]')]
    list_of_following.forEach(list_of_following => console.log(list_of_following))
    list_of_following.forEach(list_of_following => list_of_following.click())

`````
4- Press Enter

You unfollowed all of your followings. Now You can follow what you want . :tw-1f31e:
