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
        cost_center = df_un['مرکز هزینه'].item()
        employee_id = df_un['شماره پرسنلی'].item()
        insurance_type = df_un['نوع بیمه'].item()
        insurance_number = df_un['شماره بیمه'].item()
        employment_date = df_un['تاریخ استخدام'].item()
        date_of_birth = df_un['تاریخ تولد'].item()
        place_of_birth = df_un['محل تولد'].item()
        first_name = df_un['نام'].item()
        last_name = df_un['نام خانوادگی'].item()
        employer_name = first_name + " " + last_name
        national_id = df_un['شماره شناسنامه'].item()
        father_name = df_un['نام پدر'].item()
        national_code = df_un['کد ملی'].item()
        postal_code = df_un['کد پستی'].item()
        telephone = df_un['تلفن'].item()
        mobile = df_un['تلفن همراه'].item()
        education_degree = df_un['مدرک تحصیلی'].item()
        field_of_study = df_un['رشته تحصیلی'].item()
        address = df_un['آدرس'].item()
        gender = df_un['جنسیت'].item()
        job_description = df_un['شرح شغل'].item()
        job_code = df_un['کد شغل'].item()
        contract_duration = df_un['مدت قرارداد(ماه)'].item()
        monthly_base_salary = df_un['حقوق پایه ماهانه'].item()
        daily_base_salary = df_un['حقوق پایه روزانه'].item()
        hourly_base_salary = df_un['حقوق پایه هر ساعت'].item()
        recruitment_bonus = df_un['حق جذب'].item()
        housing_allowance = df_un['حق مسکن'].item()
        child_allowance = df_un['حق اولاد'].item()
        food_and_weather_allowance = df_un['بن و خواروبار'].item()
        weather_disability = df_un['بدی آب و هوا'].item()
        mission_allowance = df_un['حق ماموریت'].item()
        bonus = df_un['پاداش'].item()
        insured = df_un['مشمول بیمه'].item()
        worker_share = df_un['سهم کارگر'].item()
        employer_share = df_un['سهم کارفرما'].item()
        two_thirds_exemption = df_un['معافیت دو هفتم'].item()
        seniority = df_un['سنوات'].item()
        supervisor_allowance = df_un['حق سرپرستی'].item()
        supplementary_insurance = df_un['بیمه تکمیلی'].item()
        unemployment_insurance = df_un['بیمه بیکاری'].item()
        termination_date = df_un['تاریخ ترک کار'].item()
        st.header("نمونه قرارداد كار")
        contract = f'''
    اين قرارداد به موجب ماده (10) قانون كار جمهوري اسلامي ايران بين كارفرما /نماينده قانوني كارفرما و كارگر منعقد مي شود.
    1)مشخصات طرفين: 
    
    كارفرما/ نماينده قانوني كارفرما :
    
    آقاي/خانم/شركت  ...........................
    
    فرزند  ........................... 
     
    شماره شناسنامه/شماره ثبت: .......................................................................     به نشاني:...............................................................................................................................................................................................................
    
    و كارگر آقاي/خانم {first_name} {last_name}  
          
    فرزند : {father_name}         , متولد : {date_of_birth}         ,  شماره شناسنامه : {national_id} 
   
     شماره ملي :{national_code} ,  ميزان تحصيلات {education_degree} ,  نوع و ميزان مهرات: {job_description} 
  
     به نشاني   {address}   منعقد مي گردد.

    2) نوع قرارداد               دائم □                 موقت □              كار معين□

    3)نوع كار يا حرفه يا حجم كار يا وظيفه اي كه كارگر به آن اشتغال مي‌‌يابد: {job_description}

    4) محل انجام كار: 

    5)تاريخ انعقاد قرارداد: 1403/01/01

    6) مدت قرارداد: {contract_duration}

    7) ساعت كار: 42 ساعت
    ميزان ساعت كار و ساعت شروع و پايان آن با توافق طرفين تعيين مي‌گردد، ساعت كار نمي تواند بيش از ميزان مندرج در قانون كار تعيين شود ليكن كمتر از آن مجاز است.

    8) حق السعي:

   \n الف) مزد ثابت / مبنا روزانه/ ساعتي  : {'{:,}'.format(hourly_base_salary)} ريال.
    \nب) حق مسكن ماهيانه  : {'{:,}'.format(housing_allowance)} ريال.
    \nج) حق اولاد ماهيانه : {'{:,}'.format(child_allowance)} ريال.
    \nد) پايه سنوات روزانه : {'{:,}'.format(seniority)} ريال.
    \nه) كمك هزنه اقلام مصرفي خانوار (بن كارگري)ماهيانه : {'{:,}'.format(food_and_weather_allowance)} ريال.
    \nو) ساير مزايا:  ريال




    محل امضا كارفرما                                                                           محل امضا كارگر

    9) حقوق و مزايا: حقوق و مزايا بصورت هفتگي / ماهانه كارگر به حساب شماره ............................... نزد بانك........................... شعبه ............ توسط كارفرما يا نماينده قانوني وي پرداخت مي گردد.

    10)بيمه: به موجب ماده 148 قانون كار كارفرمايان كارگاه هاي مشمول اين قانون مكلفند بر اساس قانون تامين اجتماعي نسبت به بيمه نمودن كارگران واحد خود اقدام نمايند.

    11) عيدي و پاداش سالانه: به موجب ماده واحده قانون مربوط به تعيين عيدي و پاداش سالانه كارگران شاغل در كارگاه‌هاي مشمول قانون كار مصوب 6/12/1370 مجلس شوراي اسلامي به ازاي يك سال كار معادل شصت روز مزد ثابت/مبنا (تاسقف نود روز حداقل مزد روزانه قانوني كارگران) به عنوان عيدي و پاداش سالانه به كارگر پرداخت مي شود. براي كار كمتر از يك سال ميزان عيدي و پاداش و سقف مربوط به نسبت محاسبه خواهد شد.

    12) حق سنوات يا مزاياي پايان كار: به استناد ماده 24 قانون كار در صورت خاتمه قراردادكار، كار معين  يا مدت موقت، كارفرما مكلف است به كارگري كه مطابق قرارداد يكسال يا بيشتر، به كار اشتغال داشته است براي هر سال سابقه، اعم از متوالي يا متناوب  بر اساس آخرين حقوق مبلغي معادل يك ماه حقوق به عنوان مزاياي پايان كار(حق سنوات) به وي پرداخت نمايد.

    13) فسخ قرارداد: به استناد ماده 25 قانون كار و تبصره آن در قرارداد كار موقت و يا براي انجام كار معين هيچ يك از طرفين به تنهايي حق فسخ آن را ندارند و رسيدگي به اختلافات ناشي از اين نوع قرارداد در صلاحيت هيات‌هاي تشخيص و حل اختلاف مي باشد.

    14) ساير: ساير موضوعات مندرج در قانون كار و مقررات تبعي از جمله مرخصي استحقاقي نسبت به اين قرارداد اعمال خواهد شد.

    15) اين قرارداد در 4 نسخه تنظيم مي شود كه يك نسخه نزد كارفرما يك نسخه نزد كارگر يك نسخه به تشكل كارگري (در صورت وجود) و يك نسخه نيز توسط كارفرما به اداره تعاون كار و رفاه اجتماعي محل تحويل مي شود.




    محل امضاي كارفرما                                                                            محل امضاي كارگر
    '''
        st.write(contract)


        