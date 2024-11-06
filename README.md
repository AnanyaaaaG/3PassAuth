# Multi-Page Password Authentication System

This project is a simple multi-page password authentication system built using Flask. The application requires users to enter a set of three passwords, one at a time, to authenticate successfully. Passwords are stored in a CSV file, allowing for easy management and updates.

## Features

- Multi-page authentication flow
- Passwords stored in a CSV file
- User-friendly interface with centered text and input fields
- Success and failure messages displayed on separate pages

## Project Structure

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install Flask if you haven't already:

   ```bash
   pip install Flask
   ```

4. Ensure you have the `passwords.csv` file with the desired password sets in the project directory.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to start the authentication process.

3. Enter the first password. If it matches, you will be directed to the second password page. Continue this process until all three passwords are entered.

4. If all passwords match the corresponding set in the CSV file, you will see a success message. If any password is incorrect, you will be redirected to a failure page.

## Customization

- To change the passwords, simply edit the `passwords.csv` file. Each line should contain a set of three passwords separated by commas.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Flask documentation: [Flask](https://flask.palletsprojects.com/)
- CSV module documentation: [CSV](https://docs.python.org/3/library/csv.html)
