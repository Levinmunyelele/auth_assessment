# Full-Stack Authentication Assessment

### Tech Stack
* **Backend:** Python (Flask)
* **Database:** SQLite (SQLAlchemy ORM)
* **Frontend:** Jinja2 Templates + Bootstrap 5
* **Auth:** Flask-Login & Werkzeug Security

### How to Run Locally 
#### For WSL/Linux/macOS
1. **Navigate to project folder:** `cd auth_assessment`
2. **Activate Virtual Environment:** `source venv/bin/activate`
3. **Install Dependencies:** `pip install Flask Flask-SQLAlchemy Flask-Login`
4. **Run Application:** `python3 app.py`
5. **Access:** Open `http://127.0.0.1:5000` in your browser.

#### For Windows (Command Prompt)
1. **Navigate to project folder:** `cd auth_assessment`
2. **Activate Virtual Environment:** `venv\Scripts\activate`
3. **Install Dependencies:** `pip install Flask Flask-SQLAlchemy Flask-Login`
4. **Run Application:** `python app.py`
5. **Access:** Open `http://127.0.0.1:5000` in your browser.

### Technical Decisions & Assumptions
* **SQLite:** Chosen for portability. It allows the project to run immediately on the interviewer's machine without external database configuration.
* **PBKDF2 Hashing:** Selected to demonstrate security awareness by ensuring industry-standard password protection.
* **Server-Side Rendering:** Used Flask templates for faster initial load and simpler state management for this specific scope.


### Future Improvements
If given more time, I would implement:
* **JWT (JSON Web Tokens):** For stateless authentication.
* **Email Verification:** To ensure valid user registration.
* **Rate Limiting:** To protect the login endpoint against brute-force attacks.
* **CSRF Protection:** Implementing Flask-WTF to protect all forms against Cross-Site Request Forgery attacks.

* **Environment Variables:** Moving the SECRET_KEY and database URI to a .env file to ensure no sensitive credentials remain in the source code.

