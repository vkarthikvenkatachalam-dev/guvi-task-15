import  pandas as pd

def test_read_data_from_excel():
    df=pd.read_excel("my_files/login_data.xlsx")
    print(df)
