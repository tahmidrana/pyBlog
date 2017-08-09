# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ExpenseForm

from django.shortcuts import render
from .models import Expense

def expense(request):
    all_expens = Expense.objects.all()
    return render(request, 'cost/expense.html', {'expenses':all_expens})

def add(request):
    form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form':form})

def add_expense(request):
    print("Add expense")
