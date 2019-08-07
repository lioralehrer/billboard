from django.shortcuts import render

posts=[{
    "title" :"vikings",
    "author": "melech",
    "content":"blablabla01",
    "date_pub":"today"
},
{
    "title" :"vikings2",
    "author": "melech",
    "content":"blablabla02",
    "date_pub":"today"
},
{
    "title" :"vikings3",
    "author": "melech",
    "content":"blablabla03",
    "date_pub":"today"
},
]
def home(request):
    context = {
        "posts" : posts
    }
    return render(request, 'board/home.html', context)

def about(request):
    return render(request, 'board/about.html')    