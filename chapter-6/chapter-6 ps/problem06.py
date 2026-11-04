post=input("Enter your post: ")
# if (post.lower()=="harry"): 
if(post.lower()in "harry".lower()):
    print("This post is about Harry")
else:
    print("This post is not about Harry")