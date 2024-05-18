# Change the MAX_CONNECTION value in server.conf file

def update_server_config(file_path,key,value):
    # Open file to read line
    with open(file_path,'r') as file:
        lines = file.readlines()
        
    # open file to do write operations
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


file_path = 'server.conf'
key = 'MAX_CONNECTIONS'
value = '300'
update_server_config(file_path,key,value)