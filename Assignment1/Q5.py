
def processString(input_str): 
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric(): 
            # output_str += char * 2
            output_str += char
        else:
            output_str += char.upper()
    return output_str

test = ["abcdefG1", "CCDDEExy", "1234567b", "8665"]

for item in test: 
    print("Input: " + item)
    output = processString(item)
    print("Output: " + output)