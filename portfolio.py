from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os

app = Flask(__name__)

# -------------------------------
# Embedded HTML Templates
# -------------------------------

index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Portfolio</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f9; color: #333; }
    header { background: #333; color: #fff; padding: 15px; margin-bottom: 20px; text-align:center; }
    nav a { color: #fff; margin: 0 10px; text-decoration: none; font-weight: bold; }
    h1, h2 { color: #444; }
    a { color: #0077cc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .profile { text-align:center; margin: 20px 0; }
    .profile img { width: 150px; height: 150px; border-radius: 50%; border: 3px solid #333; }
    .skills { background:#fff; padding:20px; border-radius:10px; box-shadow:0px 2px 5px rgba(0,0,0,0.1); }
    .projects { background:#fff; padding:20px; border-radius:10px; margin-top:20px; box-shadow:0px 2px 5px rgba(0,0,0,0.1); }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to My Portfolio</h1>
    <nav>
      <a href="{{ url_for('home') }}">Home</a>
      <a href="{{ url_for('contact') }}">Contact</a>
      <a href="{{ url_for('download_resume') }}">Download Resume</a>
    </nav>
  </header>

  <div class="profile">
    <img src="https://via.placeholder.com/150" alt="My Photo">
    <h2>Hello, I'm Bharath 👋</h2>
    <p>A passionate Full Stack Developer (Python | Flask | MERN)</p>
  </div>

  <section class="skills">
    <h2>Skills</h2>
    <ul>
      <li>Python, Flask, Django</li>
      <li>HTML, CSS, JavaScript</li>
      <li>React.js, Node.js, MongoDB</li>
      <li>Git, GitHub, Deployment</li>
    </ul>
  </section>

  <section class="projects">
    <h2>Projects</h2>
    <ul>
      <li><b>Portfolio Website</b> – Personal website built using Flask</li>
      <li><b>Data Analysis Tool</b> – Sales data analysis with Pandas & Matplotlib</li>
      <li><b>MERN Blog App</b> – Blog platform with authentication</li>
    </ul>
  </section>

  <section>
    <h2>Connect with Me</h2>
    <p>
      <a href="https://www.linkedin.com" target="_blank">LinkedIn</a> | 
      <a href="https://github.com" target="_blank">GitHub</a> | 
      <a href="mailto:youremail@example.com">Email Me</a>
    </p>
  </section>
</body>
</html>
"""

contact_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Contact Me</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f9; color: #333; }
    header { background: #333; color: #fff; padding: 15px; margin-bottom: 20px; text-align:center; }
    nav a { color: #fff; margin: 0 10px; text-decoration: none; font-weight: bold; }
    form { max-width: 500px; margin:auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0px 2px 5px rgba(0,0,0,0.2); }
    form input, form textarea, form button { width: 100%; padding: 10px; margin-top: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; }
    form button { background: #333; color: #fff; cursor: pointer; }
    form button:hover { background: #555; }
  </style>
</head>
<body>
  <header>
    <h1>Contact Me</h1>
    <nav>
      <a href="{{ url_for('home') }}">Home</a>
      <a href="{{ url_for('contact') }}">Contact</a>
    </nav>
  </header>

  <form method="POST">
    <label>Name:</label>
    <input type="text" name="name" required><br><br>

    <label>Email:</label>
    <input type="email" name="email" required><br><br>

    <label>Message:</label><br>
    <textarea name="message" required></textarea><br><br>

    <button type="submit">Send</button>
  </form>
</body>
</html>
"""

success_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Message Sent</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f9; color: #333; text-align:center; }
    header { background: #333; color: #fff; padding: 15px; margin-bottom: 20px; }
    nav a { color: #fff; margin-right: 15px; text-decoration: none; font-weight: bold; }
  </style>
</head>
<body>
  <header>
    <h1>✅ Your message has been sent!</h1>
    <nav>
      <a href="{{ url_for('home') }}">Home</a>
    </nav>
  </header>

  <p>Thank you for reaching out. I will get back to you soon.</p>
</body>
</html>
"""

# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template_string(index_html)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Log message in console
        print(f"📩 New message from {name} ({email}): {message}")

        return redirect(url_for("success"))
    return render_template_string(contact_html)

@app.route("/success")
def success():
    return render_template_string(success_html)

@app.route("/resume")
def download_resume():
    return send_from_directory(
        directory=os.getcwd(),  # current folder
        path="resume.pdf",
        as_attachment=True
    )

# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
