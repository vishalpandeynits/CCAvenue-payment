from django.shortcuts import HttpResponse, render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .utils import *


def checkout(request):
    p_merchant_id = settings.CC_MERCHANT_ID

    # current site domain
    current_site = settings.CURRENT_SITE_DOMAIN

    p_order_id = '0001'
    p_currency = settings.CC_CURRENCY
    p_amount = '100'

    p_redirect_url = str(current_site) + '/payment_success/'
    p_cancel_url = str(current_site) + '/payment_cancel/'

    p_language = settings.CC_LANG

    p_billing_name = 'Foo Bar'
    p_billing_address = '12/Foo Bar'
    p_billing_city = 'Tinsukia'
    p_billing_state = 'Assam'
    p_billing_zip = '786125'
    p_billing_country = settings.CC_BILL_CONTRY
    p_billing_tel = '9957767675'
    p_billing_email = 'vishal.pandey@chat360.io'

    p_delivery_name = ''
    p_delivery_address = ''
    p_delivery_city = ''
    p_delivery_state = ''
    p_delivery_zip = ''
    p_delivery_country = 'India'
    p_delivery_tel = ''

    p_merchant_param1 = ''
    p_merchant_param2 = ''
    p_merchant_param3 = ''
    p_merchant_param4 = ''
    p_merchant_param5 = ''
    p_promo_code = ''

    p_customer_identifier = ''
    merchant_data = 'merchant_id=' + p_merchant_id + '&' + 'order_id=' + p_order_id + '&' + "currency=" + p_currency + \
                    '&' + 'amount=' + p_amount + '&' + 'redirect_url=' + p_redirect_url + '&' + 'cancel_url=' + p_cancel_url + \
                    '&' + 'language=' + p_language + '&' + 'billing_name=' + p_billing_name + '&' + 'billing_address=' + p_billing_address + \
                    '&' + 'billing_city=' + p_billing_city + '&' + 'billing_state=' + p_billing_state + '&' + 'billing_zip=' + p_billing_zip + \
                    '&' + 'billing_country=' + p_billing_country + '&' + 'billing_tel=' + p_billing_tel + '&' + 'billing_email=' + p_billing_email + \
                    '&' + 'delivery_name=' + p_delivery_name + '&' + 'delivery_address=' + p_delivery_address + '&' + 'delivery_city=' + p_delivery_city + \
                    '&' + 'delivery_state=' + p_delivery_state +  '&' + 'delivery_zip=' + p_delivery_zip + '&' + 'delivery_country=' + p_delivery_country + \
                    '&' + 'delivery_tel=' + p_delivery_tel + '&' + 'merchant_param1=' + p_merchant_param1 + '&' + 'merchant_param2=' + p_merchant_param2 + \
                    '&' + 'merchant_param3=' + p_merchant_param3 + '&' + 'merchant_param4=' + p_merchant_param4 + '&' + 'merchant_param5=' + p_merchant_param5 + \
                    '&' + 'promo_code=' + p_promo_code + '&' + 'customer_identifier=' + p_customer_identifier + '&'

    encryption = encrypt(merchant_data, settings.CC_WORKING_KEY)
    
    params = {
        'p_redirect_url': p_redirect_url,
        'encryption': encryption, 'access_code': settings.CC_ACCESS_CODE,
        'cc_url': settings.CC_URL, 'p_amount': p_amount
    }

    return render(request, 'payment.html', params)


@csrf_exempt
def payment_success(request):

    """
    Method to handel cc-ave payment success.
    :param request:
    :return:
    """

    response_data = request.POST

    response_chiper = response_data.get('encResp')
    payment_list = decrypt(response_chiper, settings.CC_WORKING_KEY)

    # payment success code

    return HttpResponse('DONE')


@csrf_exempt
def payment_cancel(request):

    """
    Method to handel cc-ave.
    :param request: data
    :return: status
    """

    response_data = request.POST

    response_chiper = response_data.get('encResp')
    payment_list = decrypt(response_chiper, settings.CC_WORKING_KEY)
    print(payment_list)
    # payment cancel code

    return HttpResponse('Cancel')
