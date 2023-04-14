from django.shortcuts import render
import httplib2
import json
# Create your views here.

total_count = 0
count_by_country = {}

http = httplib2.Http()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_country_from_ip(ip_address):
    global http
    # ip_address='73.170.135.6'
    url = f'https://ipapi.co/{ip_address}/json/'
    resp, content =http.request(url,method="GET")
    data = json.loads(content)
    name = data['country_name']
    return name
    


def handle_click(request):
    global total_count
    global count_by_country

    if request.method == 'GET':       
        
        data = count_by_country

        return render(request, 'click_view.html', context={'data': data, 'count': total_count})

    if request.method == 'POST':
        total_count += 1
    
        ip = get_client_ip(request)
        country = get_country_from_ip(ip)

        if country in count_by_country:
            count_by_country[country] += 1
        else :
            count_by_country[country] = 1
        
        data = count_by_country

        return render(request, 'click_view.html', context={'data': data, 'count': total_count})
