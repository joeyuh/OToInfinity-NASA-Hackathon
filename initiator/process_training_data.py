import subprocess

def generate_trainingSet():
    cmd_list = ['python ./file_process/divider.py', 'python ./file_process/reader.py', 'python file_process/space_processor.py', 'python ./file_process/a_processor.py']
    for cmd in cmd_list:
        try:
            subprocess.run(cmd, shell=True)
        except Exception as e:
            print(e)
            break




if __name__ == '__main__':
    generate_trainingSet()