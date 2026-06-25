# 💰 MoneyMentor

MoneyMentor is a modern personal finance management web application built with Django. It helps users track income, manage expenses, analyze spending habits, and gain insights into their financial activities through an intuitive dashboard.

---

## 🚀 Features

### Authentication

* User Registration
* Secure Login & Logout
* User-specific financial data

### Financial Management

* Income Tracking
* Expense Tracking
* Transaction Categorization
* Transaction Notes

### Analytics

* Spending Analysis
* Income vs Expense Insights
* Financial Summary Dashboard
* Data Visualization Support

### User Experience

* Clean and Responsive Interface
* Easy Navigation
* Organized Financial Records

---

## 🛠 Tech Stack

### Backend

* Python 3.14
* Django

### Database

* PostgreSQL

### Frontend

* HTML5
* CSS3
* JavaScript

### Version Control & DevOps

* Git
* GitHub
* GitHub Actions (CI)

---

## 📂 Project Structure

```text
MoneyMentor/
│
├── accounts/          # User authentication app
├── MoneyMentor/       # Finance management app
├── core/              # Django project settings
├── static/            # CSS, JS, Images
├── templates/         # HTML templates
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone git@github.com:Sreeraam19/MoneyMentor.git
cd MoneyMentor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key

DB_NAME=moneymentor
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Continuous Integration

This project uses GitHub Actions to automatically:

* Install dependencies
* Verify Django configuration
* Run project checks on every push

Workflow location:

```text
.github/workflows/django.yml
```

---

## 🎯 Future Roadmap

* Budget Planning
* Savings Goals
* Monthly Reports
* Export to Excel/PDF
* Financial Forecasting
* AI-Powered Insights
* Multi-Currency Support

---

## 📸 Screenshots

Screenshots will be added as the project evolves.

---

## 👨‍💻 Author

**M.K. Sreeraam**

Student • Python Enthusiast • Django Developer

---

## 📜 License

This project is currently under development.

A license will be added in a future release.
