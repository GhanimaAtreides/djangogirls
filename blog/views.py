from io import BytesIO
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import array, pi, exp, log
from django.http import HttpResponse
import matplotlib.pyplot as plt

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def experiment_exp_sum(request):
    incoming_date = request.POST.get('date', None)                                                # azért kell a get is, hogy ne hasaljon el, ha nincs date az url-ben, hanem adjon vissza egy None-t
    return render(request, 'blog/experiment_exp_sum.html', {'sum_date': incoming_date})

def experiment_exp_sum_png(request):
    fig = Figure()
    FigureCanvas(fig)
    ax = fig.add_subplot(111)

    N = 12000

    incoming_date = request.GET.get('date', None)       #így lehet kipróbálni: http://localhost:8000/experiments/experiment_exp_sum.png?date=2019-01-03

    year, month, day = incoming_date.split('-')
    year = int(year[2:4])
    month = int(month)
    day = int(day)

    def f(n, year, month, day):
        return n/day + n**2/month + n**3/year 

    z = array( [exp( 2*pi*1j*f(n, year, month, day) ) for n in range(3, N+3)] )
    z = z.cumsum()

    ax.plot(z.real, z.imag, color='#338399')
    ax.set_aspect(1)

    buf = BytesIO()
    fig.savefig(buf, format='png')

    return HttpResponse(buf.getvalue(), content_type='image/png')
