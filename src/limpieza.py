import pandas as pd
from pymongo import MongoClient
import numpy as np

def companiesMongo(country_code):
    """
    Conecta con MongoDb y hace un query de las empresas de un país
    """
    mongodbURL = f"mongodb://localhost/datamad0620"
    client = MongoClient(mongodbURL, connectTimeoutMS=2000, serverSelectionTimeoutMS=2000)
    db = client.get_database("datamad0620")

    query = {"offices.country_code":f"{country_code}",
        "category_code":{"$in": ["web", "games_video","ecommerce","mobile","social","software"]},
        }
    projection ={"offices":1, "name":1, "founded_year":1,"total_money_raised":1,"category_code":1}
    res = list(db.companies.find(query,projection))
    return res


def limipiezaData(companies,code):
    df = pd.DataFrame(list(companies))
    offices = df.explode("offices").apply(lambda e: e.offices,axis=1,result_type="expand")
    clean_offices = pd.concat([df[["name","_id"]], offices], axis=1)
    clean_offices = clean_offices.rename(columns={"_id":"company_id"})
    filtered = clean_offices[(clean_offices['country_code']== f"{code}")]
    return filtered   

def transformToGeoPoint(s):
    """
    Transforma Latitud y Longitud a formato Geopoints
    """
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }
    