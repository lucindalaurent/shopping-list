from django.shortcuts import render
#menghubungkan template dan model, misah tampilan data
# Create your views here.
def show_main(request):
    context = {
        'name': 'Lucinda Laurent',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
