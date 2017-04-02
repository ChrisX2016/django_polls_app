from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .models import Choice, Question, Vote, UserProfile
from django.db.models import Sum
from django.contrib import messages
from .form import RegisterForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        myvote={}
        myvote['choice'] = selected_choice
        if request.user.id:
            myvote['voter'] = request.user
        mynewvote = Vote(**myvote)
        mynewvote.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add(request):
    if request.method == 'POST':
        content = request.POST
        print(content)
        allChoice = []
        for i in content.getlist('choice'):
            if i != '':
                allChoice.append(i)
        if content['question'] and allChoice:
            question = {}
            question['question_text'] = content['question']
            question['pub_date'] = timezone.now()
            # print(type(request.user))
            if request.user.id:
                question['owner'] = request.user

            newQuestion = Question(**question)
            newQuestion.save()


            for temp in allChoice:
                if temp != '' and temp!= None:

                    # print(type(Choice.choice_text))
                    choice = {}
                    choice['question'] = newQuestion
                    choice['choice_text'] = temp
                    choice['votes'] = 0
                    newChoice = Choice(**choice)
                    newChoice.save()

            latest_question_list = Question.objects.order_by('-pub_date')
            add_status = 1
            return render(request, 'polls/add.html',{'add_status':add_status})
        else:
            add_status = -1
            return render(request, 'polls/add.html',{'add_status':add_status})
    return render(request, 'polls/add.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/polls')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # todo email check
        login(request, user)
        messages.success(request, "Welcome "+ user.get_username())
        return HttpResponseRedirect('/polls')
    else:
        content={}
        content['err_msg']='Username or Password Error!'
        content['latest_question_list']=Question.objects.order_by('-pub_date')
        # print(content)
        return render(request, 'polls/index.html',content)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/profile/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],first_name=form.cleaned_data['firstname'],
                                            last_name=form.cleaned_data['lastname'])
            user.save()
            userprofile = UserProfile(user=user,birthday=form.cleaned_data['birthday'])
            userprofile.save()
            login(request, user)
            return HttpResponseRedirect('polls/profile/')
        else:
            return render(request,'polls/signup.html',{'form':form})
    else:
        form = RegisterForm()
        context = {'form':form}
        return render(request,'polls/signup.html',context)


def myvote_view(request):
    all_votes = Vote.objects.filter(voter=request.user.id).annotate(total_votes=Sum('choice__votes'))
    
    return render(request, 'polls/myvote.html',{'all_votes':all_votes})


def myquestion_view(request):
    all_questions = Question.objects.filter(owner_id=request.user.id).annotate(total_votes=Sum('choice__votes')).values()

    return render(request, 'polls/myquestion.html',{'all_questions':all_questions})


def profile_view(request):
    all_votes = Vote.objects.filter(voter=request.user.id).all()
    return render(request, 'polls/profile.html',{'all_votes':all_votes})

# todo reset password through email
