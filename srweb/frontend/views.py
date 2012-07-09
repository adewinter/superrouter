# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def connectivity(request):
    context = {}
    context.update({'wifi_list': get_wifi_list()})
    context.update({'device_status': get_interface_status()})
    return render(request, "frontend/connectivity.html", context)

def media(request):
    return render(request, template_name="frontend/base.html")

def settings(request):
    return render(request, template_name="frontend/base.html")

def advanced(request):
    return render(request, template_name="frontend/base.html")

def data(request):
    print 'Got Request %s' % request
    return HttpResponse('bla')

def get_wifi_list():
    """
    just returns a list of strings containing the SSIDs
    """
    return _fake_get_ssids()


def get_interface_status():
    """
    Return a dict. E.g.
    {
        "wlan0": {
            "label": 'Wireless (External)',
            "connected": True,
            "enabled": True,
        },
        "eth0": {
            "label": 'Ethernet',
            "connected": False,
            "enabled": True
        },
        "bluetooth": {
            "label": 'BlueTooth',
            "connected": False,
            "enabled": False,
        }
    }
    """
    return _fake_get_interface_status()

def _sys_get_interface_status():
    """
    STUB FOR THE F'REAL SHIT
    """
    pass

def _fake_get_interface_status():
    return {
        "wlan0": {
            "label": 'Wireless (External)',
            "connected": True,
            "enabled": True,
        },
        "eth0": {
            "label": 'Ethernet',
            "connected": False,
            "enabled": True
        },
        "bluetooth": {
            "label": 'BlueTooth',
            "connected": False,
            "enabled": False,
        }
    }

def _sys_get_ssids():
    """
    #STUB CHANGE TO REAL THING
    """
    pass

def _fake_get_ssids():
    return ['lxion', "Artisan's Asylum 5ghz", "Fredland", "Some SSIDs"]