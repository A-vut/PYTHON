import re

scope=[]

def create_input_pin_dict(name, **kwargs):
    input_pin[name]=kwargs
    return input_pin[name]

def create_output_pin_dict(name, **kwargs):
    output_pin[name]=kwargs
    return output_pin[name]

def add_cb(list_data):
    for x in list_data:
        scope.append('{')
    return scope

def remove_cb(list_data):
    for x in list_data:
        scope.pop()
    return scope


with open("t.lib","r") as inline:
    input_pin={}
    output_pin={}
    line=inline.readline()
    # print(len(scope),scope,line)
    line=line.replace(" ", "")
    scope=add_cb(re.findall("{", line))
    scope=remove_cb(re.findall("}", line))
    # print(len(scope),scope,line)
    while line:
        # line=line.replace(" ", "")
        # scope=add_cb(re.findall("{", line))
        # scope=remove_cb(re.findall("}", line))
        # if re.search(r"\bpg_pin",line):
        # print(line)
        # print("Size of scope :",len(scope),scope,line)
        if re.search(r"\bpin\([A-Z]\)",line):
        # print(line)
        # pass
        # pin_name=re.search("[A-Z]", line)
        # pin_name=pin_name.group()
        # print(pin_name)
            print("Size of scope :",len(scope),scope,line)

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
                print(pin_name,len(scope),line)
                
                # print(name,':',line)
                pin_type=pin_function=related_power_pin=related_ground_pin="",
                while len(scope)>=2:
                    print(pin_name,len(scope),line)
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
                    
                    line=inline.readline()
                    line=line.replace(" ", "")
                    scope=add_cb(re.findall("{", line))
                    scope=remove_cb(re.findall("}", line))
                print("Exit from pin :",pin_name,pin_type,pin_function,related_power_pin,
                related_ground_pin,len(scope),line)
                #     print(name,pin_name,len(scope),line)

                #     if len(scope)<2 :
                # #         # temp_power_pin=create_power_pin_dict(pin_name,pin_name=pin_name,pg_type=pg_type,
                # #         # related_bias_pin=related_bias_pin, physical_connection=physical_connection,
                # #         # voltage_name=voltage_name
                # #         # )
                #         if pin_type=='input':
                #             # temp_input_pin=create_input_pin_dict(pin_name,pin_name=pin_name,pin_type=pin_type,
                #             # related_power_pin=related_power_pin,
                #             # related_ground_pin=related_ground_pin
                #             # )
                #             print(name, pin_name,pin_type,line)
                # #             input_pin[pin_name]=temp_input_pin.copy()

                #         elif pin_type=="output":
                #             # temp_output_pin=create_output_pin_dict(pin_name,pin_name=pin_name,pin_type=pin_type,
                #             # pin_function=pin_function, related_power_pin=related_power_pin,
                #             # related_ground_pin=related_ground_pin
                #             # )
                #             print(name, pin_name,pin_type,line)
                # #             output_pin[pin_name]=temp_output_pin.copy()
                #         # break
                
                
                # # # temp_power_pin.clear()


                line=inline.readline()
                line=line.replace(" ", "")
                scope=add_cb(re.findall("{", line))
                scope=remove_cb(re.findall("}", line))
                print(pin_name,len(scope),line)
                # print(name,":",line)
            # print(name,power_pin)
                # print("Line :",line,name,power_pin)
        
                

        line=inline.readline()
        line=line.replace(" ", "")
        scope=add_cb(re.findall("{", line))
        scope=remove_cb(re.findall("}", line))