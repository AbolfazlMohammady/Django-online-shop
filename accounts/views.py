from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout ,authenticate


from . import forms

def signup_view(request):

    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = forms.CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def profile_view(request):
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # پس از ذخیره شدن تغییرات، کاربر به صفحه پروفایل باز می‌گردد
    else:
        form = forms.UserProfileForm(instance=request.user)
    return render(request, 'account/my-account.html', {'form': form})




@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        # Get form data
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Update basic info (first_name, last_name, email)
        user.first_name = request.POST.get('f_name')
        user.last_name = request.POST.get('l_name')
        user.email = request.POST.get('email')
        user.save()

        # Check if the user wants to change the password
        if current_password and new_password1 and new_password2:
            # Verify if the current password is correct
            if user.check_password(current_password):
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()

                    # Keep the user logged in after password change
                    update_session_auth_hash(request, user)
                    messages.success(request, 'پسورد با موفقیت تغییر کرد.')
                else:
                    messages.error(request, 'پسورد جدید مطابقت ندارد.')
            else:
                messages.error(request, 'پسورد فعلی اشتباه است.')

        return redirect('profile')

    return render(request, 'profile_form.html', {'user': user})




