import yaml 
with open('test.yaml','r') as file: 
    prime_service = yaml.safe_load(file)
print(prime_service)
