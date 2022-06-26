from django.shortcuts import render
from .models import Category, Topic, Post
from django.core.paginator import Paginator
from .forms import TopicForm, PostForm
from django.shortcuts import redirect


def home_forum(request):
    category = Category.objects.all()


    return render(request, 'forum/forum.html', {'category': category,})



def category(request, pk):

    topic = Topic.objects.filter(category_id=pk)


    return render(request, 'forum/category.html', {'topic': topic, 'pk': pk})



def create_topic(request, pk):
    topic = Topic.objects.filter(pk=pk)
    for item in topic:
        category_id = item.id


    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.category_id = category_id
            object.user_id = request.user.id
            print(object)
            object.save()
            return redirect(f'/forum/category/{pk}')
    return render(request, 'objects/create_object.html', {'form': form, })


def update_topic(request, pk):
    topic = Topic.objects.get(id=pk)
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.id = pk
            topic.save()
            return redirect(f'/forum/category/{topic.category_id}')
    return render(request, 'objects/create_object.html', {'form': form})



def delete_topic(request, pk):
    data = Topic.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect(f'/forum/category/{data.category_id}')
    return render(request, 'forum/delete.html')



def post(request, pk):

    post = Post.objects.filter(topic_id=pk)

    paginator = Paginator(post, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'forum/post.html', {'page_obj': page_obj, 'pk':pk })



def create_post(request, pk):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.topic_id = pk
            object.user_id = request.user.id
            print(object)
            object.save()
            return redirect(f'/forum/post/{pk}')
    return render(request, 'objects/create_object.html', {'form': form, })


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = pk
            post.save()
            return redirect(f'/forum/post/{post.topic_id}')
    return render(request, 'objects/create_object.html', {'form': form})



def delete_post(request, pk):
    data = Post.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect(f'/forum/post/{data.topic_id}')
    return render(request, 'forum/delete.html')