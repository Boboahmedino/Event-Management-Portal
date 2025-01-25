### **Event Management Portal**

#### **Overview**  
This web-based Event Management Portal, built with HTML, CSS, JavaScript, and Django, provides an efficient solution for organizing and managing events at Lagos State University. It allows users both within and outside the university community to view, register for events, and book halls for events, all through an intuitive interface. Admins have the ability to manage events, track reservations, and handle event-related logistics seamlessly.

#### **Features**

- **User Authentication:** Secure user authentication allows individuals to create accounts, log in, and safely manage their event registrations and hall bookings.
- **Event Management:** Admins can add, update, or remove events, providing key details such as dates, times, locations, and descriptions to keep the community informed.
- **Hall Booking and Reservations:** Users, both within and outside the university community, can browse available halls, make reservations for events, and secure booking slots through the portal. Admins can review and manage all reservations.
- **Event Tracking:** Once registered or booked, users can track event participation and reservation status, and access relevant event materials or updates.
- **Responsive Design:** The portal is designed to be fully responsive, ensuring seamless use on all devices, including mobile phones, tablets, and desktops.

#### **Installation**

To run this application, you need to install the required libraries listed in the `requirements.txt` file. Follow the steps below to install the dependencies:

1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the following command to install all required libraries:
   ```bash
   pip install -r requirements.txt
   ```
This command will automatically install all the necessary libraries, including Django and other dependencies, ensuring your project is ready to run.

#### **Additional Notes**

- **Database Configuration:** This application is designed to work seamlessly with PostgreSQL as the default database. Ensure you have a PostgreSQL server running locally with the required database (e.g., "EventDB") and user credentials configured as specified in the project settings. Alternatively, the application can also be configured to work with MySQL by updating the database settings in the `settings.py` file.
  
- **Static and Media Files:** Ensure that all necessary static files, such as images (e.g., event banners, logos), are placed in the appropriate directories as defined in the Django project settings. Update file paths as needed to match your setup.

- **Customizability:** This platform is highly customizable and can be extended with additional features like event notifications, multi-user roles (admin, participant, guest), user feedback systems, and more.

- **Environment Setup:** It is recommended to use a virtual environment to manage your dependencies and ensure a clean project setup. This helps isolate the project’s libraries and avoid conflicts with other Python projects.
