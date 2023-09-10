import os
import re

def conc(base_folder,temp_file):
    with open(temp_file, 'w+', encoding='utf=8') as temp:
        for root, _, files in os.walk(base_folder):
            for file in files:
                if file == 'Passwords.txt':
                    file_path = os.path.join(root,file)
                    with open(file_path, 'r', encoding='utf-8') as lineinpassword_file:
                        line = lineinpassword_file.read()
                        temp.write(line)
                        temp.write('\n')

def extract_url(text):
    regex = r'URL: (?P<url>https?://(?:www\.)?([a-zA-Z0-9.-]+)\.\w+)/?\nUsername: (?P<username>.+)\nPassword: (?P<password>.+)\nApplication: (?P<app>.+)'
    matches = re.findall(regex, text)
    return matches

def organize(seqs):
    domain_data = {}
    for seq in seqs:
        domain = seq[1]
        username = seq[2]
        password = seq[3]
        if domain not in domain_data:
            domain_data[domain]=[]
        domain_data[domain].append(f"{username}:{password}")
    return domain_data

def write_data(data):
    for domain, seqs in data.items():
        file_path = os.path.join("logins",f"{domain}.txt")
        print(file_path)
        with open(file_path,'a',encoding='utf-8') as file :
            for seq in seqs:
                file.write(seq + "\n")

def runlogins(base_folder):
    conc(base_folder,"temp.txt")
    with open("temp.txt", 'r', encoding='utf-8') as file:
        text = file.read()
        seq = extract_url(text)
        org = organize(seq)
        write_data(org)
