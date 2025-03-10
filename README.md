# Contact Scraper

A Python-based web scraper for extracting contact information from the Bundeling platform.

## Features

- Automated browser session management using Selenium
- Manual login support for secure authentication
- Chrome profile integration for persistent sessions
- Screenshot capture for debugging

## Prerequisites

- Python 3.9 or higher
- Chrome browser installed
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fkeijzer/contact_scraper.git
cd contact_scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with your credentials:
```
BUNDELING_USERNAME=your_username
BUNDELING_PASSWORD=your_password
BUNDELING_GROUP=your_group_name
```

## Usage

1. Run the scraper:
```bash
python src/scraper.py
```

2. When prompted, log in manually:
   - Select the correct client
   - Enter your username and password
   - Click the login button
   - Wait until you reach the dashboard
   - Press Enter to continue

3. The scraper will then proceed to extract the required information.

## Development

The project structure:
```
contact_scraper/
├── src/
│   ├── scraper.py      # Main scraper implementation
│   ├── config.py       # Configuration management
│   └── test_connection.py  # Connection testing
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
└── README.md         # This file
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 