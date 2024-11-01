from django.shortcuts import render

# Create your views here.
class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("register_successful")

    @transaction.atomic
    def form_valid(self, form):
        user = CustomUser.objects.create_user(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        CustomUserProfile.objects.create(
            user=user,
            id_number=form.cleaned_data["id_number"],
            occupation=form.cleaned_data["occupation"],
            address=form.cleaned_data["address"],
            street_number=form.cleaned_data["street_number"],
            flat_number=form.cleaned_data["flat_number"],
            zip_code=form.cleaned_data["zip_code"],
            city=form.cleaned_data["city"]).save()