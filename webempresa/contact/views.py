from django.shortcuts import render, redirect
from django.urls      import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
       contact_form = ContactForm(data=request.POST)
       if contact_form.is_valid():
           name    = request.POST.get('name','')
           email   = request.POST.get('email','')
           content = request.POST.get('content','')
           # enviando correo...
           email = EmailMessage(
               "La Caffettiera: Nuevo mensaje de contacto",
               "De {} <{}>\n\n{}".format(name, email, content),
               "no-contestar@inbox.mailtrap.io",
               ["rptinoco.nun@gmail.com","jesus.eep@gmail.com"],
               reply_to=[email]
           )

           try:
               email.send()
               # OK
               return redirect(reverse('contact')+"?OK")
           except:
               # FAIL    
               return redirect(reverse('contact')+"?FAIL")

    return render(request,"contact/contact.html",{'form':contact_form})
