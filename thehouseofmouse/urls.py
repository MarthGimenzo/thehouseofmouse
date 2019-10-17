"""thehouseofmouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, faqs_view, about_view
from products.views import listing_view, results_view
from cart.views import cart_view, checkout_info_view, checkout_shipping_view, checkout_payment_view, checkout_confirm_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # standard pages
    path('', home_view, name="home"),
    path('faqs/', faqs_view, name="faqs"),
    path('about/', about_view, name="about"),

    # listings and search
    path('listing/', listing_view, name="listing"),
    path('results/', results_view, name="results"),

    # cart and payment
    path('cart/', cart_view, name="cart"),
    path('checkout/info', checkout_info_view, name="info"),
    path('checkout/shipping', checkout_shipping_view, name="shipping"),
    path('checkout/payment', checkout_payment_view, name="payment"),
    path('checkout/confirm', checkout_confirm_view, name="confirm"),

]
