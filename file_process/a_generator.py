import os

def shift(in_dir,out_dir):
    q = []
    q_dir = '/Users/donglianghan/Desktop/NLP_for_NASA/raw_data/q'
    for question in os.listdir(q_dir):
        q.append(question)
    for filename in os.listdir(in_dir):
        f = os.path.join(in_dir,filename)
        otp = os.path.join(out_dir,filename)
        if filename in q:
            os.rename(f,otp)

if __name__ == '__main__':
    shift('./keywords','./raw_data/a')
