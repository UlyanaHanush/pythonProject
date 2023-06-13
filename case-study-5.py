'''
1.Read file bank-data.csv
2.Build a set of unique jobs
3.Read the input from command line –profession
4.Check if professionis in list
5.Print whetherclient is eligible
'''
'''
1.Compute max and min age for loan eligibility based on data in csv file
2.Store max and min age in dictionary
3.Make the profession check case insensitive
4.Currently program ends after the check. Take the input in whileloop and end only ifuser types "END" for profession
'''
job = set()
age = []
dict_age = {}
with open('bank-data.csv', 'r') as f:
    for line in f:
        if line.split(',')[1]!='job':
            job.add(line.split(',')[1])
            age.append(line.split(',')[0])
print(job)
# print(age)
dict_age['min'] = min(age)
dict_age['max'] = max(age)
print(dict_age)
while True:
    job_new = input('input job or END: ')
    if job_new == 'END':
        break
    elif job_new.lower() in job:
        print('client is eligible')
    else:
        print("client isn't eligible")
