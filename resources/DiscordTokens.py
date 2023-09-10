import os 

def token_grabber(base_folder,output_file):
    with open(output_file, 'a', encoding='utf-8') as out_file:
        for  root, _,files in os.walk(base_folder):
            for file in files:
                if file == 'Tokens.txt':
                    file_path = os.path.join(root,file)
                    print(file_path)
                    with open(file_path, 'r', encoding='utf-8') as token_file:
                        token=token_file.read()
                        print(f"[+]Adding {token}")
                        out_file.write(token)
                        out_file.write('\n')
        print("----Successfully Tokens Grabbed .----")