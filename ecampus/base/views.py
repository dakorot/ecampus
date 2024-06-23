from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from .models import Profile, Student, Lecturer, Post, Comment, Message, Grade, Question, Choice
from django.db.models import F
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, MessageForm, GradeForm, VoteForm
from django.contrib.auth.decorators import permission_required


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register_form.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong during the registration')
    context = {'form': form}
    return render(request, 'base/login_register_form.html', context)


def home_page(request):
    # context = {}
    return render(request, 'base/home.html')


def profile_page(request, pk=None):
    if pk is None:
        profile = request.user.profile
    else:
        profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)


def feed_page(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/feed.html', context)


def user_post(request, pk):
    user_post = Post.objects.get(id=pk)
    comments = user_post.comment_set.all().order_by('created')

    if request.method == "POST":
        comment = Comment.objects.create(
            user=request.user,
            post=user_post,
            body=request.POST.get('body')
        )
        return redirect('user_post', pk=user_post.id)

    context = {'user_post': user_post, 'comments': comments}
    return render(request, 'base/post.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.author = request.user
            form.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    user_post = Post.objects.get(id=pk)
    form = PostForm(instance=user_post)

    if request.user != user_post.author:
        return HttpResponse('You are not the author.')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=user_post)
        if form.is_valid():
            user_post.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    user_post = Post.objects.get(id=pk)
    if request.method == 'POST':
        user_post.delete()
        return redirect('feed')
    context = {'object': user_post}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.user != comment.user:
        return HttpResponse('You are not the author.')

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('feed')

    context = {'form': form}
    return render(request, 'base/comment_form.html', context)


@login_required(login_url='login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('feed')

    context = {'object': comment}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def messages_page(request):
    inbox_messages = Message.objects.filter(receiver=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    context = {'inbox_messages': inbox_messages, 'sent_messages': sent_messages}
    return render(request, 'base/messages.html', context)


@login_required(login_url='login')
def create_message(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            form.save()
            return redirect('messages')
    context = {'form': form}
    return render(request, 'base/message_form.html', context)


@login_required(login_url='login')
def performance_page(request):
    return render(request, 'base/performance.html')


@login_required(login_url='login')
@permission_required('base.view_grades', login_url='login', raise_exception=HttpResponseForbidden)
def grades_page(request):
    grades = Grade.objects.all()
    context = {'grades': grades}
    return render(request, 'base/grades.html', context)


@login_required(login_url='login')
@permission_required('base.add_grades', login_url='login', raise_exception=HttpResponseForbidden)
def create_grade(request):
    form = GradeForm()
    lecturer = Lecturer.objects.get(user=request.user)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.lecturer = lecturer
            form.save()
            return redirect('grades')
    context = {'form': form}
    return render(request, 'base/grade_form.html', context)


@login_required(login_url='login')
@permission_required('base.edit_grades', login_url='login', raise_exception=HttpResponseForbidden)
def update_grade(request, pk):
    grade = Grade.objects.get(id=pk)
    form = GradeForm(instance=grade)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            grade.save()
            return redirect('grades')
        else:
            messages.error(request, 'Something went wrong')

    context = {'form': form}
    return render(request, 'base/grade_form.html', context)


@login_required(login_url='login')
@permission_required('base.delete_grades', login_url='login', raise_exception=HttpResponseForbidden)
def delete_grade(request, pk):
    grade = Grade.objects.get(id=pk)

    if request.method == 'POST':
        grade.delete()
        return redirect('grades')

    context = {'object': grade}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def examinations_page(request):
    return render(request, 'base/examinations.html')


def documents_page(request):
    return render(request, 'base/documents.html')


@login_required(login_url='login')
def subjects_choice_page(request):
    questions = Question.objects.all()
    student = Student.objects.get(user=request.user)

    context = {'questions': questions, 'student': student}
    return render(request, 'base/subjects_choice.html', context)


def vote(request, question_pk):
    question = Question.objects.get(id=question_pk)
    form = VoteForm()
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = VoteForm(request.POST, question_id=question_pk)
        if form.is_valid():
            choices = form.cleaned_data['choices']
            print(choices)
            for choice in choices:
                choice.votes = F('votes') + 1
                # choice.save(commit=False)
                choice.save()
                student.choices.add(choice)
            return redirect('vote-results', question_pk=question_pk)
    elif request.method == 'GET':
        form = VoteForm(request.POST, question_id=question_pk)
    context = {'question': question, 'form': form}
    return render(request, 'base/vote_form.html', context)


def vote_results(request, question_pk):
    question = Question.objects.get(id=question_pk)
    choices = question.choice_set.all()
    students = Student.objects.all()

    context = {'question': question, 'choices': choices, 'students': students}

    return render(request, 'base/vote_results.html', context)


def help_page(request):
    return render(request, 'base/help.html')
