import streamlit as st  
import pandas as pd

st.markdown("""<style>body { direction: rtl; }</style>""", unsafe_allow_html=True)
sample = pd.read_csv('person.csv')

def convert_df(df):

    # IMPORTANT: Cache the conversion to prevent computation on every rerun

    return df.to_csv().encode('utf-8')


csv = convert_df(sample)
#adding a download button to download csv file

st.download_button( 

    label="Download data as CSV",

    data=csv,

    file_name='sample_df.csv',

    mime='text/csv',

)


file = st.file_uploader("Upload File", type=["xlsx", "xls"])






if file:
    df = pd.read_excel(file)
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
        supervisor_allowance = str(df_un['حق سرپرستی'].item())
        supplementary_insurance = str(df_un['بیمه تکمیلی'].item())
        unemployment_insurance = str(df_un['بیمه بیکاری'].item())
        termination_date = str(df_un['تاریخ ترک کار'].item())
        st.header("نمونه قرارداد كار")
        # Path to the HTML file
        html_file_path = './empolye.html'

        # Read the contents of the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        # Replace placeholders in the HTML content
        print("Last Name:", last_name)
        print("First Name:", first_name)
        print("National Code:", national_code)
        print("Father Name:", father_name)
        print("Address:", address)
        print("Mobile:", mobile)

        html_content = html_content.replace("first_name", first_name)
        html_content = html_content.replace("national_code", national_code)
        html_content = html_content.replace("father_name", father_name)
        html_content = html_content.replace("address",address)
        html_content = html_content.replace("mobile", mobile)
        html_content = html_content.replace("last_name", last_name)
        html_content = html_content.replace("hourly_base_salary", "{:,.0f}".format(float(hourly_base_salary)))
        html_content = html_content.replace("housing_allowance", "{:,.0f}".format(float(housing_allowance)))
        html_content = html_content.replace("child_allowance", "{:,.0f}".format(float(child_allowance)))
        html_content = html_content.replace("seniority", "{:,.0f}".format(float(seniority)))
        html_content = html_content.replace("food_and_weather_allowance", "{:,.0f}".format(float(food_and_weather_allowance)))

    
        # Display the HTML content
        # st.components.v1.html(html_content, width=1200, height=5000) 
        st.markdown(html_content, unsafe_allow_html=True)
   
