# Smart Device Management Website

This website is a tool for managing and monitoring smart devices (e.g., plugs), tracking their energy consumption, and performing automatic control based on a machine learning model's analysis. The system uses a **Flask** backend in Python, a **SQLite** database for storing device data, and an **Angular** frontend to interact with users.

---

## Features

### 1. **Device Management**
   - **View Device Status**: Display a list of devices, including their status (on/off) and current power consumption.
   - **Toggle Device Status**: The admin or user can toggle the status of any device (turn it on/off), which will also update the power consumption value.
   
### 2. **Device History**
   - **Track Device Power Consumption**: View the historical power consumption data of each device.
   - **Device History Logs**: The system logs the power consumption of each device on a daily basis.

### 3. **Energy Consumption Analysis**
   - **Machine Learning Model**: A simple Linear Regression model analyzes the power consumption history of each device.
   - **Automatic Device Control**: Based on the analysis, the model can turn off devices that are identified as idle (based on a predefined threshold).

---

## Architecture Overview

### Backend (Flask)
- **Flask** serves as the backend for the website, providing RESTful APIs that allow interaction with the database and perform machine learning analysis.
- The backend connects to an **SQLite** database to store and retrieve device data, including the current status and power consumption.
- The backend also provides the functionality for toggling device status, viewing device history, and performing the energy consumption analysis.

### Frontend (Angular)
- The **Angular** frontend is responsible for displaying device information, allowing users to toggle device states, and showing the energy analysis.

---

## Installation

### Prerequisites
- Python 3.x
- Node.js and npm (for Angular)
- SQLite (used for local database)

### Backend Setup (Flask)

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Initialize the database:
    ```bash
    python init_db.py
    ```
    This will create the `devices.db` SQLite database with the required tables.

4. Run the Flask backend:
    ```bash
    python app.py
    ```
    The Flask server will be available at `http://localhost:5000`.

### Frontend Setup (Angular)

1. Navigate to the frontend folder:
    ```bash
    cd frontend
    ```

2. Install the required Angular dependencies:
    ```bash
    npm install
    ```

3. Start the Angular development server:
    ```bash
    ng serve
    ```
    The Angular app will be available at `http://localhost:4200`.

---

## API Endpoints

### 1. **Get Devices** (`GET /api/devices`)
   - Returns a list of all devices with their status and power consumption.

### 2. **Toggle Device** (`POST /api/device/<device_id>/toggle`)
   - Toggles the status of a device between "on" and "off". If the device is turned on, the power consumption is randomly generated.

### 3. **Get Device History** (`GET /api/device/history`)
   - Fetches the historical power consumption data for all devices.

### 4. **Analyze and Turn Off Idle Devices** (`POST /api/analyze-and-turn-off`)
   - Uses a machine learning model to analyze the power consumption history and turns off devices that are identified as idle (below a predefined threshold of 5 watts).

---

## Technologies Used
- **Backend**: Python, Flask, SQLite, Flask-CORS, scikit-learn (for machine learning)
- **Frontend**: Angular, TypeScript, HTML, CSS (Tailwind CSS for styling)
- **Database**: SQLite
- **Machine Learning**: Linear Regression (to predict idle state based on power consumption data)

---

## Future Enhancements
- **User Authentication**: Implement a more robust authentication system for users.
- **Advanced Machine Learning**: Integrate more advanced models to predict power consumption and optimize device control.
- **Real-time Updates**: Use WebSockets or similar technologies for real-time updates of device status and power consumption.

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and commit them.
4. Push your changes and create a pull request.

---
