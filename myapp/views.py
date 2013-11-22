from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.template import RequestContext
from django.utils.encoding import smart_unicode
from django.utils import simplejson

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
        
def index(request):
    records_dict_list =  __read(request)
    site.addsitedir('site-packages','.')
    path = sys.path
    # for csrf
    return render_to_response('index.html',
                              { 'records': records_dict_list,
                                'path'   : path
                                },
                              context_instance=RequestContext(request))


def __createHttpResponseJson( results ) :
    response = HttpResponse(
                            mimetype     = 'application/json; charset=utf-8',
                            content_type = 'application/json; charset=utf-8',
                            )
    response.__setitem__( 'Access-Control-Allow-Origin', '*' )
    response.content = simplejson.dumps( results, ensure_ascii = False )
    
    return response

def __read(request, sort_key='-score'):
    if request.GET.has_key('sort_key'):
        sort_key = request.GET['sort_key'] #@todo:[SMT] refactor, GET? POST? both??
        
    records = models.Record.get_all().order_by(sort_key)
    records_dict_list = [ {'id'          : str(record.id),
                           'username'    : smart_unicode(record.username),
                           'description' : smart_unicode(record.description),
                           'score'       : str(record.score),
                           'datetime'    : str(record.datetime.astimezone(pytz.timezone('Asia/Tokyo'))),
                           'grade'       : __judgeGrade(record.score),
                           } for record in records ]
    return records_dict_list

def read(request, sort_key='-score'):
    records_dict_list = __read(request, sort_key)
    records_json = __createHttpResponseJson( records_dict_list )
    return records_json

def create(request):
    record = models.Record( username = request.POST['username'],
                            description = request.POST['description'],
                            score = request.POST['score'],
                            )
    record.save()
    return index(request)

def update(request):
    record = models.Record.objects.get(id=request.POST['id'])
    record.username = request.POST['username']
    record.description = request.POST['description']
    record.score = request.POST['score']

    record.save()
    return index(request)

def delete(request):
    record = models.Record.objects.get(id=request.POST['id'])
    record.delete()
    return index(request)

