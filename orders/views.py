from django.shortcuts import render, redirect
from orders.models import orders
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def order(request):
	orders_all = orders.objects.exclude(completed=True)
	return render(request, 'orders.html', {'orders': orders_all})

@login_required
def completed_order(request):
	orders_all = orders.objects.exclude(completed=False)
	return render(request, 'orders.html', {'orders': orders_all})


@login_required
def order_detail(request, order_id):
	order = orders.objects.get(id=order_id)
	return render(request, 'order_detail.html', {'order': order})

@login_required
def new_order(request):
	return render(request, 'form.html')

@login_required
def order_submit(request):
	if request.method == 'POST':
		print(request.POST)
		orders_no = orders.objects.count()
		id = orders_no + 1
		name = request.POST['name']
		enroll_no = request.POST['enroll_no']
		room = request.POST['room']
		kurta = request.POST['kurta']
		pyjama = request.POST['pyjama']
		shirt = request.POST['shirt']
		tshirt = request.POST['tshirt']
		pant = request.POST['pant']
		lower = request.POST['lower']
		shorts = request.POST['shorts']
		bedsheet = request.POST['bedsheet']
		pillowcover = request.POST['pillowcover']
		towel = request.POST['towel']
		dupatta = request.POST['dupatta']
		total_clothes = int(kurta) + int(pyjama) + int(shirt) + int(tshirt) + int(pant) + int(lower) + int(shorts) + int(bedsheet) + int(pillowcover) + int(towel) + int(dupatta)
		order = orders(id=id,
		               name=name,
		               enroll_no=enroll_no,
		               room=room,
		               kurta=kurta,
		               pyjama=pyjama,
		               shirt=shirt,
		               tshirt=tshirt,
		               pant=pant,
		               lower=lower,
		               shorts=shorts,
		               bedsheet=bedsheet,
		               pillowcover=pillowcover,
		               towel=towel,
		               dupatta=dupatta,
		               total_clothes=total_clothes,
		               completed=False)
		order.save()
		send_mail('Your dhobi order',
		          'Your order has been submitted',
		          'order@digitaldhobi.com', [f"{enroll_no}@bennett.edu.in"],
		          fail_silently=True)
		return redirect('order_detail', order_id=order.id)

@login_required
def completed(request, order_id):
	order = orders.objects.get(id=order_id)
	order.completed = True
	order.save()
	return redirect('orders')


def home(request):
	return render(request, 'home.html')

@login_required
def home2(request):
	return render(request, 'home2.html')
