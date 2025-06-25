# 🛒 Order Management System – Google OAuth 2.0 & Django Rest Framework Integration

# Conclusion of this project
This assignment demonstrates the seamless integration of Google OAuth 2.0 with Django Rest Framework (DRF), laying the foundation for a scalable and secure Order Management System. The implemented system accomplishes:

OAuth 2.0 Authentication with secure access and refresh token handling using Google's APIs.
RESTful API endpoints for data entry and retrieval, adhering to best practices in API development.

Filtered data access based on parameters like title or user, allowing future extension into role-based or user-specific resource access.

This solution showcases essential backend development skills using Python and Django, aligning with Ywork.ai’s innovative, AI-driven ecosystem that demands integration of multiple services for real-time, data-centric applications.

The developed template offers a robust starting point for more complex integrations such as:

Payment gateway APIs

AI/ML-powered recommendations or analytics

Inventory & logistics management






This project implements a secure and extendable backend system using **Django Rest Framework**, integrated with **Google OAuth 2.0** for authentication. It features API endpoints for adding and retrieving sample order data.

---

## 🚀 Features

- 🔐 Google OAuth 2.0 Login Flow (access & refresh tokens)
- 🧾 RESTful API for data entry and retrieval
- 🔍 Query-based filtering (e.g., filter by title or user)
- 🛡️ Secure environment variable handling
- 📦 Built using Python, Django, DRF

---

## 📁 Project Structure

order_management/              <- Project root folder
├── core/                      <- Django app
├── myproject/                 <- Django project
├── .env.example               <- Sample environment file (never submit your real .env!)
├── manage.py
├── requirements.txt
├── README.md


##Running the Project
# 1. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 2. Start development server
python manage.py runserver





---

## 🔧 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/order-management-oauth-drf.git
cd order-management-oauth-drf

# 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate         # Windows: env\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Copy .env.example to .env and fill in your Google credentials
cp .env.example .env




