from django.shortcuts import render,redirect
from .models import Customer, Category, Products

# Create your views here.
def about(request):
    return render(request, 'about_us.html')

def index(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)

    else:
        products = Products.get_all_products()
    # products=Products.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    print(products)

    return render(request, 'index.html', data)

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = Customer.get_customer_by_email(email)
    error_message = None

    if customer:
        if password == customer.password:
            print("Login")
            request.session['customer'] = customer.id
            request.session['email'] = customer.email
            request.session['name'] = customer.first_name
            return redirect('/index/')
        else:
            print("NOT LOGIN")
            error_message = 'Invalid Email or Password!!'
    else:
        error_message = "Invalid Email or Password"
    return render(request, 'login.html', {'error': error_message})

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cust = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)
        cust.save()
        return redirect('/index/')
    else:
        print("invalid")
        return render(request, 'signup.html')
