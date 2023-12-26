from django_otp.plugins.otp_totp.models import TOTPDevice
from .models import OTP, CustomUser
from .forms import OTPForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def generate_otp(request):
    user = request.user
    totp_device, created = TOTPDevice.objects.get_or_create(user=user)
    otp_code = totp_device.generate_otp()
    OTP.objects.create(user=user, totp_device=totp_device, otp_code=otp_code)

    # Send the OTP code to the user (e.g., via email or SMS)
    return otp_code  # Return the OTP code for demonstration purposes

def send_otp(request):
    if request.user.is_authenticated:
        email = request.user.email
        otp = generate_otp()  # Corrected the function name
        """Send the generated otp via email"""
        send_otp_via_email(otp, email)

def send_otp_via_email(otp, email):
    subject = 'Your one-time Password (OTP)'
    message = f'Your OTP is {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def verify(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:  # Corrected the exception type
        return HttpResponse('User not found!')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']

            # Retrieve the OTP record from the database
            otp_record = OTP.objects.filter(user=user, otp_code=otp_code).first()

            if otp_record and otp_record.totp_device.verify_otp(otp_code):
                # OTP verification successful
                otp_record.delete()  # Remove the used OTP record
                return HttpResponse('OTP Verified Successfully!')
            else:
                # Invalid OTP
                form.add_error('otp_code', 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()

    return render(request, 'verify_otp.html', {'form': form, 'user': user})
