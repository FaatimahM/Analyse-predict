def extract_municipality_hashtags(df):
    import numpy as np
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}
    #Municipality column
    muni_list = []
    flag = 0
    count = 1
    for i in df['Tweets']:
        for keys in mun_dict.keys():
            if keys in i:
                muni_list.append(mun_dict[keys])
                flag += 1
        if flag == count:
            count += 1
        else:
            muni_list.append(np.nan)
    df['municipality'] = muni_list
    
    #Hashtag column
    # create a list: hash_list
    hash_list = []
    for i in df['Tweets']:
        # create a list: spl_str & innerlist
        spl_str = []
        innerlist = []
        flag = 0
        spl_str = i.split()
        for var in spl_str:
            if var[0] == '#':
                innerlist.append(var.lower())
                flag += 1
        if flag != 0:
            hash_list.append(innerlist)
        else:
            hash_list.append(np.nan)
    df['hashtags'] = hash_list
    return df 