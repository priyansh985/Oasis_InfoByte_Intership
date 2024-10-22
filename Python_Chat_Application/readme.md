# Python Chat Application

This is a simple chat application built using Python and Flask with Socket.IO for real-time communication. The application allows users to join chat rooms and communicate with each other in real-time.

## Features

- Real-time messaging using Flask-SocketIO.
- Ability to create and join chat rooms.
- Unique room codes for each chat room.
- User-friendly interface.

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory.
2. Run the `app.py` file:
    ```bash
    python app.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000/`.
4. Enter a username and a room code to join a chat room, or create a new room.

## Code Overview

- `app.py`: Contains the main application code, including the Flask routes and Socket.IO event handlers.
- `templates/`: Contains the HTML templates for the application.
- `static/`: Contains the static files (CSS, JavaScript) for the application.

## Example

1. Open the application in your web browser.
2. Enter a username and a room code to join an existing chat room, or create a new room.
3. Start chatting with other users in the room.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Flask and Flask-SocketIO documentation and tutorials for providing guidance on building the application.
- Oasis Infobyte Internship for the project opportunity.