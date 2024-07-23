FILEPATH = "Members_list.txt"

def get_names(filepath = FILEPATH):

    with open(filepath,'r') as file_local:  #Read the text file and return the list of names in it
        names_local = file_local.readlines()
    return names_local

def write_names(names_arg,filepath = FILEPATH):


    with open(filepath,'w') as file:    #Write the list of names in text file
        file.writelines(names_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_names())
