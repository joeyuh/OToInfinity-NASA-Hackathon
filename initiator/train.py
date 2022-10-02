import subprocess

cmd_list = ['t2t-datagen --t2t_usr_dir=self_script --problem=my_problem --data_dir=./self_data', 't2t-trainer --t2t_usr_dir=self_script --problem=my_problem --data_dir=./self_data --model=lstm_seq2seq_attention --hparams_set=lstm_attention --output_dir=./train']

for cmd in cmd_list:
    subprocess.run(cmd, shell=True)