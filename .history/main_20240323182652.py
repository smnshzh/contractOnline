import streamlit as st  
import pandas as pd
import os
from docx import Document
from html2docx import html2docx
import io
from spire.doc import *
from spire.doc.common import *
import random
import os

column_mapping = {
                    'وضعیت تاهل':'marital_status',
                    'مرکز هزینه': 'cost_center',
                    'شماره پرسنلی': 'employee_id',
                    'نوع بیمه': 'insurance_type',
                    'شماره بیمه': 'insurance_number',
                    'تاریخ استخدام': 'employment_date',
                    'تاریخ تولد': 'date_of_birth',
                    'محل تولد': 'place_of_birth',
                    'نام': 'first_name',
                    'نام خانوادگی': 'last_name',
                    'شماره شناسنامه': 'national_id',
                    'نام پدر': 'father_name',
                    'کد ملی': 'national_code',
                    'کد پستی': 'postal_code',
                    'تلفن': 'telephone',
                    'تلفن همراه': 'mobile',
                    'مدرک تحصیلی': 'education_degree',
                    'رشته تحصیلی': 'field_of_study',
                    'آدرس': 'address',
                    'جنسیت': 'gender',
                    'شرح شغل': 'job_description',
                    'کد شغل': 'job_code',
                    'مدت قرارداد(ماه)': 'contract_duration',
                    'حقوق پایه ماهانه': 'monthly_base_salary',
                    'حقوق پایه روزانه': 'daily_base_salary',
                    'حقوق پایه هر ساعت': 'hourly_base_salary',
                    'حق جذب': 'recruitment_bonus',
                    'حق مسکن': 'housing_allowance',
                    'حق اولاد': 'child_allowance',
                    'بن و خواروبار': 'food_and_weather_allowance',
                    'بدی آب و هوا': 'weather_disability',
                    'حق ماموریت': 'mission_allowance',
                    'پاداش': 'bonus',
                    'مشمول بیمه': 'insured',
                    'سهم کارگر': 'worker_share',
                    'سهم کارفرما': 'employer_share',
                    'معافیت دو هفتم': 'two_thirds_exemption',
                    'سنوات': 'seniority',
                    'حق سرپرستی': 'supervisor_allowance',
                    'بیمه تکمیلی': 'supplementary_insurance',
                    'بیمه بیکاری': 'unemployment_insurance',
                    'تاریخ ترک کار': 'termination_date',
                    'تعداد فرزند':'child_number',
                    'تاریخ شروع قرارداد':'cstart',
                    'تاریخ پایان قرارداد' : 'cend'

                        }






def delete_files_in_folder(folder_path):
    # بررسی وجود فولدر
    if not os.path.exists(folder_path):
        print("فولدر موجود نیست.")
        return
    
    # باز کردن فولدر و حذف تمامی فایل‌ها
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                delete_files_in_folder(file_path)
        except Exception as e:
            print(f"خطا در حذف {file_path}: {e}")

def download_file(file_path, file_name):
    with open(file_path, "rb") as file:
        data = file.read()
    st.download_button(
        label=file_name,
        data=data,
        file_name=file_name,
        mime="application/octet-stream",
        key = file_path
    )

st.markdown("""<style>body { direction: rtl; }</style>""", unsafe_allow_html=True)
# Sidebar title
st.sidebar.header('CM Options')

# Add a radio button to the sidebar
selected_option = st.sidebar.radio("Select an option", ["Setting","Option 1", "Option 2", "Option 3"])
if selected_option== "Setting":
    tab1 , tab2 = st.tabs(["add contract","leave comment"])
    with tab1:
     # Create the "contracts" directory if it doesn't exist
        directory = "contracts"
        files = ""
        if directory not in os.listdir():
            os.makedirs(directory, exist_ok=True)
        else:
            # List files in the "contracts" directory
            files = os.listdir(directory)

            # File selector
            selected_file = st.selectbox("Select a file to delete", [""] + files)

            if selected_file:
                if st.button("Delete Selected File"):
                    file_path = os.path.join(directory, selected_file)
                    try:
                        os.remove(file_path)
                        st.write(f"File '{selected_file}' deleted successfully.")
                        # Refresh the list of files after deletion
                        files = os.listdir(directory)
                    except Exception as e:
                        st.write(f"Error deleting file '{selected_file}': {e}")

        # File uploader
        uploaded_file = st.file_uploader("Upload a contract file", type=['html'])

        if uploaded_file is not None:
            if st.button("Upload Contract File"):
                # Save the uploaded file to the "contracts" directory
                file_path = os.path.join(directory, uploaded_file.name)
                with open(file_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                
                st.write(f"File uploaded successfully and saved to: {file_path}")
    with tab2:
        col1 
        st.dataframe(pd.DataFrame({"excel Header":column_mapping.keys(),"html tag":column_mapping.values()}))
if selected_option == "Option 1" :
    download_file('./sample.xlsx','sample.xlsx')
    st.header("ساخت قرارداد بر اساس کد پرسنلی")

    file = st.file_uploader("Upload File", type=["xlsx", "xls"])
    
    if file:
        df = pd.read_excel(file, dtype=str)
        selected_person = st.selectbox("Select Person ID", df['شماره پرسنلی'])
        if selected_person:
            
            st.write(f"Selected person ID: {selected_person}")
            # You can perform further actions based on the selected person ID here
            df_un = df[df['شماره پرسنلی']==selected_person]
            cost_center = str(df_un['مرکز هزینه'].item())
            employee_id = str(df_un['شماره پرسنلی'].item())
            insurance_type = str(df_un['نوع بیمه'].item())
            insurance_number = str(df_un['شماره بیمه'].item())
            employment_date = str(df_un['تاریخ استخدام'].item())
            date_of_birth = str(df_un['تاریخ تولد'].item())
            place_of_birth = str(df_un['محل تولد'].item())
            first_name = str(df_un['نام'].item())
            last_name = str(df_un['نام خانوادگی'].item())
            employer_name = first_name + " " + last_name
            national_id = str(df_un['شماره شناسنامه'].item())
            father_name = str(df_un['نام پدر'].item())
            national_code = str(df_un['کد ملی'].item())
            postal_code = str(df_un['کد پستی'].item())
            telephone = str(df_un['تلفن'].item())
            mobile = str(df_un['تلفن همراه'].item())
            education_degree = str(df_un['مدرک تحصیلی'].item())
            field_of_study = str(df_un['رشته تحصیلی'].item())
            address = str(df_un['آدرس'].item())
            gender = str(df_un['جنسیت'].item())
            job_description = str(df_un['شرح شغل'].item())
            job_code = str(df_un['کد شغل'].item())
            contract_duration = str(df_un['مدت قرارداد(ماه)'].item())
            monthly_base_salary = str(df_un['حقوق پایه ماهانه'].item())
            daily_base_salary = str(df_un['حقوق پایه روزانه'].item())
            hourly_base_salary = str(df_un['حقوق پایه هر ساعت'].item())
            recruitment_bonus = str(df_un['حق جذب'].item())
            housing_allowance = str(df_un['حق مسکن'].item())
            child_allowance = str(df_un['حق اولاد'].item())
            food_and_weather_allowance = str(df_un['بن و خواروبار'].item())
            weather_disability = str(df_un['بدی آب و هوا'].item())
            mission_allowance = str(df_un['حق ماموریت'].item())
            bonus = str(df_un['پاداش'].item())
            insured = str(df_un['مشمول بیمه'].item())
            worker_share = str(df_un['سهم کارگر'].item())
            employer_share = str(df_un['سهم کارفرما'].item())
            two_thirds_exemption = str(df_un['معافیت دو هفتم'].item())
            seniority = str(df_un['سنوات'].item())
            supervisor_allowance = df_un['حق سرپرستی'].item()
            supplementary_insurance = str(df_un['بیمه تکمیلی'].item())
            unemployment_insurance = str(df_un['بیمه بیکاری'].item())
            termination_date = str(df_un['تاریخ ترک کار'].item())
            marital_status = str(df_un['وضعیت تاهل'].item())
            child_number = str(df_un['تعداد فرزند'].item())
            meniority = int(monthly_base_salary)/12
            cstart = str(df_un['تاریخ شروع قرارداد'].item())
            cend = str(df_un['تاریخ پایان قرارداد'].item())
                        # Path to the HTML file
            contract_dir = './contracts'
            contract_list = os.listdir(contract_dir)
            select_contract = st.selectbox(label="نوع قرارداد را انتخاب نمایید", options=contract_list)

            html_file_path = None
            if select_contract:
                html_file_path = os.path.join(contract_dir, select_contract)

            if html_file_path:
                # Perform actions with html_file_path
                # For example, you might want to display the HTML content:
                st.write(f"Selected HTML file path: {html_file_path}")
            else:
                st.write("لطفا یک قرارداد را انتخاب نمایید.")

            # Read the contents of the HTML file
            with open(html_file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            # Replace placeholders in the HTML content
            if gender == "مرد":
                gender = "آقای"
            elif gender == "زن":
                gender = "خانم"

            replacement_dict = {
    'cost_center': cost_center,
    'employee_id': employee_id,
    'insurance_type': insurance_type,
    'insurance_number': insurance_number,
    'employment_date': employment_date,
    'date_of_birth': date_of_birth,
    'place_of_birth': place_of_birth,
    'first_name': first_name,
    'last_name': last_name,
    'employer_name': employer_name,
    'national_id': national_id,
    'father_name': father_name,
    'national_code': national_code,
    'postal_code': postal_code,
    'telephone': telephone,
    'mobile': mobile,
    'education_degree': education_degree,
    'field_of_study': field_of_study,
    'address': address,
    'gender': gender,
    'job_description': job_description,
    'job_code': job_code,
    'contract_duration': contract_duration,
    'monthly_base_salary':"{:,.0f}".format(float(monthly_base_salary)),
    'daily_base_salary': "{:,.0f}".format(float(daily_base_salary)),
    'hourly_base_salary': "{:,.0f}".format(float(hourly_base_salary)),
    'recruitment_bonus': "{:,.0f}".format(float(recruitment_bonus)),
    'housing_allowance': "{:,.0f}".format(float(housing_allowance)),
    'child_allowance': "{:,.0f}".format(float(child_allowance)),
    'food_and_weather_allowance': "{:,.0f}".format(float(food_and_weather_allowance)),
    'weather_disability': "{:,.0f}".format(float(weather_disability)),
    'mission_allowance': "{:,.0f}".format(float(mission_allowance)),
    'bonus': "{:,.0f}".format(float(bonus)),
    'insured': insured,
    'worker_share': worker_share,
    'employer_share': employer_share,
    'two_thirds_exemption': two_thirds_exemption,
    'seniority': seniority,
    'supervisor_allowance': supervisor_allowance,
    'supplementary_insurance': supplementary_insurance,
    'unemployment_insurance': unemployment_insurance,
    'termination_date': termination_date,
    'marital_status':marital_status,
    'child_number':child_number,
    'meniority':"{:,.0f}".format(float(meniority)),  ##سنوات ماهانه به دلیل داشتن کلمات مشابه با سنوات به این شکل نوشته شده است تا در ایگذتری به مشکل نخورد
    'eydi':"{:,.0f}".format(float(meniority*2)),
    'cend' : cend,
    'cstart' : cstart
}
            for placeholder, value in replacement_dict.items():
                
                html_content = html_content.replace(placeholder, value)
            
        
            # Display the HTML content
            # st.components.v1.html(html_content, width=1200, height=5000) 
            st.markdown(html_content, unsafe_allow_html=True)
            # Layout the buttons in a single row
        col1, col2 , col3 = st.columns(3)
        
        # Save as HTML button
        if col1.button("Save as HTML"):
            if not os.path.exists("download"):
                os.makedirs("download")
            with open(f"./download/{employee_id}.txt", "w", encoding="utf-8") as file:
                file.write(html_content)
            st.success("HTML file saved successfully.")

        # Save as Word button
        if col2.button("Save as Word"):
            if not os.path.exists("download"):
                os.makedirs("download")
            doc = Document()
            # Add a section to the document
            sec = doc.AddSection()
            # Add a paragraph to the section
            paragraph = sec.AddParagraph()
            paragraph.AppendHTML(html_content)

            doc.SaveToFile(f"./download/{employee_id}.docx", FileFormat.Docx2016)
            st.success("Word document saved successfully.")
        if col3.button("save as pdf"):
            if not os.path.exists("download"):
                os.makedirs("download")
            doc = Document()
            # Add a section to the document
            sec = doc.AddSection()
            # Add a paragraph to the section
            paragraph = sec.AddParagraph()
            paragraph.AppendHTML(html_content)

            doc.SaveToFile(f"./download/{employee_id}.pdf", FileFormat.PDF)
            

            # Display success message
            st.success("PDF document saved successfully.")
                

if selected_option == "Option 2":
        st.write("دانلود فایل های ساخته شده")
        filepath = os.listdir('./download')
        print(filepath)
        for file in filepath:
            pdf_file_path = os.path.join('./download', file)
            # st.markdown(f'<a href="{pdf_file_path}" download="{file}">Download {file}</a>', unsafe_allow_html=True)
            download_file(pdf_file_path, file)
if selected_option == "Option 3":
   if st.button("Clear Folder"):
        delete_files_in_folder('./download')
        st.success("Folder successfully deleted")