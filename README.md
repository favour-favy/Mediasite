# 📸 My Media Gallery

A Django web application for uploading, organizing, and browsing multimedia content (images and videos), with search, pagination, and a commenting system.

## Features

- **Upload media** — add images or videos with a title, description, and category
- **Edit & delete** — update or remove any uploaded item, with a confirmation step before deletion
- **Search** — find items by title
- **Pagination** — gallery displays items 6 per page
- **Categories/tags** — organize media into categories (e.g. personal, receipts)
- **Comments** — visitors can view details of a media item and leave comments
- **Responsive design** — styled with Bootstrap 5, dark theme

## Tech Stack

- Python 3.12
- Django 6.1
- SQLite (default database)
- Bootstrap 5 (via CDN)

## Setup Instructions

1. Clone the repository
   git clone https://github.com/favour-favy/Mediasite.git
   cd Mediasite

2. Create and activate a virtual environment
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies
   pip install django

4. Run migrations
   python manage.py makemigrations
   python manage.py migrate

5. Start the development server
   python manage.py runserver

6. Open in browser
   http://127.0.0.1:8000/

## Models

- Category — name (e.g. "personal", "receipts")
- MediaItem — title, description, file, media_type (image/video), category, uploaded_at
- Comment — linked to a MediaItem, includes name, text, created_at

## Notes

- No user authentication is implemented yet — all uploads and comments are open/public.
- Uploaded files are stored locally in the media/ folder (not included in this repo).

## Author

Favour