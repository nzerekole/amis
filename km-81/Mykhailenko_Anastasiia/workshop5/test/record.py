class Record:
    def __init__(self, data):
        self.met_code = data['MET_CODE']
        self.exp_type = data['EXP_TYPE']
        self.met_n = data['MET_NAME']
        self.year = data['YEAR']
        self.register_date = data['REGISTER_DATE']