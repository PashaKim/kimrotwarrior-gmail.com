import re
import string
from random import randint
from datetime import datetime, timedelta

from django.db.models import Sum
from django.shortcuts import render
from .models import Book, Author


def main(request):
    return render(request, 'main.html', {})


def first_warm_up(request):
    context = dict()
    l_first = list(range(1, 10+1))
    l_second = list(string.ascii_lowercase[:10])
    l_third = list(range(5, 15+1))
    context['1_1'] = {'l_first': l_first, 'l_second': l_second, 'l_third': l_third}

    l_first_r = list()
    for n in l_first:
        if n % 2 == 0:
            l_first_r.append(n)
    l_first_r.reverse()
    context['1_2'] = {'l_first_r': l_first_r}

    l_combine = l_first + l_second + l_third
    context['1_3'] = {'l_combine': list(set(l_combine))}

    l_comb_int = l_first + l_third
    l_comb_int_diff = [l_comb_int[i] for i in range(len(l_comb_int)) if i != l_comb_int.index(l_comb_int[i])]
    context['1_4'] = {'l_combine_int_unique': list(set(l_comb_int)), 'l_combine_int_difference': l_comb_int_diff}

    l_second_str = ''.join(l_second)
    context['1_5'] = {'l_first_sum': sum(l_first), 'l_second_str': l_second_str, 'l_third_sum': sum(l_third)}

    context['1_6'] = {'index_d':  l_second_str.find('d')}

    l_second_str_2 = l_second_str[:]
    context['1_7'] = {'l_second_str_2': l_second_str_2.replace('d', 'a')}

    new_dict = {'letters': l_second, 'numbers': [randint(100, 200) for i in range(0, 10)]}
    context['1_8'] = {'new_dict': new_dict}

    key_list = list()
    value_list = list()
    for key, value in new_dict.items():
        if key not in key_list:
            key_list.append(key)
        value_list.append(value)

    context['1_9'] = {'keys': key_list}
    context['1_10'] = {'values': value_list}
    context['1_11'] = {'l_dict': [{key: new_dict[key]} for key in new_dict]}

    context['1_12'] = {'now': datetime.now(), 'yesterday': datetime.now() - timedelta(days=1)}

    return render(request, 'tasks/warm_up.html', context=context)


def second_regular_expressions(request):
    context = dict()
    ip_samples = ['\t\nSome text 127.0.0.1 GET ....\n4 127.0.0.2 8888 GET ....\n',
                  'google.com has address 216.58.209.174\r\ngoogle.com mail is handled by 20 alt1.aspmx.l.google.com.',
                  ]
    context['ip_list'] = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', r' '.join(ip_samples))
    url_samples = ['http://api.facebook.com/user/56', 'http://api.FaceBook.Com',
                   'https://facebook.com', 'https://sub.sub.sub.example.com:8000/user/photo/56/',
                   ]
    context['url_list'] = re.findall(r'https?://([a-zA-Z\.]+)', r' '.join(url_samples))
    context['url_replace'] = (re.sub(r'//([a-zA-Z\.]+)', '//example.org', r' '.join(url_samples))).split(' ')
    return render(request, 'tasks/regular_expressions.html', context)


def fourth_orm_task(request):
    context = dict()
    context['books'] = Book.objects.prefetch_related('author').all()
    context['authors'] = Author.objects.all()
    authors_values = Author.objects.annotate(pages_sum=Sum('books_set__pages_count')).values('name', 'pages_sum')
    context['task'] = [{d['name']:d['pages_sum']} for d in authors_values]
    return render(request, 'tasks/orm_task.html', context=context)
