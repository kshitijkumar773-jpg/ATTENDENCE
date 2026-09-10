# AttendanceOS

AttendanceOS is a face-recognition attendance system with a Flask API, Next.js web interface, and a legacy Python desktop interface.

## Features

- Student and teacher account registration
- Teacher employee ID validation
- Face profile registration and training
- Live face-based attendance sessions
- Attendance records and reports
- Responsive HTML/CSS dashboard
- Flask API with MongoDB storage

## Project Structure

```text
Attendance-Management-system-using-face-recognition/
|-- backend/       Flask API and MongoDB integration
|-- frontend/      Next.js web application
|-- attendance.py  Python desktop application
|-- TrainingImage/ Captured face images
|-- Attendance/    Generated attendance records
|-- StudentDetails/
|-- requirements.txt
```

## Requirements

- Windows 10 or newer
- Python 3.11 recommended for DeepFace and TensorFlow compatibility
- Node.js 18 or newer for the web interface
- MongoDB Community Server or a MongoDB Atlas connection
- A working camera for face registration and attendance

## Installation

Clone the repository and enter the project folder:

```powershell
git clone https://github.com/kshitijkumar773-jpg/ATTENDENCE.git
cd ATTENDENCE/Attendance-Management-system-using-face-recognition
```

Install the desktop application dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install the backend dependencies:

```powershell
python -m pip install -r backend/requirements.txt
```

The project creates `TrainingImage` and `Attendance` automatically. Do not commit captured images, model files, passwords, or `.env` files.

## Database Configuration

Start local MongoDB, or create a `.env` file inside `backend`:

```env
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=facerecognition
COLLECTION_NAME=students
THRESHOLD=0.6
```

Never place a MongoDB username or password directly in Python source files.

## Run the Web Application

Open two terminals.

Terminal 1, start the Flask API:

```powershell
cd backend
python app.py
```

The API runs at `http://127.0.0.1:5000`.

Terminal 2, install and start the Next.js frontend:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

## Run the Desktop Application

From the project root:

```powershell
python attendance.py
```

Use the desktop application in this order:

1. Register a student and capture face images.
2. Train the face model.
3. Start automatic attendance.
4. View or export attendance records.

## Health Check

With the backend running, open:

```text
http://127.0.0.1:5000/health
```

`models_ready: true` means the face-recognition models loaded correctly. If it is false, use Python 3.11 and install the backend requirements again.

## Troubleshooting

### `ModuleNotFoundError: No module named 'flask'`

Install backend requirements from the project root:

```powershell
python -m pip install -r backend/requirements.txt
```

### `Error connecting to server`

Make sure the Flask API is running at `http://127.0.0.1:5000`.

### `Database unavailable`

Start MongoDB or set a valid `MONGODB_URI` in `backend/.env`.

### DeepFace or MTCNN is unavailable

Use Python 3.11. Python 3.14 may not have compatible TensorFlow wheels for the face-recognition stack.

## GitHub

Repository: https://github.com/kshitijkumar773-jpg/ATTENDENCE
