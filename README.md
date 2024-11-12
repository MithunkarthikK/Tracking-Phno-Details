# Tracking-Phno-Details
Project Description: Tracking details of Phonenumber Using Python
Overview
The idea behind the application was to help maintaining the data of users.That is, to if we enter the mobile number in our system we can able to get the details about the particular mobile number. Using this system we can get the details like longitude, latitude, if the user is active or not,personal details of user .

Features

Input Handling: The tool prompts the user to enter a phone number, ensuring that it is in the correct format (including the country code).
Timezone Retrieval: It uses the timezone module to determine the timezone(s) associated with the provided phone number.
Geolocation Information: The tool retrieves the geographical location of the phone number using the geocoder module, providing a description based on the input number.
Service Provider Identification: It identifies the telecommunications service provider for the entered phone number using the carrier module.

Technical Details

Language: Python
Library Used: phonenumbers
Input: A string representing a phone number, including the country code (e.g., +14155552671).
Output:
Timezone(s) associated with the phone number.
Location description (city, region, etc.).
Name of the service provider.

Example Usage

User Input: The user is prompted to enter a phone number, such as +14155552671.
Output: The program will output:
Timezone: ['America/New_York']
Location: New York, New York
Service Provider: Verizon Wireless
