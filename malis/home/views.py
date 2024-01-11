from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 
from django.contrib.auth import logout
from .models import *
from django.utils import timezone
from django.contrib.auth.views import LogoutView
from django.db.models import Q
from decimal import Decimal
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db.models import Max
from datetime import timedelta
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import modelformset_factory
from django.http import HttpResponseBadRequest
from django.db import transaction 
from datetime import datetime
import os


def home(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'home.html', context) 