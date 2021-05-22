import json
import pickle
import numpy as np

__location = None
__dataColumns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __dataColumns.index(location.lower())
    except:
        loc_index = -1


    x = np.zeros(len(__dataColumns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0],2)


def get_location_names():
    return __location

def load_saved_artifacts():
    print("Loading saved artifacts.....Start")
    global __location
    global __dataColumns
    
    with open("./artifacts/columns.json",'r') as f:
        __dataColumns = json.load(f)['data_columns']
        __location = __dataColumns[3:]
    
    global __model
    with open("./artifacts/bangluru_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    
    print("Loading saved artifacts.... DONE!!!")

if __name__ == "__main__":
    load_saved_artifacts()
    #print(get_location_names())
    print(get_estimated_price('1st block jayanagar',1000,2,2))
    print(get_estimated_price('bisuvanahalli',2000,3,2))
