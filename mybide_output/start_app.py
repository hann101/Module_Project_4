import os
  
path = os.getcwd()
print(path)


os.system('cd {}'.format(path))
# os.system('set FLASK_APP=pybo')
os.environ["FLASK_APP"] = "policy"
os.environ["FLAKS_ENV"] = "development"

os.system('flask run --host=0.0.0.0')