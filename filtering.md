filter = {}
filter["type"] = "And"
filter["filters"] = []
filter1={}
filter1["type"] = "Contains"
filter1["name"] = "name"
filter1["value"] = "Pod02"
print(filter1)
filter["filters"].append(filter1)machines = obj.get_machines(maxpagesize=1, filter = filter)