# Shopping App Backend in Python
A **Backend-only** e-commerce simulation build in Python, featuring **user/admin login**, **product catalog**, **cart management stock validation**, and **payment simulation**.
Designed with **modular architecture** and **role-based access control** to mimic real-world enterprise applications.

---

## Features
- **User & Admin Login** with session management
- **Role-based Access Control** — separate privileges for users and admins
- **Product Catalog** with categories
- **Admin Functions**:
  - Add, update, delete products
  - Add, delete categories
- **User Functions**:
  - View products & categories
  - Add/remove/view cart items
  - Checkout with payment simulation
- **Stock Validation** — prevent over-ordering
- **Payment Options**: UPI, Credit Card, Net Banking
- **Modular Codebase** for easy maintenance and future upgrades

---

## Project Structure
shopping-app-python/
│
├── shopping_app/
│ ├── init.py
│ ├── data.py # In-memory database
│ ├── auth.py # Authentication & session management
│ ├── catalog.py # Product & category management
│ ├── cart.py # Shopping cart operations
│ ├── payment.py # Payment simulation & stock deduction
│ ├── utils.py # Helper functions
│ └── main.py # Menu-driven app entry point
│
├── requirements.txt
├── README.md


---

## 🔑 Example Credentials
**User Login**
Username: user1
Password: pass123
Role: user

**Admin Login**
Username: admin1
Password: adminpass
Role: admin


---

## 🖥 How to Run
1. **Clone the Repository**
bash
git clone https://github.com/Arshad123-khan/shopping-app-python.git
cd shopping-app-python
python -m shopping_app.main
