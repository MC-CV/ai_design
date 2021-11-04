
from tqdm import tqdm
class analyse():
    def __init__(self):
        pass

    @staticmethod
    def _stats(cut_corpus, gold_corpus ,tp):
        """计算准确率、召回率、F1值。"""
        d1 = {'as':'\u3000','msr':'  ','pku':'  ','cityu':' '}
        success_count, cut_count, gold_count = 0, 0, 0
        # import pdb;pdb.set_trace()
        for index in tqdm(range(len(cut_corpus))):
            cut_sentence = cut_corpus[index].strip().split(d1[tp])
            gold_sentence = gold_corpus[index].strip().split(d1[tp])
            cut_count += len(cut_sentence)
            gold_count += len(gold_sentence)
            for word in cut_sentence:
                if word in gold_sentence:
                    success_count += 1
        recall = float(success_count) / float(gold_count)
        precision = float(success_count) / float(cut_count)
        f1 = (2 * recall * precision) / (recall + precision)
        return precision, recall, f1

    @staticmethod
    def test(goldset,cutset,tp):
        """分词测试。"""
        gold_corpus = [
            sentence for sentence in goldset if sentence
        ]
        cut_corpus = [
            sentence for sentence in cutset if sentence
        ]
        result = analyse._stats(cut_corpus, gold_corpus,tp)
        return result

    #根据状态序列进行分词
    @staticmethod
    def tag_seg(sentence,tag):
        word_list = []
        start = -1
        started = False

        if len(tag) != len(sentence):
            return None

        if len(tag) == 1:
            word_list.append(sentence[0])   #语句只有一个字，直接输出

        else:
            if tag[-1] == 'B' or tag[-1] == 'M':    #最后一个字状态不是'S'或'E'则修改
                if tag[-2] == 'B' or tag[-2] == 'M':
                    tag[-1] = 'S'
                else:
                    tag[-1] = 'E'

            for i in range(len(tag)):
                if tag[i] == 'S':
                    if started:
                        started = False
                        word_list.append(sentence[start:i])
                    word_list.append(sentence[i])
                elif tag[i] == 'B':
                    if started:
                        word_list.append(sentence[start:i])
                    start = i
                    started = True
                elif tag[i] == 'E':
                    started = False
                    word = sentence[start:i + 1]
                    word_list.append(word)
                elif tag[i] == 'M':
                    continue

        return word_list