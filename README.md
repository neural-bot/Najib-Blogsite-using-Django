# Najib Blogsite

## 📌 Introduction
Najib Blogsite is a dynamic and user-friendly blogging platform built with Django. It allows users to create, edit, and delete blog posts while supporting image uploads, category filtering, and user authentication.

## 🚀 Features
- User authentication (signup, login, logout)
- Create, edit, and delete blog posts
- Upload images with posts
- Filter posts by categories
- Responsive UI with Bootstrap

## 🛠️ Installation
### 1. Clone the repository
```bash
git clone https://github.com/neural-bot/Najib-Blogsite-using-Django
cd najib-blogsite
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

## 📂 Project Structure
```
najib-blogsite/
│── blog/              # Django app containing models, views, templates
│── media/             # Stores uploaded images
│── static/            # Static assets (CSS, JS, images)
│── templates/         # HTML templates
│── requirements.txt   # Dependencies list
│── manage.py          # Django project manager
│── db.sqlite3         # Database file (SQLite by default)
```

## 📸 Screenshots
_Add screenshots of your project here_

## 🏗️ Technologies Used
- **Django** – Web framework
- **Bootstrap** – UI styling
- **Pillow** – Image handling

## 💡 Future Improvements
- Add comments section
- Implement user profiles
- Enhance UI/UX

## 🤝 Contribution
Feel free to fork, create issues, and submit pull requests!
