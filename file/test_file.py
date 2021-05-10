import re

dictionary = {}
scope=[]
# power_pin={}

def create_root_dictionary(name,**kwargs):
    # print(type(kwargs))
    dictionary[name]=kwargs

def create_power_pin_dict(name, **kwargs):
    power_pin[name]=kwargs
    return power_pin[name]

def create_input_pin_dict(name, **kwargs):
    power_pin[name]=kwargs
    return power_pin[name]
def create_output_pin_dict(name, **kwargs):
    power_pin[name]=kwargs
    return power_pin[name]

def add_cb(list_data):
    for x in list_data:
        scope.append('{')
    return scope

def remove_cb(list_data):
    for x in list_data:
        scope.pop()
    return scope

# inline=open("test_parse.lib",'r')
with open("test_parse.lib","r") as inline:

    line=inline.readline()
    counter = 0
    # print(type(line))
    list1=[]
    while line:
        # print(line)
        line=line.replace(" ", "")
        # print(counter,line)

        # variable declare starts
        name=""
        value=""
        cell_footprint=""
        area=0
        cell_leakage_power=0
        pin_name=""
        # pg_type=""
        # related_bias_pin=""
        # voltage_name=""
        # physical_connection=""
        power_pin={}
        input_pin={}
        output_pin={}

        # variable declare ends
        scope.clear()
        if re.search('cell\(([A-Z0-9_])+\)\{',line):
            scope=add_cb(re.findall("{", line))
            scope=remove_cb(re.findall("}", line))

            counter = counter +1

            name=""
            dct={}
            for x in range(0,len(line),1):
                if line[x] == '(':
                    i=x+1
                    name=""
                    while(line[i]!=')'):
                        name+=line[i]
                        i+=1
                    x=i
                    
            name=(str(counter)+name)
                   
            line=inline.readline()

            while line:
                line=line.replace(" ", "")
                # print(line)
                scope=add_cb(re.findall("{", line))
                scope=remove_cb(re.findall("}", line))
                temp_power_pin={}
                if len(scope)==0:
                    create_root_dictionary(
                        name, cell_footprint=cell_footprint,
                        area=float(area), cell_leakage_power=cell_leakage_power,
                        power_pin=dict(power_pin),input_pin=dict(input_pin),output_pin=dict(output_pin)
                    )
                    power_pin.clear()
                    input_pin.clear()
                    output_pin.clear()
                    break
                if re.search("cell_footprint",line):
                    cell_footprint=re.search("[A-Z0-9]+_[A-Z0-9]+_[A-Z0-9]+",line)
                    cell_footprint=(cell_footprint.group())
                    # print(cell_footprint.group())
                elif re.search("area",line):
                    area=re.search("([0-9])+\.([0-9])+",line)
                    area=float(area.group())
                    # print(area.group())
                elif re.search("cell_leakage_power",line):
                    cell_leakage_power=re.search("([0-9])+\.([0-9])+((e-)*([0-9])+)*",line)
                    cell_leakage_power=float(cell_leakage_power.group())
                elif re.search(r"\bpg_pin",line):
                    while re.search(r"\bpg_pin",line):
                        pin_name=re.search("[A-Z]+", line)
                        pin_name=pin_name.group()

                        line=inline.readline()
                        line=line.replace(" ", "")
                        scope=add_cb(re.findall("{", line))
                        scope=remove_cb(re.findall("}", line))

                        
                        # print(name,':',line)
                        pg_type=related_bias_pin=physical_connection=voltage_name="",
                        while not re.search("}", line):
                            # print(name,':',line)
                            if re.search(r"\bpg_type", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':':
                                        i=x+1
                                        pg_type=""
                                        while(line[i]!=';'):
                                            pg_type+=line[i]
                                            i+=1
                                        x=i

                            elif re.search(r"\brelated_bias_pin", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':':
                                        i=x+1
                                        related_bias_pin=""
                                        while(line[i]!=';'):
                                            related_bias_pin+=line[i]
                                            i+=1
                                        x=i
                            elif re.search(r"\bvoltage_name", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':':
                                        i=x+1
                                        voltage_name=""
                                        while(line[i]!=';'):
                                            voltage_name+=line[i]
                                            i+=1
                                        x=i
                            elif re.search(r"\bphysical_connection", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':':
                                        i=x+1
                                        physical_connection=""
                                        while(line[i]!=';'):
                                            physical_connection+=line[i]
                                            i+=1
                                        x=i
                            line=inline.readline()
                            line=line.replace(" ", "")
                            scope=add_cb(re.findall("{", line))
                            scope=remove_cb(re.findall("}", line))
                            if re.search("}", line):
                                # temp_power_pin=create_power_pin_dict(pin_name,pin_name=pin_name,pg_type=pg_type,
                                # related_bias_pin=related_bias_pin, physical_connection=physical_connection,
                                # voltage_name=voltage_name
                                # )
                                if pin_name=="VDD" or pin_name=="VSS":
                                    temp_power_pin=create_power_pin_dict(pin_name,pin_name=pin_name,pg_type=pg_type,
                                    related_bias_pin=related_bias_pin,
                                    voltage_name=voltage_name
                                    )
                                if pin_name=="VNW" or pin_name=="VPW":
                                    temp_power_pin=create_power_pin_dict(pin_name,pin_name=pin_name,pg_type=pg_type,
                                    physical_connection=physical_connection,
                                    voltage_name=voltage_name
                                    )

                                # print("Line :",line,name,temp_power_pin)
                                # if temp_power_pin["pg_type"]:
                                power_pin[pin_name]=temp_power_pin.copy()
                                break
                        # Insert new data into list
                        # print("Line :",line,name,power_pin)
                        
                        
                        # temp_power_pin.clear()


                        line=inline.readline()
                        line=line.replace(" ", "")
                        scope=add_cb(re.findall("{", line))
                        scope=remove_cb(re.findall("}", line))
                    # print(name,power_pin)
                        # print("Line :",line,name,power_pin)
                
                # check total pin here (Input and Output)
                elif re.search(r"\bpin\([A-Z]\)",line):
                    # print(line)
                    # pass
                    # pin_name=re.search("[A-Z]", line)
                    # pin_name=pin_name.group()
                    # print(pin_name)
                    # print("Size of scope :",len(scope),scope)

                    while re.search(r"\bpin\([A-Z]\)",line):
                        # count+=1
                        pin_name=re.search("[A-Z]", line)
                        pin_name=pin_name.group()
                        # print(name,':', pin_name)
                        # print("Size of scope :",len(scope),scope)

                        line=inline.readline()
                        line=line.replace(" ", "")
                        scope=add_cb(re.findall("{", line))
                        scope=remove_cb(re.findall("}", line))
                        # print(pin_name,len(scope),line)
                        
                        pin_type=pin_function=related_power_pin=related_ground_pin=related_bias_pin="",
                        max_transition=capacitance=rise_capacitance=min_capacitance=max_capacitance=""
                        while len(scope)>=2:
                            # print(pin_name,len(scope),line)
                        # #     # print(name, pin_name,"Size of scope :",len(scope),scope)
                        # #     # print(name,':',line)

                            if re.search(r"\bdirection", line):
                                if re.search("input",line):
                                    pin_type=(re.search("input",line)).group()
                                    # print(name, pin_name, pin_type)
                                elif re.search("output",line):
                                    pin_type=(re.search("output",line)).group()
                                    # print(name, pin_name, pin_type)
                            elif re.search(r"\bfunction",line):
                                # print(name,line)
                                pin_function=re.search("!*[A_Z]+(!*[A-Z]*)*",line)
                                pin_function=pin_function.group()
                                # print(name,pin_type,pin_function)
                            elif re.search(r"\brelated_power_pin", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':' and line[x+1]=="\"":
                                        i=x+2
                                        related_power_pin=""
                                        while(line[i]!='\"'):
                                            related_power_pin+=line[i]
                                            i+=1
                                        x=i
                            elif re.search(r"\brelated_ground_pin", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':' and line[x+1]=="\"":
                                        i=x+2
                                        related_ground_pin=""
                                        while(line[i]!='\"'):
                                            related_ground_pin+=line[i]
                                            i+=1
                                        x=i
                            elif re.search(r"\brelated_bias_pin", line):
                                for x in range(0,len(line),1):
                                    if line[x] == ':' and line[x+1]=="\"":
                                        i=x+2
                                        related_bias_pin=""
                                        while(line[i]!='\"'):
                                            related_bias_pin+=line[i]
                                            i+=1
                                        x=i
                            elif re.search(r"\bmax_transition", line):
                                if re.search("[0-9]+(\.[0-9]+)*",line):
                                    max_transition=re.search("[0-9]+(\.[0-9]+)*",line).group()
                            elif re.search(r"\bcapacitance", line):
                                if re.search("[0-9]+(\.[0-9]+)*",line):
                                    capacitance=re.search("[0-9]+(\.[0-9]+)*",line).group()
                            elif re.search(r"\brise_capacitance", line):
                                if re.search("[0-9]+(\.[0-9]+)*",line):
                                    rise_capacitance=re.search("[0-9]+(\.[0-9]+)*",line).group()
                            elif re.search(r"\bfall_capacitance", line):
                                if re.search("[0-9]+(\.[0-9]+)*",line):
                                    fall_capacitance=re.search("[0-9]+(\.[0-9]+)*",line).group()
                            elif re.search(r"\bmin_capacitance", line):
                                if re.search("[0-9]+\.[0-9]+([e-]*[0-9]+)*",line):
                                    min_capacitance=re.search("[0-9]+\.[0-9]+([e-]*[0-9]+)*",line).group()
                            elif re.search(r"\bmax_capacitance", line):
                                if re.search("[0-9]+\.[0-9]+([e-]*[0-9]+)*",line):
                                    max_capacitance=re.search("[0-9]+\.[0-9]+([e-]*[0-9]+)*",line).group()

                            
                            
                            line=inline.readline()
                            line=line.replace(" ", "")
                            scope=add_cb(re.findall("{", line))
                            scope=remove_cb(re.findall("}", line))
                            
                            # print(name,pin_name,len(scope),line)

                            # print("Exit from pin :",pin_name,pin_type,pin_function,related_power_pin,
                            #     related_ground_pin,len(scope),line)

                            if len(scope)<2:
                                if pin_type=='input':
                                    temp_input_pin=create_input_pin_dict(pin_name,pin_name=pin_name,pin_type=pin_type,
                                    related_power_pin=related_power_pin,
                                    related_ground_pin=related_ground_pin, related_bias_pin=related_bias_pin,
                                    max_transition=max_transition,capacitance=capacitance,
                                    rise_capacitance=rise_capacitance,fall_capacitance=fall_capacitance
                                    )
                                    # print(name, pin_name,pin_type,line)
                                    input_pin[pin_name]=temp_input_pin.copy()
                                    # print(name,"Exit from pin :",pin_name,pin_type,pin_function,related_power_pin,
                                    #     related_ground_pin,len(scope),line)

                                elif pin_type=="output":
                                    temp_output_pin=create_output_pin_dict(pin_name,pin_name=pin_name,pin_type=pin_type,
                                    pin_function=pin_function, related_power_pin=related_power_pin,
                                    related_ground_pin=related_ground_pin,related_bias_pin=related_bias_pin,
                                    max_transition=max_transition,min_capacitance=min_capacitance,
                                    max_capacitance=max_capacitance
                                    )
                                    output_pin[pin_name]=temp_output_pin.copy()

                                    # print(name,"Exit from pin :",pin_name,pin_type,pin_function,related_power_pin,
                                    #     related_ground_pin,len(scope),line)
                                    # print(name, pin_name,pin_type,line)

                # read the line for next iteration for next cell 
                line=inline.readline()
                
        else:
            line=inline.readline()
            # line=line.replace(" ", "")


    # Show the outputs: 
    
    # print(dct)
    # print(list1)
    # print(dictionary)

    # for keys, values in dictionary.items():
    #     print(keys,":",values)

    # print(dictionary["9INV_X0P5M_A9TR_W3"]['cell_footprint'])
    # print(dictionary["9INV_X0P5M_A9TR_W3"]["area"])
    # print(dictionary["9INV_X0P5M_A9TR_W3"]['cell_leakage_power'])
    # print(dictionary["9INV_X0P5M_A9TR_W3"]['input_pin'])
    # print(dictionary["3AND2_X11M_A9TR_W3"]['input_pin'])
    # print(dictionary["3AND2_X11M_A9TR_W3"]['output_pin'])
    # print("\n9INV_X0P5M_A9TR_W3 :",dictionary["9INV_X0P5M_A9TR_W3"]['power_pin'])
    # print("\n6BUF_X0P8B_A9TR_W3 :",dictionary["6BUF_X0P8B_A9TR_W3"]['power_pin'])
    # print(dictionary["12INV_X0P7B_A9TR_W3"]['power_pin']["VDD"])
    # print(dictionary["12INV_X0P7B_A9TR_W3"]['power_pin']["VNW"])
    # print(dictionary["12INV_X0P7B_A9TR_W3"]['power_pin']["VPW"])
    # print(dictionary["12INV_X0P7B_A9TR_W3"]['power_pin']["VSS"])


