# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ExpenseForm

from django.shortcuts import render, redirect
from .models import Expense

def expense(request):
    all_expens = Expense.objects.all()
    return render(request, 'cost/expense.html', {'expenses':all_expens})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('expenses')
    else:
        form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form':form})