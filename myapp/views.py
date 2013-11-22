from django.http import HttpResponse

from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.template import RequestContext
from django.utils.encoding import smart_unicode
import sys
import time
import pytz

import site
import models



def main(request):
    return HttpResponse("Hello, nihohi!<br><a href='./mysite/myapp/'>Go to sample page</a>")


def __judgeGrade(score):
    if score > 100000:
        grade = "gradeA" 
    elif score > 1000:
        grade = "gradeC" 
    elif score > 100:
        grade = "gradeX"
    else:
        grade = "gradeU"
    return grade
        
def read(request, sort_key='-score'):
    if request.GET.has_key('sort_key'):
        sort_key = request.GET['sort_key'] #@todo:[SMT] refactor, GET? POST? both??
        
    records = models.Record.get_all().order_by(sort_key)
    records_tmp = [ {'id'          : str(record.id),
                     'username'    : smart_unicode(record.username),
                     'description' : smart_unicode(record.description),
                     'score'       : str(record.score),
                     'datetime'    : str(record.datetime.astimezone(pytz.timezone('Asia/Tokyo'))),
                     'grade'       : __judgeGrade(record.score),
                     } for record in records ]
    site.addsitedir('site-packages','.')
    path = sys.path
    # for csrf
    return render_to_response('index.html',
                              { 'records': records_tmp,
                                'path'   : path
                                },
                              context_instance=RequestContext(request))

def create(request):
    record = models.Record( username = request.POST['username'],
                            description = request.POST['description'],
                            score = request.POST['score'],
                            )
    record.save()
    return read(request)

def update(request):
    record = models.Record.objects.get(id=request.POST['id'])
    record.username = request.POST['username']
    record.description = request.POST['description']
    record.score = request.POST['score']

    record.save()
    return read(request)

def delete(request):
    record = models.Record.objects.get(id=request.POST['id'])
    record.delete()
    return read(request)

