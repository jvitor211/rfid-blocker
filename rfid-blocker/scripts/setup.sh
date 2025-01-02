#!/bin/bash
echo "Setting up the RFID Blocker project..."

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Frontend setup
cd frontend
npm install
cd ..

echo "Setup complete!