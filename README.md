# PizzaVan
#### Image of site here

Live site: <a href="heroku" target="_blank">PizzaMe</a>.
For **Admin access** with relevant sign-in information, click <a href="herokuapp" target="_blank">here</a>.
Github repository, click <a href="https://github.com/MathewIsherwood/PizzaVan" target="_blank">here</a>.

## Table of Contents
1. [Introduction](#introduction)
2. [Overview](#overview)
3. [UX - User Experience](#ux---user-experience)
    - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
4. [Project Planning](#project-planning)
    - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
    - [User Stories](#user-stories)
5. [Scope Plane](#scope-plane)
6. [Structural Plane](#structural-plane)
7. [Skeleton & Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
8. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
9. [Security](#security)
10. [Features](#features)
    - [User View - Registered/Unregistered](#user-view---registeredunregistered)
    - [Role-Based Dashboard Features](#role-based-dashboard-features)
    - [Role-Based Navigation](#role-based-navigation)
    - [Soft Delete/Archiving for Patient Accounts](#soft-deletearchiving-for-patient-accounts)
    - [Order System](#order-system)
    - [Messaging System](#messaging-system)
    - [Profile Management](#profile-management)
    - [Confirmation Messages](#confirmation-messages)
    - [CRUD Functionality](#crud-functionality)
    - [Feature Showcase](#feature-showcase)
11. [Future Features](#future-features)
12. [Technologies & Languages Used](#technologies--languages-used)
13. [Libraries & Frameworks](#libraries--frameworks)
14. [Tools & Programs](#tools--programs)
15. [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
16. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [PostgreSQL](#postgresql)
    - [Heroku deployment](#heroku-deployment)
    - [Clone project](#clone-project)
    - [Fork Project](#fork-project)
17. [Privacy Policy](#privacy-policy)
18. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
19. [Acknowledgements](#acknowledgements)

## Overview
PizzaMe is an online platform that allows users to:
- Register and create a profile
- Search for pizza van locations
- Review the pizza orders
- Pre-register interest in orders for a specific day / location

The platform ensures accessibility across all devices and browsers, and its goal is to streamline the process of buying a pizza. In future iterations, PizzaMe will be updated to have more location options, online pre-ordering and talk to the van via messaging.

## UX - User Experience
### Design Inspiration
My inspiration for PizzaMe came from the colours of Pizza, why change what is already a great formula! 

For the business inspiration, there is a pizza van that visits my area but only on a Tuesday. Unless I ask them, I have no idea where in town they are the rest of the week. What if I need a pizza, like medically NEED a pizza on a Friday?! A website is required!

### Colour Scheme
![Pizza](<planning_files/pizza.png>)
![Tomatoes](<planning_files/tomatoes.jpg>)

|Tag|Colour|Item(s)|Hex Code|
|---|---|---|---|
|**Primary Color:**|Red|Tomato, Pepper|#f20929|
|**Secondary Color:**|Green|Basil, Pepper|#798539|
|**Accent Color:**|Yellow|Cheddar, Motzeralla|#d2913f|
|**Background:**|Brown|Mushrooms|#ad8875|
|**Font Color:**|Black|Olives|#01000|

#### Accessibility check for colour scheme

Colour Blind Safe and contrast was checked by [Adobe Color](<https://color.adobe.com/create/color-accessibility>)

![Contrast Check](<planning_files/ContrastCheck.jpg>)

#### Contrast checker

To check the text contrast I used [Adobe Color](<https://color.adobe.com/create/color-accessibility>)

![Contrast Red Black](<planning_files/Contrast-Red-Black.jpg>)
![Contrast Green Black](<planning_files/Contrast-Green-Black.jpg>)
![Contrast Yellow Black](<planning_files/Contrast-Yellow-Black.jpg>)
![Contrast Brown Black](<planning_files/Contrast-Brown-Black.jpg>)

### Font

Using [Google Font](<https://fonts.google.com/>), I imported "Montserrat" and "Bricolage Grotesque" to my CSS file. I set "Montserrat" as my default font. 
I used "Bricolage Grotesque" as a font for content on my menu page and for authorisation pages.
Aditionally I used "Bodoni Moda" and "Bodoni Moda SC" as highlight fonts.

## Project Planning

### Strategy Plane
The primary objective of PizzaMe is to bridge the gap between people who want pizza and small pizza makers. By offering an intuitive interface, users can easily search for their ideal pizza and pre-order without hassle.

### Site Goals
- Provide customers with a user-friendly platform to book pizzas with PizzaMe.
- Allow PizzaMe to manage their pre-orders and reviews.
- Offer an intuitive interface with role-based dashboards for workers and customers.

### Agile Methodologies - Project Management
I used an agile approach to project management. The PizzaMe development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

### MoSCoW Prioritization
### Must-Haves

1. **User Registration and Login**

    **Acceptance Criteria:**
    - Users can register with a username, email, and password.
    - Users can log in with their credentials.
    - Users receive a confirmation email upon registration.

    **Tasks:**
    - Set up Django AllAuth for user authentication.
    - Create registration and login forms.
    - Implement on screen confirmation for new users.
    - Design responsive registration and login pages.

2. **Notifications**

    **Acceptance Criteria:**
    - Users receive notifications for order status updates.

    **Tasks:**
    - Implement a notification system using Django signals.
    - Create a notifications model.
    - Design a notifications section in the user dashboard.
    - Ensure notifications are displayed responsively.

3. **Create Order**

    **Acceptance Criteria:**
    - Users can create a new order by selecting pizzas and specifying details.
    - Users receive a confirmation message upon successful order creation.

    **Tasks:**
    - Create an order model and form.
    - Implement order creation logic.
    - Design a responsive order creation page.
    - Display a confirmation message upon order creation.

4. **Edit Order**

    **Acceptance Criteria:**
    - Users can edit their existing order.
    - Changes are saved and reflected in the user's order history.

    **Tasks:**
    - Implement order edit functionality.
    - Create a form for editing order.
    - Design a responsive order edit page.
    - Ensure changes are saved and displayed correctly.

5. **View Order**

    **Acceptance Criteria:**
    - Users can view their current and past order.
    - Order details are displayed clearly and responsively.

    **Tasks:**
    - Create a view for displaying user order.
    - Design a responsive order history page.
    - Ensure order details are displayed correctly.

6. **Delete Order**

    **Acceptance Criteria:**
    - Users can delete their existing order.
    - Deleted order are removed from the user's order history.

    **Tasks:**
    - Implement order deletion functionality.
    - Add a delete button to the order history page.
    - Ensure order are removed from the database upon deletion.

### Should-Haves

7. **Reviews**

    **Acceptance Criteria:**
    - Users can leave reviews for their orders.
    - Reviews are displayed on the order details page.

    **Tasks:**
    - Create a review model and form.
    - Implement review submission logic.
    - Design a responsive review section on the order details page.

8. **Edit Reviews**

    **Acceptance Criteria:**
    - Users can edit their existing reviews.
    - Changes are saved and reflected in the review section.

    **Tasks:**
    - Implement review edit functionality.
    - Create a form for editing reviews.
    - Design a responsive review edit page.
    - Ensure changes are saved and displayed correctly.

9. **Filtering Options**

    **Acceptance Criteria:**
    - Users can filter orders and reviews based on various criteria.
    - Filtered results are displayed clearly and responsively.

    **Tasks:**
    - Implement filtering logic for orders and reviews.
    - Create a filtering form.
    - Design a responsive filtering interface.
    - Ensure filtered results are displayed correctly.

10. **Owner - Review Dashboard**

    **Acceptance Criteria:**
    - Owners can view and manage customer reviews.
    - Reviews are displayed in a dashboard format.

    **Tasks:**
    - Create a review dashboard for owners.
    - Implement review management functionality.
    - Design a responsive review dashboard.
    - Ensure reviews are displayed and managed correctly.

11. **Owner - Orders Dashboard**

    **Acceptance Criteria:**
    - Owners can view and manage incoming orders.
    - Orders are displayed in a dashboard format.

    **Tasks:**
    - Create an orders dashboard for owners.
    - Implement order management functionality.
    - Design a responsive orders dashboard.
    - Ensure orders are displayed and managed correctly.

### Could-Haves

12. **Profile Pictures for Users and Staff**

    **Acceptance Criteria:**
    - Users and staff can upload profile pictures.
    - Profile pictures are displayed on their profiles.

    **Tasks:**
    - Implement profile picture upload functionality.
    - Create a form for uploading profile pictures.
    - Design a responsive profile picture section.
    - Ensure profile pictures are displayed correctly.

13. **Messaging System**

    **Acceptance Criteria:**
    - Users can send and receive messages within the platform.
    - Messages are displayed in a messaging interface.

    **Tasks:**
    - Implement a messaging system.
    - Create a messaging model and form.
    - Design a responsive messaging interface.
    - Ensure messages are sent and received correctly.

14. **Personal Profile with Pre-Planned Filters (Allergies, Distastes)**

    **Acceptance Criteria:**
    - Users can set preferences for allergies and distastes.
    - Preferences are used to filter available pizzas.

    **Tasks:**
    - Implement preference setting functionality.
    - Create a form for setting preferences.
    - Design a responsive preferences section.
    - Ensure preferences are used to filter pizzas correctly.

15. **Changing / Removing Toppings**

    **Acceptance Criteria:**
    - Users can customize their pizzas by changing or removing toppings.
    - Customizations are reflected in the order details.

    **Tasks:**
    - Implement topping customization functionality.
    - Create a form for customizing toppings.
    - Design a responsive customization interface.
    - Ensure customizations are saved and displayed correctly.

16. **Changing Crusts**

    **Acceptance Criteria:**
    - Users can customize their pizzas by changing the crust.
    - Customizations are reflected in the order details.

    **Tasks:**
    - Implement crust customization functionality.
    - Create a form for customizing crusts.
    - Design a responsive customization interface.
    - Ensure customizations are saved and displayed correctly.

17. **Order History**

    **Acceptance Criteria:**
    - Users can view their past orders.
    - Order history is displayed clearly and responsively.

    **Tasks:**
    - Create a view for displaying order history.
    - Design a responsive order history page.
    - Ensure past orders are displayed correctly.

18. **Saved Orders**

    **Acceptance Criteria:**
    - Users can save their favorite orders for quick reordering.
    - Saved orders are displayed in a saved orders section.

    **Tasks:**
    - Implement saved orders functionality.
    - Create a form for saving orders.
    - Design a responsive saved orders section.
    - Ensure saved orders are displayed and managed correctly.

19. **Reset Password (Requires Email or SMS Integration)**

    **Acceptance Criteria:**
    - Users can reset their password using email or SMS.
    - Password reset instructions are sent to the user's email or phone.

    **Tasks:**
    - Implement password reset functionality.
    - Integrate email or SMS for password reset.
    - Design a responsive password reset page.
    - Ensure password reset instructions are sent correctly.

20. **Add Photo onto Review**

    **Acceptance Criteria:**
    - Users can add photos to their reviews.
    - Photos are displayed alongside the review.

    **Tasks:**
    - Implement photo upload functionality for reviews.
    - Create a form for adding photos to reviews.
    - Design a responsive photo section in the review.
    - Ensure photos are displayed correctly with the review.

### Sprints
- **Sprint 1:** Initial Setup - Project, repository, environment setup.
- **Sprint 2:** User Authentication & Role-Based Dashboards.
- **Sprint 3:** Specialist Search & Item Order System.
- **Sprint 4:** Static Pages & UI/UX Improvements.
- **Sprint 5:** Deployment & Testing.

## User Stories
### Guest User Stories (Users Without an Account)

- As a guest, I want to `browse the pizzas`, so I can see what pizzas are available.
- As a guest, I want to `sign up` easily, so I can place an order without hassle.

### Customer User Stories (Users logged in)

- As a customer, I want to order `multiple pizzas` at once, so I can buy food for my family or group.
- As a customer, I want to receive an `order confirmation`, so I know my order was successfully placed.
- As a customer, I want to `order a single pizza`, just for me.
- As a customer, I want to be able to `edit my order`, got to be able to change my mind!
- As a customer, I want to be able to `delete my order`, changed my mind!

## Admin (Business Owner) User Stories
- As an admin, I want to `view and manage incoming orders`, so I can prepare them efficiently.
- As an admin, I want to update `order status` so customers know when their pizza is ready.

## Flow Diagram
![User Flow Diagram](planning_files/UserFlowDiagram.jpg)

## Scope Plane

The PizzaMe platform will include the following MVP functionalities:
- User registration and role-based dashboards.
- Search and filtering system

## Structural Plane
The site is structured around an easy-to-use interface. The primary menu includes links to orders and user profile management.

## Skeleton & Surface Planes

### Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:

<details open>
    <summary>Wireframe - Main Page (Index Page) - Over Multiple Devices</summary>  
    <img src="planning_files/Wireframes-Multi-Device.jpg"> 
</details>
<details>
    <summary>Wireframe - Find Pizza Page</summary>  
    <img src="planning_files/wireframe-find-pizza-page.jpg"> 
</details>
<details>
    <summary>Wireframe - Order Pizza Page - Logged In</summary>  
    <img src="planning_files/Wireframe-Order-Pizza-LoggedIn.jpg"> 
</details>
<details>
    <summary>Wireframe - Order Pizza Page - Logged Out</summary>  
    <img src="planning_files/Wireframe-Order-Pizza-LoggedOut.jpg"> 
</details>
<details>
    <summary>Wireframe - Reviews Page</summary>  
    <img src="planning_files/Wireframe-Reviews-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Specials Page</summary>  
    <img src="planning_files/Wireframe-Specials-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Register Page</summary>  
    <img src="planning_files/Wireframe-Register-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Login / Logout Page</summary>  
    <img src="planning_files/Wireframe-LoginLogout.jpg"> 
</details>
<br />
Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices. Wireframes include all MoSCoW Prioritization levels.

## database schema - entity relationship diagram

- user (customers & admins)

> - id (autofield): [primary key]
> - username (charfield)
> - first_name (charfield)
> - last_name (charfield)
> - email (emailfield)
> - password (charfield)
> - is_staff (booleanfield)
> - is_active (booleanfield)
> - date_joined (datetimefield)

- order

> - id (pk) (integer)
> - user_id (fk → user) (integer)
> - order_date (timestamp)
> - status (varchar(9)) - example (Pending, Preparing, Delivered, Cancelled)
> - total_price (float)
> - forward_order (boolean)
> - forward_order_time (timestamp)

- pizza

> - id (pk)(integer)
> - name (varchar(100))
> - size (varchar(6)) - example (Small, Medium, Large)
> - price (float)
> - description (varchar(100))
> - featured_image (varchar(100))
> - enabled (boolean)

orderitem (many-to-many between order & pizza)

> - id (pk) (integer)
> - order_id (fk → order) (integer)
> - pizza_id (fk → pizza) (integer)
> - quantity (integer)

- payment

> - id (pk) (integer)
> - order_id (fk → order) (integer)
> - payment_method (varchar(12)) - example (Credit Card, Paypal, Cash)
> - payment_status (varchar(8)) - example (Paid, Pending, Failed)

![Initial ERD](<planning_files/Initial-ERD.jpg>)

The above ERD was generated using https://dbdiagram.io/

`Check authentication: I Think Therefore I Blog > Authentication > Django AllAuth`

~~~
Table userAllauth {
id (AutoField): [primary key]
username (CharField): [note:'Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.']
first_name (CharField): [note:'Optional. 150 characters or fewer.']
last_name (CharField): [note:'Optional. 150 characters or fewer.']
email (EmailField): [note:'Optional. 254 characters or fewer.']
password (CharField): [note:'Required. A hashed representation of the user's password.']
is_staff (BooleanField): [note:'Designates whether the user can log into the admin site.']
is_active (BooleanField): [note:'Designates whether this user should be treated as active.']
date_joined (DateTimeField): [note:'The date and time when the user account was created.']
}

Table order{
ID Integer [primary key]
User_ID Integer [note:'(FK → User)']
Order_date timestamp
Status varchar(9) [note: 'Pending, Preparing, Delivered, Cancelled']
Total_price Float
Forward_order boolean
Forward_order_time timestamp
}

Table pizza {
ID integer [primary key]
Name varchar(100)
Size varchar(6) [note: 'Small, Medium, Large']
Price Float
Description varchar(100)
featured_image varchar(100)
enabled boolean
}

Table orderItem {
ID Integer [primary key]
Order_ID Integer [note:'(FK → Order)']
Pizza_ID Integer [note:'(FK → Pizza)']
Quantity Integer
}

Table payment {
ID Integer [primary key]
Order_ID Integer [note:'(FK → Order)']
Payment_method varchar(12) [note: 'Credit Card, PayPal, Cash']
Payment_status varchar(8) [note: 'Paid, Pending, Failed']
}

Ref: userAllauth.ID < order.User_ID
Ref: orderItem.Order_ID > order.ID
Ref: orderItem.Pizza_ID > pizza.ID
Ref: payment.Order_ID - order.ID
~~~


