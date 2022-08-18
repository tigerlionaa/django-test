# Django Practical Test

## Tools Used

<b>Language Choice:</b> Python <br>
<b>Frameworks:</b> Django, Django REST Framework <br>
<b>Database:</b> SQLite <br>
<b>Library:</b>  Django-Phonenumber-Field <br>

# Project Overview

* A RESTful API using Django REST Framework to track customers, their details, subscribed plan.
* This App has multiple endpoints of `GET`, `POST`, `PUT`, `DELETE` http methods.
* This Cutomers app has 2 layers of hierarchical user 
                                    1. <b>Superuser/Admin</b>
                                    2. <b>Customer/Subscriber under those superuser/admin</b>
* A customer is recognized by his/her unique `primary_phone_number`, third party library has been utilized to validate the customer number.
* Customer can't update or change the `primary_phone_number` once it's assigned to that customer.
* With a unique `primary_phone_number` a customer can only subscribe to a plan at a time, customer can update the plan but can't hold membership of multiple paln.
* If a customer subscribe to a paid plan (bronze, silver, gold), in that case customer will own the number.
* If a customer subsribe to no paid plan, in that case the subscribed company will own the number.

## API Endpoints
* `users` can handle `GET` request, we can view all the `superusers` and `customers` under them.
* `users/id/` can handle `GET` request, we can view individual `superuser` and `customers` under the `superuser`.
* `subscriptioninfo` can handle `GET`, and `POST` request methods. By `GET` request we can view all the `customers` and their `info` under a logged `superuser`. By 'POST` request a new `customer` with his/her related `info` will be created.
* `subscriptioninfo/id/` can handle <b>GET</b>, <b>PUT</b> and <b>DELETE</b> request methods.

* Anyone can Search in this site by putting anything related to post.

* Viewers can comment on any post by providing their name and email.

* Related posts will show up while inside of a post which will be filtered by topic name.

* Quick Walkthrough - https://www.youtube.com/watch?v=5sywVg_tyQU

* Deployed Link - https://featured-blog.herokuapp.com/
