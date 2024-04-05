list1 = [{"Name": "Jack","Age": 20},{"Name": "Ryan","Age": 22},{"Name": "Mike","Age": 18},{"Name": "Eva","Age": 28}]

start_e = list(filter(lambda person: person["Name"].startswith("E"),list1))
print(start_e)

more_20 = list(filter(lambda person: person["Age"] > 20, list1))
print(more_20)