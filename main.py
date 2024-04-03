from hospitalsystem import HospitalManagementSystem
import tkinter as tk
from tkinter import messagebox
from patient import Patient
from doctor import Doctor

#call main function
if __name__ == "__main__":
    # Create an instance of the HospitalManagementSystem
    hospital = HospitalManagementSystem()

    # Function to handle choices
    def handle_choice(choice):
        if choice == "1":
            hospital_management_menu()  #call hospital_management_menu
        elif choice == "2":
            manage_consultation_menu()  #call manage_consultation_menu
        elif choice == "3":
            prescription_submenu()  # Call prescription_submenu 
        elif choice == "4":
            exit_application()  #exit
        else:
            messagebox.showinfo("Invalid Choice", "Please enter a valid choice.")

    def add_patient_record_window():
        # Create a new window for adding patient record
        add_patient_window = tk.Toplevel(root)
        add_patient_window.title("Add Patient Record")
        add_patient_window.geometry("400x300")  # width and height

        # Function to handle adding patient record
        def add_patient_record():
            # get data from entry widgets
            patient_id = id_entry.get()   #get id
            patient_name = name_entry.get()   #get name
            patient_age = age_entry.get()    #get age 
            patient_condition = condition_entry.get()   #get condition
            patient_admission_date = admission_date_entry.get()    #get admission date

            # Create a Patient object
            patient = Patient(patient_id, patient_name, patient_age, patient_condition, patient_admission_date)

            # Call hospital add_patient method
            hospital.add_patient(patient)

            # Display message
            messagebox.showinfo("Success", "Patient added successfully.")

        # Define tkinter layouts and widgets
        id_label = tk.Label(add_patient_window, text="ID:")
        id_label.pack()
        id_entry = tk.Entry(add_patient_window)
        id_entry.pack()

        #for name 
        name_label = tk.Label(add_patient_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(add_patient_window)
        name_entry.pack()

        #for age
        age_label = tk.Label(add_patient_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(add_patient_window)
        age_entry.pack()

        #for condition
        condition_label = tk.Label(add_patient_window, text="Condition:")
        condition_label.pack()
        condition_entry = tk.Entry(add_patient_window)
        condition_entry.pack()

        #for admission date
        admission_date_label = tk.Label(add_patient_window, text="Admission Date (YYYY-MM-DD):")
        admission_date_label.pack()
        admission_date_entry = tk.Entry(add_patient_window)
        admission_date_entry.pack()

        #add button for add patient
        add_button = tk.Button(add_patient_window, text="Add Patient", command=add_patient_record)
        add_button.pack()

    #doctor window 
    def add_doctor_record_window():
        # Create a new window for adding doctor record
        add_doctor_window = tk.Toplevel(root)
        add_doctor_window.title("Add Doctor Record")
        add_doctor_window.geometry("400x300")  #width and height

        # Function to handle adding doctor record
        def add_doctor_record():
            # get data from entry widgets
            doctor_id = id_entry.get()
            doctor_name = name_entry.get()
            doctor_experience = experience_entry.get()
            doctor_specialization = specialization_entry.get()

            # Create a Doctor object
            doctor = Doctor(doctor_id, doctor_name, doctor_experience, doctor_specialization)

            # Call hospital add_doctor method
            hospital.add_doctor(doctor)

            # Display success message
            messagebox.showinfo("Success", "Doctor added successfully.")

        # Define tkinter widgets and layout for adding doctor record window
        id_label = tk.Label(add_doctor_window, text="ID:")
        id_label.pack()
        id_entry = tk.Entry(add_doctor_window)
        id_entry.pack()

        #for doctor name
        name_label = tk.Label(add_doctor_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(add_doctor_window)
        name_entry.pack()

        #for doctor experience
        experience_label = tk.Label(add_doctor_window, text="Experience:")
        experience_label.pack()
        experience_entry = tk.Entry(add_doctor_window)
        experience_entry.pack()

        #for doctor specialization
        specialization_label = tk.Label(add_doctor_window, text="Specialization:")
        specialization_label.pack()
        specialization_entry = tk.Entry(add_doctor_window)
        specialization_entry.pack()

        #add button to add doctor when details added
        add_button = tk.Button(add_doctor_window, text="Add Doctor", command=add_doctor_record)
        add_button.pack()

    #view all patients window
    def view_all_patients_window():
        # Create a new window for viewing all patients
        view_patients_window = tk.Toplevel(root)
        view_patients_window.title("View All Patients")
        view_patients_window.geometry("600x400")  #width and height

        # Call hospital view_all_patients method to get all patient records
        patients_records = hospital.view_all_patients()

        # Display patient records in a text widget 
        patients_text = tk.Text(view_patients_window)
        patients_text.pack(expand=True, fill="both")

        #used loop here to display the details
        for record in patients_records:
            patients_text.insert("end", "ID: {}\n".format(record["id"]))
            patients_text.insert("end", "Name: {}\n".format(record["name"]))
            patients_text.insert("end", "Age: {}\n".format(record["age"]))
            patients_text.insert("end", "Admission Date: {}\n".format(record["admission_date"]))
            patients_text.insert("end", "Condition: {}\n\n".format(record["condition"]))

        patients_text.config(state="disabled")

    #view all doctors window function
    def view_all_doctors_window():
        # Create a new window for viewing all doctors
        view_doctors_window = tk.Toplevel(root)
        view_doctors_window.title("View All Doctors")
        view_doctors_window.geometry("600x400")  # width and height

        # Call hospital view_all_doctors method to get all doctors records
        doctors_records = hospital.view_all_doctors()

        # Display doctor records in a text widget
        doctors_text = tk.Text(view_doctors_window)
        doctors_text.pack(expand=True, fill="both")

        #used loop here to print details of doctors
        for record in doctors_records:
            doctors_text.insert("end", "ID: {}\n".format(record["id"]))
            doctors_text.insert("end", "Name: {}\n".format(record["name"]))
            doctors_text.insert("end", "Experience: {}\n".format(record["experience"]))
            doctors_text.insert("end", "Specialization: {}\n\n".format(record["specialization"]))

        doctors_text.config(state="disabled")
        doctors_text.config(state="disabled")

    #update patient details window function
    def update_patient_record_window():
        # Create a new window for updating patient record
        update_patient_window = tk.Toplevel(root)
        update_patient_window.title("Update Patient Record")
        update_patient_window.geometry("400x300")  # width and height

        # Function to handle updating patient record
        def update_patient_record():
            # get data from tkinter entry widgets
            patient_id = id_entry.get()
            new_name = name_entry.get()
            new_age = age_entry.get()
            new_admission_date = admission_date_entry.get()
            new_condition = condition_entry.get()

            # Call hospital update_patient_record method
            if hospital.update_patient_record(patient_id, new_name, new_age, new_admission_date, new_condition):
                messagebox.showinfo("Success", "Patient record updated successfully.")
            else:
                messagebox.showerror("Error", "Failed to update patient record because id not found.")

        # Define widgets and layout for updating patient record window
        id_label = tk.Label(update_patient_window, text="Patient ID:")
        id_label.pack()
        id_entry = tk.Entry(update_patient_window)
        id_entry.pack()

        #updated name 
        name_label = tk.Label(update_patient_window, text="New Name:")
        name_label.pack()
        name_entry = tk.Entry(update_patient_window)
        name_entry.pack()

        #updated age
        age_label = tk.Label(update_patient_window, text="New Age:")
        age_label.pack()
        age_entry = tk.Entry(update_patient_window)
        age_entry.pack()

        #updated admission date
        admission_date_label = tk.Label(update_patient_window, text="New Admission Date (YYYY-MM-DD):")
        admission_date_label.pack()
        admission_date_entry = tk.Entry(update_patient_window)
        admission_date_entry.pack()

        #updated condition
        condition_label = tk.Label(update_patient_window, text="New Condition:")
        condition_label.pack()
        condition_entry = tk.Entry(update_patient_window)
        condition_entry.pack()

        #add update button to press it
        update_button = tk.Button(update_patient_window, text="Update Patient Record", command=update_patient_record)
        update_button.pack()

    #update doctor record window function
    def update_doctor_record_window():
        # Create a new window for updating doctor record
        update_doctor_window = tk.Toplevel(root)
        update_doctor_window.title("Update Doctor Record")
        update_doctor_window.geometry("400x300")  #width and height

        # Function to handle updating doctor record
        def update_doctor_record():
            # get data from tkinter entry widgets
            doctor_id = id_entry.get()
            new_name = name_entry.get()
            new_specialization = specialization_entry.get()
            new_experience = experience_entry.get()

            # Call hospital update_doctor_record method
            if hospital.update_doctor_record(doctor_id, new_name, new_experience, new_specialization):
                messagebox.showinfo("Success", "Doctor record updated successfully.")
            else:
                messagebox.showerror("Error", "Failed to update doctor record because id not found.")

        # Define widgets and layout for updating doctor record window
        id_label = tk.Label(update_doctor_window, text="Doctor ID:")
        id_label.pack()
        id_entry = tk.Entry(update_doctor_window)
        id_entry.pack()

        #for updated name
        name_label = tk.Label(update_doctor_window, text="New Name:")
        name_label.pack()
        name_entry = tk.Entry(update_doctor_window)
        name_entry.pack()

        #for new specialiation
        specialization_label = tk.Label(update_doctor_window, text="New Specialization:")
        specialization_label.pack()
        specialization_entry = tk.Entry(update_doctor_window)
        specialization_entry.pack()

        #for updated experience
        experience_label = tk.Label(update_doctor_window, text="New Experience (in years):")
        experience_label.pack()
        experience_entry = tk.Entry(update_doctor_window)
        experience_entry.pack()

        #add updated button to press it
        update_button = tk.Button(update_doctor_window, text="Update Doctor Record", command=update_doctor_record)
        update_button.pack()

    #remove patient record window function
    def remove_patient_record_window():
        # Create a new window for removing patient record
        remove_patient_window = tk.Toplevel(root)
        remove_patient_window.title("Remove Patient Record")
        remove_patient_window.geometry("300x200")  # width and height

        # Function to handle removing patient record
        def remove_patient_record():
            # get data from tkinter entry widget
            patient_id = id_entry.get()

            # Call hospital remove_patient_record method
            if hospital.remove_patient_record(patient_id):
                messagebox.showinfo("Success", "Patient record removed successfully.")
            else:
                messagebox.showerror("Error", "Failed to remove patient record because id not found.")

        # Define widgets and layout for removing patient record window
        id_label = tk.Label(remove_patient_window, text="Patient ID:")
        id_label.pack()
        id_entry = tk.Entry(remove_patient_window)
        id_entry.pack()

        #add remove button to press it
        remove_button = tk.Button(remove_patient_window, text="Remove Patient Record", command=remove_patient_record)
        remove_button.pack()

    #remove doctor record window function
    def remove_doctor_record_window():
        # Create a new window for removing doctor record
        remove_doctor_window = tk.Toplevel(root)
        remove_doctor_window.title("Remove Doctor Record")
        remove_doctor_window.geometry("300x200")  #width and height

        # Function to handle removing doctor record
        def remove_doctor_record():
            # get data from tkinter entry widget
            doctor_id = id_entry.get()

            # Call hospital remove_doctor_record method
            if hospital.remove_doctor_record(doctor_id):
                messagebox.showinfo("Success", "Doctor record removed successfully.")
            else:
                messagebox.showerror("Error", "Failed to remove doctor record because id not found.")

        # Define widgets and layout for removing doctor record window
        id_label = tk.Label(remove_doctor_window, text="Doctor ID:")
        id_label.pack()
        id_entry = tk.Entry(remove_doctor_window)
        id_entry.pack()

        #add remove button to press it for remove
        remove_button = tk.Button(remove_doctor_window, text="Remove Doctor Record", command=remove_doctor_record)
        remove_button.pack()

    #add patient for doctor queue window function
    def add_patient_for_specific_doctor_queue_window():
        # Create a new window for adding a patient to a specific doctor queue
        add_patient_to_queue_window = tk.Toplevel(root)
        add_patient_to_queue_window.title("Add Patient to Doctor's Queue")
        add_patient_to_queue_window.geometry("400x200")  #width and height

        # Function to handle adding a patient to a specific doctor queue
        def add_patient_to_queue():
            # get data from tkinter entry widgets
            patient_id = patient_id_entry.get()
            doctor_id = doctor_id_entry.get()

            # Call hospital add_patient_for_specific_doctor_queue method
            if hospital.add_patient_for_specific_doctor_queue(patient_id, doctor_id):
                messagebox.showinfo("Success", "Patient added to doctor's queue successfully.")
            else:
                messagebox.showerror("Error", "Failed to add patient to doctor's queue because there is issue of id.")

        # Define widgets and layout for adding patient to doctor's queue window
        patient_id_label = tk.Label(add_patient_to_queue_window, text="Patient ID:")
        patient_id_label.pack()
        patient_id_entry = tk.Entry(add_patient_to_queue_window)
        patient_id_entry.pack()

        #doctor id
        doctor_id_label = tk.Label(add_patient_to_queue_window, text="Doctor ID:")
        doctor_id_label.pack()
        doctor_id_entry = tk.Entry(add_patient_to_queue_window)
        doctor_id_entry.pack()

        #add button to press it for enter
        add_button = tk.Button(add_patient_to_queue_window, text="Add to Queue", command=add_patient_to_queue)
        add_button.pack()

    #remove patient from doctor queue window function
    def remove_patient_for_specific_doctor_queue_window():
        # Create a new window for removing a patient from a specific doctor queue
        remove_patient_from_queue_window = tk.Toplevel(root)
        remove_patient_from_queue_window.title("Remove Patient from Doctor's Queue")
        remove_patient_from_queue_window.geometry("400x200")  #width and height

        # Function to handle removing a patient from a specific doctor queue
        def remove_patient_from_queue():
            # get data from tkinter entry widgets
            patient_id = patient_id_entry.get()
            doctor_id = doctor_id_entry.get()

            # Call hospital remove_patient_for_specific_doctor_queue method
            if hospital.remove_patient_for_specific_doctor_queue(doctor_id, patient_id):
                messagebox.showinfo("Success", "Patient removed from doctor's queue successfully.")
            else:
                messagebox.showerror("Error", "Failed to remove patient from doctor's queue because there is issue of id.")

        # Define widgets and layout for removing patient from doctor queue window
        #enter patient id
        patient_id_label = tk.Label(remove_patient_from_queue_window, text="Patient ID:")
        patient_id_label.pack()
        patient_id_entry = tk.Entry(remove_patient_from_queue_window)
        patient_id_entry.pack()

        #enter doctor id
        doctor_id_label = tk.Label(remove_patient_from_queue_window, text="Doctor ID:")
        doctor_id_label.pack()
        doctor_id_entry = tk.Entry(remove_patient_from_queue_window)
        doctor_id_entry.pack()

        #add remove button to press it for remove
        remove_button = tk.Button(remove_patient_from_queue_window, text="Remove from Queue", command=remove_patient_from_queue)
        remove_button.pack()

    #view all doctors queue window function
    def view_all_doctors_queue_window():
        # Create a new window for viewing all doctor queues
        view_doctors_queue_window = tk.Toplevel(root)
        view_doctors_queue_window.title("View All Doctors Queue")
        view_doctors_queue_window.geometry("600x400")  # width and height

        # Call hospital view_all_doctors_queue method to get all doctors queues
        doctors_queues = hospital.view_all_doctors_queue()

        # Display doctor queues in a text widget
        doctors_queue_text = tk.Text(view_doctors_queue_window)
        doctors_queue_text.pack(expand=True, fill="both")

        # Insert the doctors queues into the text widget
        doctors_queue_text.insert("end", doctors_queues)

        # Disable the option of editing in the text widget
        doctors_queue_text.config(state="disabled")

    #show patient summary 
    def show_patient_summary_from_entry(patient_id_entry):
        # Function to display patient summary
        patient_id = patient_id_entry.get()
        show_patient_summary(patient_id)

    #show patient summary 
    def show_patient_summary(patient_id):
        # Function to display patient summary
        summary_window = tk.Toplevel(root)
        summary_window.title("Patient Summary")
        summary_window.geometry("400x300") #width and height

        current_patient = hospital.patients.head
        #loop to display patient details
        while current_patient:
            if current_patient.data.id == patient_id:
                tk.Label(summary_window, text="Patient ID: " + current_patient.data.id).pack()
                tk.Label(summary_window, text="Name: " + current_patient.data.name).pack()
                tk.Label(summary_window, text="Age: " + str(current_patient.data.age)).pack()
                tk.Label(summary_window, text="Condition: " + current_patient.data.condition).pack()

                attending_doctor = None
                current_doctor = hospital.doctors.head
                #loop to check the patient in which doctor queue
                while current_doctor:
                    consultation_queue = current_doctor.data.consultation_queue
                    for item in consultation_queue.items:
                        if item.id == patient_id:
                            attending_doctor = current_doctor.data
                            break
                    if attending_doctor:
                        break
                    current_doctor = current_doctor.next

                #display all the details of docotrs
                if attending_doctor:
                    tk.Label(summary_window, text="Attending Doctor:").pack()
                    tk.Label(summary_window, text="  ID: " + attending_doctor.id).pack()
                    tk.Label(summary_window, text="  Name: " + attending_doctor.name).pack()
                    tk.Label(summary_window, text="  Specialization: " + attending_doctor.specialization).pack()
                    tk.Label(summary_window, text="  Experience: " + str(attending_doctor.experience)).pack()
                else:
                    tk.Label(summary_window, text="Attending Doctor: Not assigned").pack()

                #display prescription prescribed by doctor
                tk.Label(summary_window, text="Prescriptions:").pack()
                prescriptions = hospital.view_prescription_by_patient_id(patient_id)
                if prescriptions:
                    #loop to display details
                    for prescription in prescriptions:
                        tk.Label(summary_window, text="  Prescription ID: " + prescription["id"]).pack()
                        tk.Label(summary_window, text="  Doctor ID: " + prescription["doctor_id"]).pack()
                        tk.Label(summary_window, text="  Doctor Name: " + prescription["doctor_name"]).pack()
                        tk.Label(summary_window, text="  Medication: " + prescription["medication"]).pack()
                        tk.Label(summary_window, text="  Dosage: " + prescription["dosage"]).pack()
                        tk.Label(summary_window, text="  Duration: " + prescription["duration"]).pack()
                        tk.Label(summary_window, text="  Notes: " + prescription["notes"]).pack()
                else:
                    tk.Label(summary_window, text="  No prescriptions found.").pack()

                return
            current_patient = current_patient.next

        tk.Label(summary_window, text="Patient not found.").pack()

    # Create a new window for patient ID entry
    def enter_patient_id_window():
        patient_id_window = tk.Toplevel(root)
        patient_id_window.title("Enter Patient ID")
        patient_id_window.geometry("300x100")  #width and height

        #prompt to enter patient id
        tk.Label(patient_id_window, text="Enter Patient ID:").pack()
        patient_id_entry = tk.Entry(patient_id_window)
        patient_id_entry.pack()

        #submit button to submit the details
        submit_button = tk.Button(patient_id_window, text="Submit", command=lambda: show_patient_summary_from_entry(patient_id_entry.get()))
        submit_button.pack()

    # Function to handle Hospital Management menu
    def hospital_management_menu():
        # Create a new window for Hospital Management submenu
        hospital_management_window = tk.Toplevel(root)
        hospital_management_window.title("Hospital Management")
        hospital_management_window.geometry("500x400")  # width and height


        # Modify the Hospital Management submenu
        choices = [
            "ADD PATIENT IN RECORD",
            "ADD DOCTOR RECORD",
            "UPDATE PATIENT RECORD",
            "UPDATE DOCTOR RECORD",
            "REMOVE PATIENT RECORD",
            "REMOVE DOCTOR RECORD",
            "VIEW ALL PATIENTS",
            "SUMMARY OF PATIENT",
            "VIEW ALL DOCTORS",
            "VIEW ALL DOCTORS QUEUE",
            "ADD PATIENT FOR SPECIFIC DOCTOR QUEUE",
            "REMOVE PATIENT FOR SPECIFIC DOCTOR QUEUE",
            "BACK TO MAIN MENU"
        ]

        #used loop here to display all options 
        for option in choices:
            if option == "ADD PATIENT IN RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=add_patient_record_window)
            elif option == "ADD DOCTOR RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=add_doctor_record_window)
            elif option == "UPDATE PATIENT RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=update_patient_record_window)
            elif option == "UPDATE DOCTOR RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=update_doctor_record_window)
            elif option == "REMOVE PATIENT RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=remove_patient_record_window)
            elif option == "REMOVE DOCTOR RECORD":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=remove_doctor_record_window)
            elif option == "VIEW ALL PATIENTS":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=view_all_patients_window)
            elif option == "SUMMARY OF PATIENT":
                def open_input_window():
                    # Function to open a new window for input
                    input_window = tk.Toplevel(hospital_management_window)
                    #prompt to enter patient id
                    input_window.title("Enter Patient ID")
                    input_window.geometry("300x100") #width and height

                    tk.Label(input_window, text="Enter Patient ID:").pack()

                    patient_id_entry = tk.Entry(input_window)
                    patient_id_entry.pack()

                    #submit summary 
                    def submit_summary():
                        # Function to submit the input and show the patient summary
                        patient_id = patient_id_entry.get()
                        show_patient_summary(patient_id)
                        input_window.destroy()  # Close the input window after submitting

                    submit_button = tk.Button(input_window, text="Submit", command=submit_summary)
                    submit_button.pack()

                # Create button for "SUMMARY OF PATIENT" option
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=open_input_window)
                button.pack(pady=2)
            #to display doctors realted methods
            elif option == "VIEW ALL DOCTORS":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=view_all_doctors_window)
            elif option == "VIEW ALL DOCTORS QUEUE":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=view_all_doctors_queue_window)
            elif option == "ADD PATIENT FOR SPECIFIC DOCTOR QUEUE":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=add_patient_for_specific_doctor_queue_window)
            elif option == "REMOVE PATIENT FOR SPECIFIC DOCTOR QUEUE":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=remove_patient_for_specific_doctor_queue_window)
            elif option == "BACK TO MAIN MENU":
                button = tk.Button(hospital_management_window, text=option, width=40, height=1, command=hospital_management_window.destroy)
            else:
                button = tk.Button(hospital_management_window, text=option, width=40, height=1)
            button.pack(pady=2)

    #update patient condition window function
    def update_patient_condition_window():
        # Create a new window for updating patient condition
        update_condition_window = tk.Toplevel()
        update_condition_window.title("Update Patient Condition")
        update_condition_window.geometry("300x200") #width and height

        # Function to update patient condition
        def update_condition():
            patient_id = patient_id_entry.get()  # Get patient ID 
            new_condition = condition_entry.get()  # Get new condition 
            # Call the update_patient_record method with the provided inputs
            if hospital.update_patient_record(patient_id, new_condition=new_condition):
                result_label.config(text="Patient condition updated successfully.")
            else:
                result_label.config(text="Failed to update patient condition because ID not found.")

        #input patient ID
        patient_id_label = tk.Label(update_condition_window, text="Enter Patient ID:")
        patient_id_label.pack()
        patient_id_entry = tk.Entry(update_condition_window)
        patient_id_entry.pack()

        #input new condition
        condition_label = tk.Label(update_condition_window, text="Enter New Condition:")
        condition_label.pack()
        condition_entry = tk.Entry(update_condition_window)
        condition_entry.pack()

        # Button to update patient condition
        update_button = tk.Button(update_condition_window, text="Update Condition", command=update_condition)
        update_button.pack()

        result_label = tk.Label(update_condition_window, text="")
        result_label.pack()

        # Run the Tkinter event loop
        update_condition_window.mainloop()

    #recommend to another doctor window function
    def recommend_another_doctor_window():
        # Create a new window for recommending another doctor
        recommend_doctor_window = tk.Toplevel()
        recommend_doctor_window.title("Recommend Another Doctor")
        recommend_doctor_window.geometry("300x250")  #width and height

        # Function to recommend another doctor
        def recommend_doctor():
            patient_id = patient_id_entry.get()  # get patient ID 
            current_doctor_id = current_doctor_id_entry.get()  # get current doctor ID 
            new_doctor_id = new_doctor_id_entry.get()  # get new doctor ID
            # Call the remove_patient_for_specific_doctor_queue and add_patient_for_specific_doctor_queue methods with the provided input
            if hospital.remove_patient_for_specific_doctor_queue(current_doctor_id, patient_id):
                if hospital.add_patient_for_specific_doctor_queue(patient_id, new_doctor_id):
                    result_label.config(text="Patient transferred successfully to Doctor with ID " + new_doctor_id +
                                            "\nRemoved from first doctor queue and added to the next doctor queue.")
                else:
                    result_label.config(text="Failed to transfer patient.")
            else:
                result_label.config(text="Patient not found or not assigned to the current doctor.")

        #input patient ID
        patient_id_label = tk.Label(recommend_doctor_window, text="Enter Patient ID:")
        patient_id_label.pack()
        patient_id_entry = tk.Entry(recommend_doctor_window)
        patient_id_entry.pack()

        #input current doctor ID
        current_doctor_id_label = tk.Label(recommend_doctor_window, text="Enter Current Doctor ID:")
        current_doctor_id_label.pack()
        current_doctor_id_entry = tk.Entry(recommend_doctor_window)
        current_doctor_id_entry.pack()

        #input new doctor ID
        new_doctor_id_label = tk.Label(recommend_doctor_window, text="Enter New Doctor ID:")
        new_doctor_id_label.pack()
        new_doctor_id_entry = tk.Entry(recommend_doctor_window)
        new_doctor_id_entry.pack()

        # Button to recommend another doctor
        recommend_button = tk.Button(recommend_doctor_window, text="Recommend Doctor", command=recommend_doctor)
        recommend_button.pack()

        result_label = tk.Label(recommend_doctor_window, text="")
        result_label.pack()

        # Run the Tkinter event loop
        recommend_doctor_window.mainloop()

    #prescription menu function
    def prescription_menu():
        # Create a new window for Prescription submenu
        prescription_window = tk.Toplevel()
        prescription_window.title("Prescription")
        prescription_window.geometry("400x400")   #width and height

        # Function to handle prescription submission
        def submit_prescription():
            patient_id = patient_id_entry.get()  # get patient ID 
            medication = medication_entry.get()  # get medication 
            dosage = dosage_entry.get()          # get dosage 
            duration = duration_entry.get()      # get duration 
            notes = notes_entry.get()            # get notes 
            doctor_id = doctor_id_entry.get()    # get doctor ID 
            doctor_name = doctor_name_entry.get() # get doctor name 

            #dictionary to store information
            prescription_info = {
                "medication": medication,
                "dosage": dosage,
                "duration": duration,
                "notes": notes
            }

            # Call give_prescription method 
            prescription_id = hospital.give_prescription(patient_id, prescription_info, doctor_id, doctor_name)
            result_label.config(text="Prescription added successfully. Prescription ID: " + str(prescription_id))


        #input patient ID
        patient_id_label = tk.Label(prescription_window, text="Enter Patient ID:")
        patient_id_label.pack()
        patient_id_entry = tk.Entry(prescription_window)
        patient_id_entry.pack()

        #input medication
        medication_label = tk.Label(prescription_window, text="Enter Medication:")
        medication_label.pack()
        medication_entry = tk.Entry(prescription_window)
        medication_entry.pack()

        #input dosage
        dosage_label = tk.Label(prescription_window, text="Enter Dosage:")
        dosage_label.pack()
        dosage_entry = tk.Entry(prescription_window)
        dosage_entry.pack()

        #input duration
        duration_label = tk.Label(prescription_window, text="Enter Duration:")
        duration_label.pack()
        duration_entry = tk.Entry(prescription_window)
        duration_entry.pack()

        #input notes
        notes_label = tk.Label(prescription_window, text="Enter Notes:")
        notes_label.pack()
        notes_entry = tk.Entry(prescription_window)
        notes_entry.pack()

        #input doctor ID
        doctor_id_label = tk.Label(prescription_window, text="Enter Doctor ID:")
        doctor_id_label.pack()
        doctor_id_entry = tk.Entry(prescription_window)
        doctor_id_entry.pack()

        #input doctor ID
        doctor_name_label = tk.Label(prescription_window, text="Enter Doctor Name:")
        doctor_name_label.pack()
        doctor_name_entry = tk.Entry(prescription_window)
        doctor_name_entry.pack()

        # Button to submit prescription
        submit_button = tk.Button(prescription_window, text="Submit Prescription", command=submit_prescription)
        submit_button.pack()

        result_label = tk.Label(prescription_window, text="")
        result_label.pack()

        # Run the Tkinter event loop
        prescription_window.mainloop()

    # Function to handle Manage Consultation submenu
    def manage_consultation_menu():
        # Create a new window for Manage Consultation submenu
        manage_consultation_window = tk.Toplevel(root)
        manage_consultation_window.title("Manage Consultation")
        manage_consultation_window.geometry("500x170")  #width and height

        #choices options
        choices = [
            "Update Patient Condition",
            "Recommend Another Doctor (Transfer)",
            "Give Prescription",
            "Exit"
        ]
        #used loop to print choices
        for option in choices:
            if option == "Update Patient Condition":
                button = tk.Button(manage_consultation_window, text=option, width=40, height=1, command=update_patient_condition_window)
            elif option == "Recommend Another Doctor (Transfer)":
                button = tk.Button(manage_consultation_window, text=option, width=40, height=1, command=recommend_another_doctor_window)
            elif option == "Give Prescription":
                button = tk.Button(manage_consultation_window, text=option, width=40, height=1, command=prescription_menu)
            elif option == "Exit":
                button = tk.Button(manage_consultation_window, text=option, width=40, height=1, command=manage_consultation_window.destroy)
            else:
                button = tk.Button(manage_consultation_window, text=option, width=40, height=1)
            button.pack(pady=2)

    # view all prescription function
    def view_all_prescriptions():
        all_prescriptions = hospital.view_all_prescriptions_for_all_doctors()
        display_prescriptions(all_prescriptions)

    # view prescription by patient id window function
    def view_prescription_by_patient_id_window():
        input_window = tk.Toplevel(root)
        input_window.title("View Prescription by Patient ID")

        #input patient ID
        label = tk.Label(input_window, text="Enter Patient ID:")
        label.pack(pady=5)

        entry = tk.Entry(input_window)
        entry.pack(pady=5)

        #add button to press it for save
        button = tk.Button(input_window, text="Submit", command=lambda: fetch_prescriptions_by_patient_id(entry.get(), input_window))
        button.pack(pady=5)

    #get prescription by patient id
    def fetch_prescriptions_by_patient_id(patient_id, input_window):
        prescriptions = hospital.view_prescription_by_patient_id(patient_id)
        if prescriptions:
            display_prescriptions(prescriptions)
        else:
            messagebox.showinfo("No Prescriptions Found", "No prescriptions found for Patient ID: {}".format(patient_id))
        input_window.destroy()

    #view prescription by doctor id function window
    def view_prescription_by_doctor_id_window():
        input_window = tk.Toplevel(root)
        input_window.title("View Prescription by Doctor ID")

        #input doctor ID
        label = tk.Label(input_window, text="Enter Doctor ID:")
        label.pack(pady=5)

        entry = tk.Entry(input_window)
        entry.pack(pady=5)

        #add button to submit
        button = tk.Button(input_window, text="Submit", command=lambda: fetch_prescriptions_by_doctor_id(entry.get(), input_window))
        button.pack(pady=5)

    #give prescripton bu enter doctor ID
    def fetch_prescriptions_by_doctor_id(doctor_id, input_window):
        prescriptions = hospital.view_prescription_by_doctor_id(doctor_id)
        if prescriptions:
            display_prescriptions(prescriptions)
        else:
            messagebox.showinfo("No Prescriptions Found", "No prescriptions found for Doctor ID: {}".format(doctor_id))
        input_window.destroy()

    # Display all prescriptions
    def display_prescriptions(prescriptions):
        display_window = tk.Toplevel(root)
        display_window.title("Prescriptions")
        display_window.geometry("500x400")  #width and height

        text_widget = tk.Text(display_window)
        text_widget.pack(pady=10, padx=10)

        #used loop to print prescripiton details
        for prescription in prescriptions:
            text_widget.insert("end", "Prescription ID: {}\n".format(prescription["id"]))
            text_widget.insert("end", "Doctor ID: {}\n".format(prescription["doctor_id"]))
            text_widget.insert("end", "Doctor Name: {}\n".format(prescription["doctor_name"]))
            text_widget.insert("end", "Medication: {}\n".format(prescription["medication"]))
            text_widget.insert("end", "Dosage: {}\n".format(prescription["dosage"]))
            text_widget.insert("end", "Duration: {}\n".format(prescription["duration"]))
            text_widget.insert("end", "Notes: {}\n\n".format(prescription["notes"]))

    # function to manage menu
    def prescription_submenu():
        prescription_submenu_window = tk.Toplevel(root)
        prescription_submenu_window.title("Prescription Submenu")
        prescription_submenu_window.geometry("400x300")  #width and height

        #options for users lists
        choices = [
            "View All Prescriptions for All Doctors",
            "View Prescription by Patient ID",
            "View Prescription by Doctor ID",
            "Exit"
        ]

        for index, option in enumerate(choices, start=1):
            button = tk.Button(prescription_submenu_window, text=option, width=40, height=2, command=lambda opt=option: handle_prescription_submenu_option(opt))
            button.pack(pady=5)

    # Prescription Menu Options
    def handle_prescription_submenu_option(option):
        if option == "View All Prescriptions for All Doctors":
            view_all_prescriptions()
        elif option == "View Prescription by Patient ID":
            view_prescription_by_patient_id_window()
        elif option == "View Prescription by Doctor ID":
            view_prescription_by_doctor_id_window()
        elif option == "Exit":
            exit_application()

    # Function to exit the application
    def exit_application():
        root.destroy()

    # Main application window
    root = tk.Tk()
    root.title("Hospital System")
    root.geometry("600x400")  # width and height

    # Create and place tkinter widgets for the main menu
    label = tk.Label(root, text="Hospital System", font=("Arial", 16))
    label.pack(pady=10)

    # Choices of main menu option
    choices = ["Hospital Management", "Manage Consultation", "Prescription", "Exit"]
    for index, choice in enumerate(choices, start=1):
        button = tk.Button(root, text=choice, width=40, height=2, command=lambda ch=str(index): handle_choice(ch))
        button.pack(pady=5)

    # Start the main event loop
    root.mainloop()