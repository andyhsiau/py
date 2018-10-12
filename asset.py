# coding:utf-8
import requests
import json

def get_Asset_info(input_hostname) :
    
    hostname = '%s.delta.corp'%input_hostname

    input_data ="""
    <API version="1.0">   
            <citype>
                <name>Workstation</name>
                <criterias>
                    <criteria>
                        <parameter>
                            <name compOperator="IS">CI Name</name>
                            <value>%s</value>
                        </parameter>
                    </criteria>
                </criterias>
                <returnFields>
                    <!-- Syntax to return all available column(s). <name>*</name> -->
                    <name>*</name>
                </returnFields>
                <sortFields sortOrder="desc">
                    <name>Product Name</name>
                </sortFields>
            </citype>
    </API> 
    """ %hostname


    data = {

        "INPUT_DATA" : input_data,
        "OPERATION_NAME" : "read",
        "TECHNICIAN_KEY" : "214E3955-EDAA-4767-9741-2C02A0F2F5F0"
    }

    r = requests.post('http://twtpeasset01:8080/api/cmdb/ci/', data=data , timeout = 10)
    CI_info = json.loads(r.text)
    CI_value = CI_info['API']['response']['operation']['Details']['field-values']['record']['value']
    print(CI_info)


    info = {

        "host_name" : CI_value[0],
        "Last_logon_user" : CI_value[37],
        "device_Manufacturer" : CI_value[19],
        "device_model" : CI_value[10],
        "device_OS" : CI_value[25],

    }

   

    return info


get_Asset_info('twty2pc1796')




