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
    - [Appointment Booking System](#appointment-booking-system)
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
![Pizza](<Planning Files/pizza.png>)
![Tomatoes](<Planning Files/tomatoes.jpg>)

|Tag|Colour|Item(s)|Hex Code|
|---|---|---|---|
|**Primary Color:**|Red|Tomato, Pepper|#f20929|
|**Secondary Color:**|Green|Basil, Pepper|#798539|
|**Accent Color:**|Yellow|Cheddar, Motzeralla|#d2913f|
|**Background:**|Brown|Mushrooms|#ad8875|
|**Font Color:**|Black|Olives|#01000|

#### Accessibility check for colour scheme

Colour Blind Safe and contrast was checked by [Adobe Color](<https://color.adobe.com/create/color-accessibility>)

![Contrast Check](<Planning Files/ContrastCheck.jpg>)

#### Contrast checker

To check the text contrast I used [Adobe Color](<https://color.adobe.com/create/color-accessibility>)

![Contrast Red Black](<Planning Files/Contrast-Red-Black.jpg>)
![Contrast Green Black](<Planning Files/Contrast-Green-Black.jpg>)
![Contrast Yellow Black](<Planning Files/Contrast-Yellow-Black.jpg>)
![Contrast Brown Black](<Planning Files/Contrast-Brown-Black.jpg>)

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
I used an agile approach to project management. The HealMate development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

### MoSCoW Prioritization
- **Must-Haves:** 
    - User registration and login 
    - Order booking 
    - Reviews
    - Role-based dashboards
- **Should-Haves:** 
    - Filtering options
- **Could-Haves:** 
    - Profile pictures for users and staff
    - Messaging system
    - Notifications
    - Personal profile with pre-planned filters (alergies, distastes)
    - Changing / Removing toppings
    - Changing crusts
    - Order history
    - Saved orders
    - Reset password (requires email or SMS integration)
    - Add photo onto review
- **Won’t-Haves:** 
    - Payment integration
    - Multiple locations per day.

### Sprints
- **Sprint 1:** Initial Setup - Project, repository, environment setup.
- **Sprint 2:** User Authentication & Role-Based Dashboards.
- **Sprint 3:** Specialist Search & Appointment Booking System.
- **Sprint 4:** Static Pages & UI/UX Improvements.
- **Sprint 5:** Deployment & Testing.

## User Stories
### Ordering Pizza

- As a customer, I want to see `special pizzas`, so I can try something new.
- As a customer, I want to order `multiple pizzas` at once, so I can buy food for my family or group.
- As a customer, I want to see an `estimated pickup time`, so I know when my pizza will be ready.
- As a customer, I want to schedule an order in advance, so I can pick it up at my `preferred time`.
- As a customer, I want to receive an `order confirmation`, so I know my order was successfully placed.

### Finding the Pizza Truck

- As a customer, I want to view the `live location` of the pizza truck, so I can find it easily.
- As a customer, I want to see the `truck’s schedule`, so I know when and where I can pick up my order.

### Reviews & Feedback

- As a customer, I want to see `other customer reviews`, so I can decide which pizza to try next.
- As a customer, I want to `leave a review` after my order, so I can share my experience.

## Admin (Business Owner) User Stories
### Order Management

- As an admin, I want to `view and manage incoming orders`, so I can prepare them efficiently.
- As an admin, I want to update `order status`, so customers know when their pizza is ready.

### Menu Management

- As an admin, I want to `feature special pizzas`, so customers can see what’s new.

### Truck Location & Schedule

- As an admin, I want to `update the truck’s live location`, so customers can find us easily.
- As an admin, I want to `set weekly schedules`, so customers can plan their visits.

### Customer Engagement

- As an admin, I want to `view & approve customer reviews`, so I can improve my service.

## Guest User Stories (Users Without an Account)

- As a guest, I want to `browse the pizzas`, so I can see what pizzas are available.
- As a guest, I want to `view the truck’s location`, so I can find out where to get a pizza.
- As a guest, I want to `sign up` easily, so I can place an order without hassle.

## Scope Plane

The PizzaMe platform will include the following MVP functionalities:
- User registration and role-based dashboards.
- Search and filtering system

## Structural Plane
The site is structured around an easy-to-use interface. The primary menu includes links to bookings and user profile management.

## Skeleton & Surface Planes

### Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:

<details open>
    <summary>Wireframe - Main Page (Index Page) - Over Multiple Devices</summary>  
    <img src="Planning Files/Wireframes-Multi-Device.jpg"> 
</details>
<details>
    <summary>Wireframe - Find Pizza Page</summary>  
    <img src="Planning Files/wireframe-find-pizza-page.jpg"> 
</details>
<details>
    <summary>Wireframe - Order Pizza Page - Logged In</summary>  
    <img src="Planning Files/Wireframe-Order-Pizza-LoggedIn.jpg"> 
</details>
<details>
    <summary>Wireframe - Order Pizza Page - Logged Out</summary>  
    <img src="Planning Files/Wireframe-Order-Pizza-LoggedOut.jpg"> 
</details>
<details>
    <summary>Wireframe - Reviews Page</summary>  
    <img src="Planning Files/Wireframe-Reviews-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Specials Page</summary>  
    <img src="Planning Files/Wireframe-Specials-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Register Page</summary>  
    <img src="Planning Files/Wireframe-Register-Page.jpg"> 
</details>
<details>
    <summary>Wireframe - Login / Logout Page</summary>  
    <img src="Planning Files/Wireframe-LoginLogout.jpg"> 
</details>
<br />
Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices.

## Database Schema - Entity Relationship Diagram

- User (Customers & Admins)

> - ID (PK) (Integer)
> - Name (varchar(100))
> - Email (varachar(100))
> - Password (varchar(20))
> - Phone (Integer)
> - Role (Customer/Admin) (varchar(10))

- Order

> - ID (PK) (Integer)
> - User_ID (FK → User) (Integer)
> - Order_date (timestamp)
> - Status (varchar(9)) - Example (Pending, Preparing, Delivered, Cancelled)
> - Total_price (Float)
> - Forward_order (boolean)
> - Forward_order_time (timestamp)

- Pizza

> - ID (PK)(Integer)
> - Name (varchar(100))
> - Size (varchar(6)) - Example (Small, Medium, Large)
> - Price (Float)
> - Description (varchar(100))

OrderItem (Many-to-Many between Order & Pizza)

> - ID (PK) (Integer)
> - Order_ID (FK → Order) (Integer)
> - Pizza_ID (FK → Pizza) (Integer)
> - Quantity (Integer)

- Payment

> - ID (PK) (Integer)
> - Order_ID (FK → Order) (Integer)
> - Payment_method (varchar(12)) - Example (Credit Card, PayPal, Cash)
> - Payment_status (varchar(8)) - Example (Paid, Pending, Failed)
> - Transaction_ID (Integer)

![Initial ERD](<Planning Files/Initial-ERD.jpg>)

The above ERD was generated using 

`python manage.py inspectdb > show_database.txt to check fields on user table.`

`Check authentication: I Think Therefore I Blog > Authentication > Django AllAuth`

~~~
Table userAllauth {
ID Integer [primary key]
Name varchar(100)
Email varachar(100)
Password varchar(20)
Phone Integer
Role varchar(10)
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
Transaction_ID Integer
}

Ref: userAllauth.ID < order.User_ID
Ref: orderItem.Order_ID > order.ID
Ref: orderItem.Pizza_ID > pizza.ID
Ref: payment.Order_ID - order.ID
~~~


