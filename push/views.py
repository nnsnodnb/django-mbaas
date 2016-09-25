from django.http import HttpResponse, HttpResponseForbidden
from push.models import DeviceTokenModel, NotificationModel
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from user_agents import parse
import json, urllib, re, ast

def index(request):
    device_tokens = DeviceTokenModel.objects.all()
    return render_to_response('push/top.html',
                             {'device_tokens': device_tokens},
                             context_instance = RequestContext(request))

def sender(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('push/sender.html', c)

def notification_thread(request):
    if request.method == 'POST':
        arrays = request.body.split('&')
        query = {}
        for item in arrays:
            tmp_arrays = item.split('=')
            if 'json' in tmp_arrays[0]:
                json_text = urllib.unquote(tmp_arrays[1])
                query[tmp_arrays[0]] = ast.literal_eval(json_text)
            else:
                query[tmp_arrays[0]] = urllib.unquote(tmp_arrays[1])

        notification = NotificationModel()
        notification.title = query['title']
        notification.message = query['message']
        notification.os_version = query['os_version']
        notification.sound = query['sound']
        notification.badge = query['badge']
        notification.url = query['url']
        if query.has_key('json'):
            notification.json = json.dumps(query['json'])
        if query.has_key('content-available'):
            notification.content_available = True
        if query.has_key('is_production'):
            notification.is_production = True

        notification.save()

        return HttpResponse(query)
    else:
        return HttpResponseForbidden()

@csrf_exempt
def device_token_register(request):
    if request.method == 'POST':# and request.META['HTTP_USER_AGENT'] == 'iOS/nnsnodnb-mBaaS-Service':
        receive_json = json.loads(request.body)
        insert_data = DeviceTokenModel(os_version = receive_json['os_version'],
                                       device_token = receive_json['device_token'])
        insert_data.save()

        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = '"' + receive_json['device_token'] + '" is registered'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponseForbidden()
