### HTML

I have used the [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes | |
| --- | --- | --- | --- |
| Home | ![screenshot](docs/testing/html/home.png) | Pass: No Errors|
| Products | ![screenshot](docs/testing/html/products.png) | Pass: No Errors |
| Product Detail | ![screenshot](docs/testing/html/product_detail.png) | Pass: No Errors|
| Product Edit | ![screenshot](docs/testing/html/product_edit.pngg) | Pass: No Errors |
| Product Add | ![screenshot](docs/testing/html/product_add.png) | Pass: No Errors |
| FAQs | ![screenshot](docs/testing/html/contact.png) | Pass: No Errors|
| Contact | ![screenshot](docs/testing/html/contact.png) | Pass: No Errors |
| Bag | ![screenshot](docs/testing/html/bag.png) | Pass: No Errors |
| Checkout | ![screenshot](docs/testing/html/checkout.png) | Pass: No Errors |
| Checkout Success | ![screenshot](docs/testing/html/checkout_success.png) | Pass: No Errors |

### CSS

I have used the [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate all of my CSS files.

| Page | Screenshot | Notes | |
| --- | --- | --- | --- |
| Home | ![screenshot](docs/testing/css/home_css.png) | Pass: No Errors|
| Products | ![screenshot](docs/testing/css/product_css.png) | Pass: No Errors |
| FAQs | ![screenshot](docs/testing/css/faqs_css.png) | Pass: No Errors|
| Contact | ![screenshot](docs/testing/css/contact_css.png) | Pass: No Errors |
| Bag | ![screenshot](docs/testing/css/bag_css.png) | Pass: No Errors |
| Checkout | ![screenshot](docs/testing/css/checkut_css.png) | Pass: No Errors |

### PYTHON

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File |  | Screenshot |  |
| --- | --- | --- | --- |
| Bag urls.py | ![screenshot](docs/testing/python/bag_urls.png) |
| Bag views.py | ![screenshot](docs/testing/python/bag_views.png) |
| Bag contexts.py | ![screenshot](docs/testing/python/bag_contexts.png) |
| Checkout admin.py | ![screenshot](docs/testing/python/checkout_admin.png) |
| Checkout forms.py | ![screenshot](docs/testing/python/checkout_forms.png) |
| Checkout models.py | ![screenshot](docs/testing/python/checkout_models.png) |
| Checkout urls.py | ![screenshot](docs/testing/python/checkout_urls.png) |
| Checkout views.py | ![screenshot](docs/testing/python/checkout_views.png) |
| Checkout webhook_handler.py | ![screenshot](docs/testing/python/checkout_webhook_handler.png) |
| Checkout webhooks.py | ![screenshot](docs/testing/python/checkout_webhooks.png) |
| FAQs admin.py | ![screenshot](docs/testing/python/faqs_admin.png) |
| FAQs models.py | ![screenshot](docs/testing/python/faqs_models.png) |
| FAQs urls.py | ![screenshot](docs/testing/python/faqs_urls.png) |
| FAQs views.py | ![screenshot](docs/testing/python/faqs_views.png) |
| Home urls.py | ![screenshot](docs/testing/python/home_urls.png) |
| Home views.py | ![screenshot](docs/testing/python/home_views.png) |
| glen_paints settings.py | ![screenshot](docs/testing/python/glen_paints_settings.png) |
| glen_paints urls.py | ![screenshot](docs/testing/python/glen_paints_urls.png) |
| Products admin.py | ![screenshot](docs/testing/python/products_admin.png) |
| Products forms.py | ![screenshot](docs/testing/python/products_forms.png) |
| Products models.py | ![screenshot](docs/testing/python/products_models.png) |
| Products urls.py | ![screenshot](docs/testing/python/products_urls.png) |
| Products views.py | ![screenshot](docs/testing/python/products_views.png) |
| Profiles forms.py | ![screenshot](docs/testing/python/products_forms.png) |
| Profiles models.py | ![screenshot](docs/testing/python/products_models.png) |
| Profiles urls.py | ![screenshot](docs/testing/python/product_urls.png) |
| Profiles views.py | ![screenshot](docs/testing/python/products_views.png) |
| Contact forms.py | ![screenshot](docs/testing/python/contact_forms.png) |
| Contact models.py | ![screenshot](docs/testing/python/contact_model.png) |
| Contact urls.py | ![screenshot](docs/testing/python/contact_urls.png) |
| Contact views.py | ![screenshot](docs/testing/python/contact_views.png) |

### Manual Testing 

| **Page**        | **Testing**                                                      | **Outcome** |
| --------------- | :--------------------------------------------------------------: | ---:|
|NAV              | Title of webpage leads back to home page                         | YES|
|NAV              | Search bar returns users query                                   | YES|
|NAV              | Account button allows users to login or register                 | YES|
|NAV              | Account dropdown options change depending on user context        | YES|
|NAV              | Bag button takes user to their bag                               | YES|
|NAV              | Bag button displays current amount in basket                     | YES|
|NAV              | Home/shop/faqs/contact buttons navigate to correct page          | YES|
|HOME PAGE        | Social media links are functional                                | YES|
|HOME PAGE        |  Browse artwork shop buttons all navigate to correct pae         | YES|
|PRODUCTS         | Filter button adjusts how products are displayed                 | YES|
|PRODUCTS(ADMIN)  | Users can edit or delete items                                   | YES|
|PRODUCTS(DETAIL) | Can adjust quantity of item                                      | YES|
|PRODUCTS(DETAIL) | Can add to bag or navigate back to products page                 | YES|
|FAQS             | Accordion works                                                  | YES|
|BAG              | Users can adjust the quantity of products                        | YES|
|BAG              | Users can navigate to secure checkout                            | YES|
|CHECKOUT         | Users used saved info to autofill detail                         | YES|
|CONTACT          | Submit button activates success toast                            | YES|
|ACCOUNT          | Users receive verification email after signing up                | YES|
|ACCOUNT          | Users can logout using logout button                             | YES|
|ACCOUNT          | Users can see account info and past orders                       | YES|


## Further Testing

This website was tested on:

- Google Chrome, Firefox, Microsoft Edge and Safari.
- Testing has been done to ensure all elements were linking correctly.

## Bugs

Faqs.css not linking up properly to deployed site. 
