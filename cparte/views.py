from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from cparte.models import ContributionPost

import logging
import pickle


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Welcome to the CParte application!")


def posts(request):
    contribution_posts = ContributionPost.objects.all()
    context = {'posts': contribution_posts}
    return render(request, 'cparte/posts.html', context)


def listen(request, channel_name):
    initiatives = [1, 2]   # Add here the ids of the initiatives
    accounts = [1]  # Add here the ids of the accounts
    str_meta_channel = request.session['meta_channel']
    meta_channel = pickle.loads(str_meta_channel)
    if meta_channel.channel_enabled(channel_name):
        meta_channel.authenticate(channel_name)
        meta_channel.set_initiatives(channel_name, initiatives)
        meta_channel.set_accounts(channel_name, accounts)
        meta_channel.listen(channel_name)
        request.session['meta_channel'] = pickle.dumps(meta_channel)
    else:
        logger.error("The channel is not enabled")
    if settings.URL_PREFIX:
        redirect_url = "%s/admin/cparte/channel/" % settings.URL_PREFIX
    else:
        redirect_url = "/admin/cparte/channel/"
    return HttpResponseRedirect(redirect_url)


def hangup(request, channel_name):
    str_meta_channel = request.session['meta_channel']
    meta_channel = pickle.loads(str_meta_channel)
    meta_channel.disconnect(channel_name)
    request.session['meta_channel'] = pickle.dumps(meta_channel)
    if settings.URL_PREFIX:
        redirect_url = "%s/admin/cparte/channel/" % settings.URL_PREFIX
    else:
        redirect_url = "/admin/cparte/channel/"
    return HttpResponseRedirect(redirect_url)