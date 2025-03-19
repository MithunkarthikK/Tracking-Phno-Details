import tkinter as tk  
from tkinter import messagebox  
import phonenumbers  
from phonenumbers import timezone, geocoder, carrier  

def get_phone_number_info():  
    number = entry.get()  
    try:  
        phone_number = phonenumbers.parse(number)  
        
        time_zone = timezone.time_zones_for_number(phone_number)  
        
        geolocation = geocoder.description_for_number(phone_number, "en")  
               
        service_provider = carrier.name_for_number(phone_number, "en")  

        result_text.set(f"Timezone: {time_zone}\nLocation: {geolocation}\nService Provider: {service_provider}")  

    except phonenumbers.NumberParseException:  
        messagebox.showerror("Error", "The phone number is not valid.")  

root = tk.Tk()  
root.title("Phone Number Info")  
root.geometry("400x300")  

label = tk.Label(root, text="Enter phone number with country code (e.g., +919874563210):")  
label.pack(pady=10)  

entry = tk.Entry(root, width=30)  
entry.pack(pady=5)  

submit_button = tk.Button(root, text="Submit", command=get_phone_number_info)  
submit_button.pack(pady=20)  

result_text = tk.StringVar()  
result_label = tk.Label(root, textvariable=result_text, justify="left")  
result_label.pack(pady=10)  


root.mainloop()  