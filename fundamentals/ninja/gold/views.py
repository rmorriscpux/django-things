from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'index.html')

def process_gold(request):
    gold_obtained = 0
    if request.POST['location'] == "Farm":
        gold_obtained = random.randint(10, 20)
    elif request.POST['location'] == "Cave":
        gold_obtained = random.randint(5, 10)
    elif request.POST['location'] == "House":
        gold_obtained = random.randint(2, 5)
    elif request.POST['location'] == "Casino":
        gold_obtained = random.randint(-50, 50)
    else:
        return redirect('/') # Failsafe.
    
    request.session['gold'] += gold_obtained

    if gold_obtained < 0:
        request.session['activity'].insert(0, "Lost " + str(-gold_obtained) + " gold at the " + request.POST['location'] + "! (" + datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p") + ")")
    else:
        request.session['activity'].insert(0, "Earned " + str(gold_obtained) + " gold at the " + request.POST['location'] + "! (" + datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S %p") + ")")

    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'].clear()
    return redirect('/')