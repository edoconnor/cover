![Coverage Checker Screenshot](/screenshot.png)

# Rectangle Coverage Checker

## Overview

The Rectangle Coverage Checker is a web application that allows users to set a target rectangle and multiple region rectangles on a canvas. The application then determines if the target rectangle is completely covered by the region rectangles. This application was developed using Python's built-in functions and packaged as a web app using the Flask framework. It is deployed to Heroku for easy access and use.

## How It Works

### 1. Setting Up the Application
- **Backend**: The backend of the application is built using Flask, a lightweight web framework for Python. The coverage algorithm is implemented using Python's built-in functions.
- **Frontend**: The frontend is developed using HTML, CSS, and JavaScript. Bootstrap is used for styling and layout.
- **Deployment**: The application is deployed on Heroku, a cloud platform that simplifies the deployment process.

### 2. Using the Application
- **Set Target**: Click the "Set Target" button and draw a rectangle on the canvas. This rectangle represents the target area that needs to be covered.
- **Add Regions**: Click the "Set Region" button and draw multiple rectangles on the canvas. These rectangles represent the regions that will potentially cover the target area.
- **Check Coverage**: Click the "Check Coverage" button to determine if the target rectangle is completely covered by the region rectangles.
- **Clear Canvas**: Click the "Clear" button to reset the canvas and start over.

### 3. Coverage Algorithm
The coverage algorithm works by checking if all corners of the target rectangle are covered by at least one region rectangle. Here's how it works:

1. **Extract Corners of the Target Rectangle**:
   - The target rectangle's corners are extracted as four points: (top-left, top-right, bottom-left, bottom-right).
   
2. **Check Each Corner**:
   - For each corner of the target rectangle, the algorithm checks if it lies within any of the region rectangles.

3. **Determine Coverage**:
   - If all corners of the target rectangle are covered by at least one region rectangle, the target is considered covered. Otherwise, it is not covered.

