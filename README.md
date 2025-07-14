# SkillMate Pro 🎯

A personalized career planning and skill tracking system built with Django.  
Users can add their skills, set short-term goals, log completed courses, and view custom career roadmaps.

## 🚀 Features

- 🔐 User Authentication (Signup/Login/Logout)
- 🧠 Skill Input & Management
- 🎯 Goal Tracking with Completion Status
- 📚 Course Completion Logging
- 🗺️ Skill-based Career Roadmaps
- 📊 Dashboard Overview with Progress Tracker
- 💡 Dynamic Skill Suggestions & Quick Actions

## 🛠️ Tech Stack

- Frontend: HTML5, Tailwind CSS
- Backend: Python, Django
- Database: SQLite (default), PostgreSQL/MySQL (recommended for production)
- Authentication: Django's built-in auth system

## ✅ Setup Instructions

1. Clone the Repository
   
   git clone https://github.com/your-username/skillmate-navi.git
   cd skillmate-navi


2. Create a Virtual Environment

   ```
   python -m venv env
   env\Scripts\activate  # On Windows
   ```

3. Install Dependencies

   ```
   pip install -r requirements.txt
   ```

4. Run Migrations

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the Development Server

   ```
   python manage.py runserver
   ```

6. Open in Browser

   ```
   http://127.0.0.1:8000/
   ```


## 📂 Folder Structure

```
skillmate_navi/
├── career/                # App folder (views, models, templates)
├── static/                # Tailwind CSS
├── templates/career/      # HTML templates
├── skillmate_navi/        # Project settings
├── db.sqlite3             # Default database
└── manage.py              # Django entry point
```

## 👤 Superuser Setup

```
python manage.py createsuperuser

```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Built with ❤️ by [Sravika Kadali](https://github.com/sravika1914)

Built with ❤️ by [Priya Bandaru](https://github.com/Priya09023)
