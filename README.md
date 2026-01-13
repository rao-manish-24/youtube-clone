# 🎬 YouTube Clone

A full-featured YouTube clone built with Django and ImageKit.io for video storage and streaming. Users can upload, watch, like/dislike videos, and view channel pages.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **User Authentication** - Register, login, logout functionality
- **Video Upload** - Upload videos up to 100MB (MP4, WebM, MOV, AVI)
- **Video Streaming** - HLS adaptive bitrate streaming (240p to 1080p)
- **Custom Thumbnails** - Upload custom thumbnails or auto-generate from video
- **Like/Dislike System** - Vote on videos with real-time updates
- **Channel Pages** - View all videos from a specific user
- **Video Watermarks** - Automatic username watermark on thumbnails
- **Responsive Design** - Dark theme UI inspired by YouTube


## 🛠️ Tech Stack

- **Backend**: Django 5.1+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Video Storage**: [ImageKit.io](https://imagekit.io)
- **Static Files**: WhiteNoise
- **WSGI Server**: Gunicorn
- **Deployment**: Railway

## 📁 Project Structure

```
youtube-clone/
│
├── 📂 youtube/                     # Django project root
│   │
│   ├── 📂 accounts/                # Authentication app
│   │   ├── 📂 templates/accounts/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── logged_out.html
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── 📂 videos/                  # Main video app
│   │   ├── 📂 templates/videos/
│   │   │   ├── list.html           # Home page
│   │   │   ├── detail.html         # Video player
│   │   │   ├── upload.html         # Upload form
│   │   │   └── channel.html        # Channel page
│   │   ├── forms.py                # Upload form
│   │   ├── imagekit_client.py      # ImageKit integration
│   │   ├── models.py               # Video, VideoLike
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── 📂 static/css/              # Stylesheets
│   │   ├── variables.css
│   │   ├── base.css
│   │   ├── navbar.css
│   │   ├── videos.css
│   │   └── ...
│   │
│   ├── 📂 templates/
│   │   └── base.html               # Base template
│   │
│   ├── 📂 youtube/                 # Settings module
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── .python-version
├── pyproject.toml
├── requirements.txt
├── Procfile
├── railway.toml
└── README.md
```

---

## 📚 API Reference

### Public Endpoints

| Method | Endpoint | Description |
|:------:|----------|-------------|
| `GET` | `/` | Home page - list all videos |
| `GET` | `/<id>` | Video detail & player |
| `GET` | `/channel/<username>/` | User channel page |

### Protected Endpoints (Auth Required)

| Method | Endpoint | Description |
|:------:|----------|-------------|
| `GET` | `/upload/` | Upload form page |
| `POST` | `/upload/submit/` | Submit video upload |
| `POST` | `/<id>/vote/` | Like/dislike video |
| `POST` | `/<id>/delete/` | Delete video (owner) |

### Authentication

| Method | Endpoint | Description |
|:------:|----------|-------------|
| `GET/POST` | `/accounts/register/` | User registration |
| `GET/POST` | `/accounts/login/` | User login |
| `POST` | `/accounts/logout/` | User logout |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/awesome-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add awesome feature"
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/awesome-feature
   ```
5. **Open** a Pull Request
