from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.utils import timezone

def expense_list(request):
    expenses = Expense.objects.order_by('-date')
    return render(request, 'tracker_app/expense_list.html', {'expenses': expenses})

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker_app:expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'tracker_app/expense_form.html', {'form': form, 'title': 'Add Expense'})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('tracker_app:expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker_app/expense_form.html', {'form': form, 'title': 'Edit Expense'})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('tracker_app:expense_list')
    return render(request, 'tracker_app/expense_confirm_delete.html', {'expense': expense})

def monthly_summary(request):
    today = timezone.localdate()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    expenses = Expense.objects.filter()
    total = expenses.aggregate(total=Sum('amount'))['total'] or 0
    by_category = expenses.values('category__name').annotate(sum=Sum('amount')).order_by('-sum')

    return render(request, 'tracker_app/monthly_summary.html', {
        'expenses': expenses,
        'total': total,
        'by_category': by_category,
        'year': year,
        'month': month,
    })