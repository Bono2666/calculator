from django.shortcuts import render


def calculator(request):
    return render(request, 'calculator.html')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculation(request):
    x = int(request.GET.get('x'))
    y = int(request.GET.get('y'))
    operation = str(request.GET.get('operator'))

    if operation == 'add':
        result = add(x, y)
    elif operation == 'sub':
        result = subtract(x, y)
    elif operation == 'mul':
        result = multiply(x, y)
    elif operation == 'div':
        result = divide(x, y)

    context = {
        'result': result
    }
    return render(request, 'calculator.html', context)
