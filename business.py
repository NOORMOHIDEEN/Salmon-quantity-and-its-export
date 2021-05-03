import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Year'].tolist())

    year = df['Year'].tolist()

    SalmonQuantity_data = df['SalmonQuantity'].tolist()

    Expo_data = df['Expo'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
        'year'            : year,
        'SalmonQuantity'  : SalmonQuantity_data,
        'Expo' : Expo_data
    }

    # print(result_dict)

    return result_dict

def add_row(year, SalmonQuantity,Expo ):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Year'       : year, 
        'SalmonQuantity'  : SalmonQuantity,
        'Expo' : Expo 
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()