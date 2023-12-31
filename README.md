# Obscenity Blocker Solution Extension

Welcome to the Obscenity Blocker Solution Extension! This project is aimed at providing a comprehensive solution for blocking explicit and offensive content across various platforms. This README file will guide you through the structure of the project and provide instructions for setting it up and running.

## Project Structure

The Git repository contains two main folders:

1. **backend**: This folder contains the backend services responsible for handling the core functionalities of the Obscenity Blocker Solution.
   - **obscenity_text**: This folder contains the microservice responsible for detecting explicit content in text data.
   - **obscenity_image**: This folder contains the service responsible for processing images and detecting explicit content within them.
   - **obscenity_video**: This folder contains the service responsible for processing videos and detecting explicit content within them.
   - **obscenity_analytics**: This folder contains the service responsible for collecting and analyzing data related to content filtering and user interactions.

2. **frontend**: This folder contains the frontend components of the Obscenity Blocker Solution Extension.
   - **chrome_extension**: This folder contains the Chrome extension, which integrates with the browser to provide content filtering capabilities.
   - **rakshak_frontend_website**: This folder contains the React application that serves as the user interface for the analytics dashboard.

## Getting Started

To get started with the Obscenity Blocker Solution Extension, follow these steps:

1. Clone the repository to your local machine.

2. Backend Setup:
   To set up the backend services, follow these steps for each FastAPI application:

   - Navigate to the respective folders within the `backend` directory for each backend service.
   - Open a terminal or command prompt and navigate to the backend service's folder.
   - Install the required dependencies by running the following command:
     ```
     pip install -r requirements.txt
     ```
   - Configure any environment variables or settings specific to the backend service.
   - Start the FastAPI application using a command similar to the following:
     ```
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```
     Here, `main` refers to the main Python file containing the FastAPI application, `app` is the instance of the FastAPI app, `--host 0.0.0.0` specifies that the application should listen on all available network interfaces, and `--port 8000` sets the port number for the application.
   - Repeat the above steps for each backend service within the `backend` directory.

3. Frontend Setup:
   - For the Chrome extension:
     1. Open the Google Chrome browser.
     2. In the address bar, type `chrome://extensions` and press Enter. This will open the Extensions page.
     3. Enable Developer mode by toggling the switch located in the top-right corner of the Extensions page.
     4. Click on the "Load unpacked" button that appears after enabling Developer mode.
     5. A file explorer window will open. Navigate to the directory where your Chrome extension is located.
     6. Select the folder that contains the Chrome extension and click the "Select Folder" button.
     7. The Chrome extension will now be loaded in developer mode.
     8. You should see the extension listed on the Extensions page, and it will be enabled by default.
     9. You can interact with the extension by clicking on its icon in the Chrome toolbar.
   
   - For the React application:
     - Open the `react-app` folder in your preferred code editor.
     - Install the dependencies by running the following command:
       ```
       npm install
       ```
     - Start the development server:
       ```
       npm run dev
       ```
     - Access the React application through your browser at the provided URL.

## Usage

Once the project is set up, you can start using the Obscenity Blocker Solution Extension to block explicit and offensive content. Here are some steps to get you started:

1. Launch the Chrome browser with the installed extension.
2. Configure the extension's settings as per your preferences.
3. Browse various websites and observe how the extension detects and blocks explicit content.
4. Interact with the React application to manage and monitor the content filtering process.
5. Explore the analytics service to gain insights into the detected content and user interactions.

**Thank you for using the Obscenity Blocker Solution Extension!**
