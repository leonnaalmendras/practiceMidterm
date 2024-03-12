from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!")

def installation(request):
    context = {
        'title': 'INSTALL HOME ASSISTANT ON ODROID DEVICES',
        'subtitle' : 'A more powerful alternative to Raspberry Pi',
        'skills' : ['You\'re comfortable following instructions on:', 'Writing boot images', 'Installing an SD card or eMMC'],
        'tools' : ['An Odroid device', 'MicroSD card or eMMC', 'Ethernet connection']
    }

    return render(request, "installation.html", context)

def configuration(request):
    context = {
        'title' : 'Configuration.yaml',
        'info' : "While you can configure most of Home Assistant directly from the user interface under Settings, some parts need you to edit configuration.yaml. This file contains integrations \
        to be loaded along with their configurations. Throughout the documentation you will find snippets that you can add to your configuration file to enable specific functionality. \
        If you run into trouble while configuring Home Assistant, refer to the configuration troubleshooting page and the configuration.yaml examples.",
    }
    return render(request, "configuration.html", context)

def automation(request):
    context = {
        'title' : 'Automating Home Assistant',
        'info' : 'Home Assistant contains information about all your devices and services.  This information is available for the user in the dashboard and \
            it can be used to trigger automations. And that’s fun! Automations in Home Assistant allow you to automatically respond to things that happen. You can turn the lights on at sunset or \
                pause the music when you receive a call. If you are just starting out, we recommend that you start with blueprint automations. These are ready-made automations by the community that you only need to configure.'
    }

    return render(request, "automation.html", context)

def index(request):
    return render(request, 'index.html')