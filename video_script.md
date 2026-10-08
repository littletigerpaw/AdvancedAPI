# 5-Minute Presentation Script

## Intro (15-20 seconds)
Hi everyone, my name is [Your Name], and this is my Mechanic Shop API project. The project is a Flask backend that helps a repair shop manage customers, service tickets, mechanics, and inventory.

## What the project does (30-40 seconds)
The goal of this project is to make it easier for a mechanic shop to track repair jobs and the parts used. Customers can create accounts, log in, and view their own service tickets. Mechanics can be assigned to tickets, and inventory items can be tracked for each repair job.

## How it works (1 minute)
The app uses Flask and SQLAlchemy to create the database models. Customer accounts have login functionality with JWT tokens, so protected routes require a valid Bearer token. The API also includes rate limiting and caching to improve performance and protect endpoints. Mechanics can be assigned to service tickets, and the app can sort them by how many jobs they have worked on. Inventory items are stored separately and linked to service tickets through a many-to-many relationship.

## Demo (2-3 minutes)
Now I’ll show the project running.

First, I’ll create a customer.
Then I’ll log in to receive a token.
Then I’ll use that token to access my tickets.
Then I’ll create a service ticket for a vehicle issue.
Then I’ll create an inventory item like an oil filter.
Then I’ll assign a mechanic to the ticket and show the response from the server.

I’ll also show the mechanics leaderboard and inventory endpoints to demonstrate the project in action.

## Closing (20-30 seconds)
This project shows how a backend API can manage real business operations in a mechanic shop, including security, performance, and data relationships. It’s a practical API project that connects customer data, repair records, mechanic assignments, and inventory management in one system.

Thank you.
