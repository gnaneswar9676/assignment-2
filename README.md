# CDP Chatbot

A command-line support agent chatbot designed to assist users with "how-to" questions and comparisons for four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. This project fulfills Assignment 2 requirements by leveraging official documentation to provide accurate, platform-specific guidance. Built with Python, it emphasizes software engineering principles over complex model-building.

## Objective
Develop a chatbot that:
- Answers "how-to" questions (e.g., "How do I set up a new source in Segment?").
- Extracts relevant information from official CDP documentation.
- Handles variations in question phrasing and irrelevant queries.
- Offers bonus features like cross-CDP comparisons.

## Data Sources
- **Segment:** [https://segment.com/docs/](https://segment.com/docs/)
- **mParticle:** [https://docs.mparticle.com/](https://docs.mparticle.com/)
- **Lytics:** [https://docs.lytics.com/](https://docs.lytics.com/)
- **Zeotap:** [https://docs.zeotap.com/home/en-us/](https://docs.zeotap.com/home/en-us/)

## Features

### Core Functionalities
1. **"How-to" Questions:**
   - Responds to queries about tasks or features in each CDP.
   - Examples:
     - "How do I set up a new source in Segment?"
     - "How can I create a user profile in mParticle?"
2. **Documentation Extraction:**
   - Fetches and indexes content from CDP documentation.
   - Uses fuzzy matching to find relevant answers.
3. **Question Handling:**
   - Processes long, short, or irrelevant questions without breaking.
   - Example: "Which movie is out this week?" → Polite redirection.

### Bonus Features
1. **Cross-CDP Comparisons:**
   - Compares approaches between platforms.
   - Example: "How does Segment's audience creation compare to Lytics?"
2. **Advanced Questions:**
   - Capable of handling more specific queries with targeted doc URLs.

## Project Structure

![image](https://github.com/user-attachments/assets/8897b984-0037-4903-89f7-9727ffe4854a)


## Prerequisites
- **Python:** 3.6 or higher
- **Libraries:**
  - `requests` (HTTP requests)
  - `beautifulsoup4` (HTML parsing)
  - `fuzzywuzzy` (Fuzzy string matching)
  - `python-Levenshtein` (Speeds up fuzzy matching)
- **Internet Connection:** For live doc fetching

## Installation
1. **Clone or Create the Project:**
   ```bash
   git clone <repository-url>
   cd cdp-chatbot
##output
![image](https://github.com/user-attachments/assets/e44788f8-26a4-4d15-9f4d-2b2b5ba0b7f5)
