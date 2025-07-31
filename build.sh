#!/bin/bash

echo "🔧 Setting up virtual environment..."
python -m venv venv
source venv/bin/activate

echo "⬇️ Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🛠️ Running migrations..."
python manage.py migrate

echo "✅ Build completed!"
