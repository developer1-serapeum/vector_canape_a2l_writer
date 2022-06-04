from spreadsheetwriter import SpreadSheetWriter
from spreadsheetreader import SpreadSheetReader
import re

###############################################################################
### Subroutines used in the main program                                    ### 
###############################################################################

REGEX_LIST = {
    'parameter_start': r"/begin CHARACTERISTIC (.+) \"",
    'parameter_end' : r"/end CHARACTERISTIC",
    'value': r".\sVALUE (0x.+) __",
    'symbol_link': r".\sSYMBOL_LINK \"(.+)\" ",
    'extended_limits': r".\sEXTENDED_LIMITS (.+) (.+)",
    'format': r".\sFORMAT \"(.+)\"",
}

def compareSmiWithA2L():
    pass

def findByRegex(line, regex):
    """
    Gets a line and a regular expression with specificed group between
    brackets(), then it will return the found group if any
    """
    pattern = re.compile(REGEX_LIST[regex])
    for match in re.finditer(pattern, line):
        #print(regex, ":", match.group(1))
        #if(match.lastindex == 2):
        #    print(regex, ":", match.group(2))
    
        return match.groups()
    
def getParametersA2L():
    """
    Read all the parameters in an A2L file and return their number
    """
    file_in = 'sample.a2l'

    match_count = 0
    found_instances = []
    parameter = {}
    
    parameter_line = False

    for line in open(file_in):
    
        # Find start of a parameter    
        parameter_start = findByRegex(line, 'parameter_start')    
        if (parameter_start != None):
        
            parameter['name'] = parameter_start[0]
            #print("Name : ", parameter_start[0])

            parameter_line = True
            match_count += 1
            #print("==> Parameter Start <==")
            

        if (parameter_line == True):
            # Get the information about the parameter
            value = findByRegex(line, 'value')
            if(value != None):
                parameter['value'] = value[0]
                #print("value: ", value[0])
            
            symbol_link = findByRegex(line, 'symbol_link')
            if(symbol_link != None):
                parameter['symbol_link'] = symbol_link[0]
                #print("symbol_link: ", symbol_link[0])
            
            extended_limits = findByRegex(line, 'extended_limits')
            if(extended_limits != None):
                parameter['extended_limits_low'] = extended_limits[0]
                parameter['extended_limits_high'] = extended_limits[1]
                #print("extended_limits_low: ", extended_limits[0])
                #print("extended_limits_high: ", extended_limits[1])

            parameter_format = findByRegex(line, 'format')
            if(parameter_format != None):
                parameter['format'] = parameter_format[0]
                #print("format: ",parameter_format[0])
            
        # Find end of a parameter
        parameter_end = findByRegex(line, 'parameter_end') 
        if (parameter_end != None):
            parameter_line = False
            found_instances.append(parameter)
            parameter = {}
            #print("*** Parameter End ***")
    
    return found_instances

###############################################################################
### The Main Program                                                        ### 
###############################################################################

if __name__ == "__main__":

    #reader = SpreadSheetReader()
    #reader.readParameter("./SMI_.xlsx", "Inputs", "V_VehicleSpeed")

    parameters = getParametersA2L()

    for parmeter in parameters:
        print(parmeter)

    print("A2L parameters count = ({}) times".format(len(parameters)))