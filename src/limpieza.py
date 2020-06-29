def companiesMongo(country_code):
    query = {"offices.country_code":f"{country_code}",
        "category_code":{"$in": ["web", "games_video","ecommerce","mobile","social","software"]},
        }
    projection ={"offices":1, "name":1, "founded_year":1,"total_money_raised":1,"category_code":1}
    res = list(db.companies.find(query,projection))
    return res