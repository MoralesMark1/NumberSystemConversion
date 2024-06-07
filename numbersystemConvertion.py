isContinue = True

def ConvertDecimalValue(decimalValue):
    baseNumber = {"OCTAL": 8, "HEXADECIMAL": 16, "BINARY": 2}
    values = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    
    
    print(10*'#' + " Convertion Result " + '#'*11)
    for currentBase in baseNumber:
        
        baseNum = baseNumber[currentBase]
        
        convertedValue = ""
            
        currentValue = decimalValue
            
        while currentValue != 0:
            result = currentValue / baseNum
            fractionalValue = result % 1
            #print(fractionalValue)
                
            remainder = int(fractionalValue * baseNum)
            remainder = values[remainder]
            
            convertedValue += str(remainder)
                
            currentValue = int(result)
        
        # Reverse the value to align the correct value
        convertedValue = convertedValue[::-1]
        
        print(f"| {currentBase:<13} | {convertedValue:>20} |")



while True:
    try:
        decimalValue = int(input("Input Decimal Number: "))        
        ConvertDecimalValue(decimalValue)
    except ValueError:
      print("Invalid input. Please enter an integer only.")
         
 