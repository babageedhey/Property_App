from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inquiry = request.POST.get('inquiry')
        user_id = request.POST.get('user_id')
        listing_realtor = request.POST.get('listing_realtor')

        #Check if user is authenticated
        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_id= listing_id, user_id=user_id)
                if has_contacted:
                        messages.error(request, 'You have made inquiry on this Property already')
                        return redirect('/listings/'+listing_id)

        contact = Contact(listing= listing, listing_id=listing_id, name=name, email=email, phone=phone, user_id=user_id, listing_realtor=listing_realtor,inquiry=inquiry)
        
        contact.save()

        #Send Mail
        send_mail(
                'Property LIsting Inquiry',
                'There is an Inquiry on '+ listing + 'Please check the dashboard',
                'babageedheyojo@gmail.com',
                [listing_realtor, 'sobby04@yahoo.co.uk'],
                fail_silently = False
        )

        messages.success(request, 'Your Request has been received, One of our realtor will contact you shortly. ')
        return redirect('/listings/'+listing_id)