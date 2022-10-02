# coding=utf-8
import os
from tensor2tensor.utils import registry
from tensor2tensor.data_generators import problem, text_problems

#自定义的problem一定要加该装饰器，不然t2t库找不到自定义的problem
@registry.register_problem
class MyProblem(text_problems.Text2TextProblem):
    @property
    def approx_vocab_size(self):
        return 2**11

    @property
    def is_generate_per_split(self):
        return False

    @property
    def dataset_splits(self):
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 9,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 1,
        }]

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        del data_dir
        del tmp_dir
        del dataset_split
        #read rawdata
        comment_list = []
        tag_list =[]

        directory = 'q'

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                fr = open(f)
                comment_list = comment_list + fr.readlines()

        directory = 'a'
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                fr = open(f)
                tag_list = tag_list + fr.readlines()

        for comment, tag in zip(comment_list, tag_list):
            comment = comment.strip()
            tag = tag.strip()
            yield {
                "inputs": comment,
                "targets": tag
            }
