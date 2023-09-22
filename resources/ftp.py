import os 

def ftp_grabber(base_folder, output_file):
    with open(output_file, 'a', encoding='utf-8') as out_file:
        for  root, _,files in os.walk(base_folder):
            for file in files:
                if file == 'Credentials.txt':
                    file_path = os.path.join(root,file)
                    print(file_path)
                    with open(file_path, 'r', encoding='utf-8') as ftp_file:
                        ftp_c=ftp_file.read()
                        out_file.write(ftp_c)
                        out_file.write('\n')
        print("----Successfully FTP Credentials Grabbed .----")

def extract_ftp_credentials(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file, open(output_file, 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        i = 0

        while i < len(lines):
            if lines[i].strip().startswith("Server:"):
                server = lines[i].strip().split(":")[1].strip()
                i += 1
                if i < len(lines) and lines[i].strip().startswith("Username:"):
                    username = lines[i].strip().split(":")[1].strip()
                    i += 1
                    if i < len(lines) and lines[i].strip().startswith("Password:"):
                        password = lines[i].strip().split(":")[1].strip()
                        i += 1
                        output_file.write(f"{server}:{username}:{password}\n")
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1

def runftp(base_folder, output_file):
    ftp_grabber(base_folder,"ftp_temp.txt")
    extract_ftp_credentials("ftp_temp.txt", output_file)