from DataSet.parser import parse_dataset

dataset = parse_dataset()
for record in dataset:
    print(record.met_name)
