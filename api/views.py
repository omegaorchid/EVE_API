from django.shortcuts import render


# Create your views here.
def home(request):
    # print(request.META.get('REMOTE_ADDR'))

    form = "stuff"

    template = 'home.html'
    content = {'form': form}

    return render(request=request, template_name=template, context=content)


# def e400():
#     template = '400.html'
#
#     return render(template_name=template)