from django.shortcuts import render, redirect

from community.models import Dashboard, Question, AddReply

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import (UpdateView,
                                        CreateView,
                                        DeleteView )

from django.db.models import Q
import datetime
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# VIEWS 


class Welcome(TemplateView):
    template_name = "community/welcome.html"


# class About(TemplateView):
#     template_name = "community/about.html"


@method_decorator(login_required, name="dispatch")    
class QuestionCreate(CreateView):
    model = Question
    fields = ["title", "description", "tag1", "tag2", "tag3"]

    def form_valid(self, form):

        self.object = form.save()
        self.object.uploaded_by = self.request.user.dashboard
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @method_decorator(login_required, name="dispatch")


class QuestionListView(ListView):
    modal = Question
    paginate_by = 4
    template_name = "question_list.html"

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
           si = ""
        return Question.objects.filter(Q(cr_date__icontains=si) | Q(description__icontains=si) |
                                       Q(title__icontains=si) | Q(tag1__icontains=si) |
                                       Q(tag2__icontains=si) | Q(tag3__icontains=si)).order_by("-id")


@method_decorator(login_required, name="dispatch")
class QuestionDetailView(DetailView):
    model = Question
    template_name = "community/question_detail.html"
    def get_context_data(self, **kwargs):

        context = super(DetailView, self).get_context_data(**kwargs)
        context['Question'] = Question.objects.all()
        # return context
        blg = AddReply.objects.all().order_by("-id")
        context['blg'] = AddReply.objects.all().order_by("-id")
        return context


# @method_decorator(login_required, name="dispatch")
# class QuestionUpload(View):
#     def get(self, request):
#         by1 = request.user.username
#         to1 = request.GET.get('quesid', None)
#         reply1 = request.GET.get('reply', None)

#         by2 = Dashboard.objects.get(user__username__icontains=by1)
#         to2 = Question.objects.get(id=to1)

#         obj = AddReply.objects.create(
#             by = by2,
#             reply = reply1,
#             to = to2
#         )

#         user = {
#                 'id':obj.id,
#                 'to':obj.to,
#                 'by':obj.by,
#                 'reply': obj.reply,
#             }

#         data = {
#             'user': user
#         }
#         return JsonResponse(data)


@login_required
def quesUpload(request):
    if request.method == 'GET':
        to1 = request.GET.get('quesid')
        reply = request.GET.get('replymsg')
        by1 = request.user.username

        to = Question.objects.get(id=to1)
        by = Dashboard.objects.get(id=request.user.id)

        # to = Question.objects.get(id=to1)

        # print(to)
        # print(by)
        # print(reply)
        # print(type(to))
        # print(type(by))
        # print(type(reply))
        

        if by != '' or to != '':
            instance = AddReply.objects.create(
                reply=reply,
                by=by, 
                to=to,
                cr_date = datetime.datetime.now()
            )   

            instance.save()
            messages.success(request, 'Your Answer has been successfully Uploaded!')

            return redirect('/forum/question/' + to1)
        else:
            print("Could not create")
            messages.success(request, 'Oops!..Your Reply has not been Uploaded!')
            return redirect('/forum/question')
    else:
        print("failed to upload")
        messages.success(request, 'Oops!..Your reply request failed!')
        return render(request, '/forum/question')

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


@method_decorator(login_required, name="dispatch")
class DashboardDetailView(DetailView):
    model = Dashboard


@method_decorator(login_required, name="dispatch")
class DashboardUpdateView(UpdateView):
    modal = Dashboard
    fields = ["name", "age", "gender", "profession", "country", "description", "image"]
    
    def get_queryset(self):
        return Dashboard.objects.filter()


@method_decorator(login_required, name="dispatch")
class DashboardListView(ListView):
    modal = Dashboard
    paginated_by = 4
    template_name = "dashboard_list.html"

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
           si = ""
        return Dashboard.objects.filter().order_by("-id")

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
