from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from blog.models import Choice, Question

# Create your views here.
from blog.models import Person


# def index(request):
#     # result = Person.objects.get(pk=1)
#     # print(result.name)
#     # p = Person(name="王建111", password="123456789")
#     # # p.name = "zhangsan"
#     # # p.password = '123456789'
#     # p.save()
#     # # result = Person.objects.get(pk=2)
#     #
#     # q = Question(question_text="问题1",pub_date=timezone.now())
#     # q.save()
#     latest_quest_list = Question.objects.order_by('pub_date')[:5]
#     template = loader.get_template('blog/index.html')
#     context = {
#         'latest_question_list': latest_quest_list,
#     }
#     # output = ','.join([q.question_text for q in latest_quest_list])
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:20]
    context = {'latest_question_list':latest_question_list}
    return render(request,'blog/index.html',context)



# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request, 'blog/detail.html', {'question': question})

def detail(request , question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', {'question': question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'blog/detail.html', {'question': question})


def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'blog/results.html',{'question':question})
# def vote(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist):
#         return render(request,'blog/detail.html', {
#             'question': question,
#             'error_message:': 'you did not select a choice.',
#         })
#     else:
#         selected_choice.votes.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('results',args=(question_id,)))




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))