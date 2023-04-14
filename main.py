from function import calculate_express
input_weight = input("Input weight: ")
try:
    try:
        input_weight = int(input_weight)
    except:
        input_weight = float(input_weight)
except:
    input_weight = str(input_weight)
input_zone = input("Input zone: ")
result = calculate_express(input_weight,input_zone)
print(result)