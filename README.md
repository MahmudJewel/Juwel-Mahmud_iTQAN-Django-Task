## Live Server
[Click here](https://groceryy.herokuapp.com) to se the live website.
## Licence
This web app is developed by : [Jewel Mahmud](https://mahmudjewel.herokuapp.com/
) under licence of [tech villain](https://www.youtube.com/channel/UCJCdq7lWqB7M5b16UatoTEw) youtube channel.

Start date of developing: Jan-2022

This project is a part of candidate selection procedure. The HR team of a reputed company from Bangladesh give this task to solve within 72 hours with two more project on cryptocurency & data scrapping.

##The django task question is given below.
You are required to build an ecommerce grocery website using Django. The following elements must be present:
1. **Login System**: Login system where users can create accounts and login with their credentials. Create an HTML form where users can input their username and password. If the credentials are correct, they will be permitted to visit the pages. Login page should be shown like a popup.
Password Requirements:
* Should be at least 8 digit long
* Must have at least one Uppercase, Lowercase and Special character
* First digit cannot be number
* Make a system that can validate the password. If anything is missing on the password, your checker should give a specific message to the user about what is missing
2. **Categories**: After logging, the main page should show 5 categories (i.e. “Vegetable”, “Fruit”, “Beverage”, “Baby”, “Bread & Bakery” etc.) with images in each of the titles
3. **Products**: Each of the categories should contain at least 10 products with images. Clicking on any product should take to the particular product page where product will be shown with image and description.
4. **Slider**: A slider should always be visible in all of the pages. This slider should contain all the 5 categories. The idea is that users will be able to easily navigate throughout the website using this slider
5. **Admin Dashboard**: Now create an admin dashboard that will only be accessed by
admins. This dashboard should show all the products and their respective view counts. Like how many times a product was views. Make sure to sort the list according to the descending order of view counts and use all the products that are part of your website.
DO NOT create any cart or payment system or anything else!


 
## Tools
### Back-end
1. Django ==> 4.0.1

### Front-end
1. Bootstrap ==> 5.1.3
2. Fontawesome ==> 5.15.4
3. HTML-5
4. CSS-3

## Home page
No one can access without login. A regitration page will open as home page.The password validation is custom. I did it with custom password validators.
After login user can see the products. 
## Slider
This part can be done using JavaScript. But I used dropdown menu bar. For passing data in each page, I used context_processor.

!![Creating account page](https://github.com/MahmudJewel/Grocery_shop_screenshot/blob/main/1-signup-page.png)

## Category page
![Category page](https://github.com/MahmudJewel/Grocery_shop_screenshot/blob/main/2-grocery.jpg)

## Product List
After clicking any category, product will be shown categorywise.  
![Product List](https://github.com/MahmudJewel/Grocery_shop_screenshot/blob/main/3-product%20view.png)

## Product view-single
![Product view-single](https://github.com/MahmudJewel/Grocery_shop_screenshot/blob/main/4-single%20product%20view.png)

## Admin view
Only Admin can see all products with total views. 
![Admin view](https://github.com/MahmudJewel/Grocery_shop_screenshot/blob/main/6-admin.png)

The End


