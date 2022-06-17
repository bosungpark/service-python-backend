"""
시조를 생성한다.
하이쿠에서 개선해야 하는 부분
.py
"""
import string
import random
from pathlib import Path
from unittest import main
from count_syllable import count_syllable_main
from collections import deque
from typing import List
from copy import deepcopy

file= Path('resources/training_datas.txt')
with open(file) as f:
    raw_haiku = f.read()

syllables_model=count_syllable_main()
# print(syllables_model)

def refine_punctuation(raw_haiku:List)->List:
    """
    데이터 정제 함수입니다.

    문장부호 및 기타 필요한 처리를 한 단어들을 리스트 형식으로 반환합니다.   
    new_haiku = ['hello', 'world', 'hello', 'the']
    """
    new_haiku=list()
    for word in raw_haiku.split():
        temp_word=''
        
        for s in word.strip():
            if s not in string.punctuation:
                temp_word+=s
        new_haiku.append(temp_word)
    return new_haiku
# print(refine_punctuation(raw_haiku))

new_haiku=refine_punctuation(raw_haiku)

def generate_haiku_lines(new_haiku:List, syllables_model:List)->None:
    """
    하이쿠의 라인조합을 생성하는 함수입니다.
    """
    syllable3=list()
    syllable4=list()
    syllable5=list()

    # def random_choice(syllable_list):
    #     return random.choice(syllable_list)

    for word in new_haiku:
        if word in syllables_model and syllables_model[word]==3:
            syllable3.append(word)
        elif word in syllables_model and syllables_model[word]==4:
            syllable4.append(word)
        elif word in syllables_model and syllables_model[word]==5:
            syllable5.append(word)

    def generate_first_or_second_line():
        """
        초/중장 샘플을 생성합니다.
        """

        s3=deepcopy(syllable3)
        s4=deepcopy(syllable4)
       
        words3=[]
        while len(s3)>=2:
            temp_word=[]
            temp_word.append(s3.pop())
            temp_word.append(s3.pop())
            words3.append(temp_word)
            #인접한 랜덤조건 충족을 위한 설정
            words3.append(temp_word.reverse())

        words4=[]
        while len(s4)>=2:
            temp_word=[]
            temp_word.append(s4.pop())
            temp_word.append(s4.pop())
            words4.append(temp_word)
            words4.append(temp_word.reverse())

        # print(words3)
        
        haiku1_or_haiku2=[]
        while len(words3)>0 and len(words4)>0:
            w3=words3.pop()
            w4=words4.pop()
            try:
                haiku1_or_haiku2.append((w3[0],w4[0],w3[1],w4[0]))
            except:
                pass

        return haiku1_or_haiku2

    def generate_third_line(syllable4:List,syllable5:List)->List:
        """
        종장 샘플을 생성합니다.
        """
        words3=[]
        while len(syllable3)>=2:
            temp_word=[]
            temp_word.append(syllable3.pop())
            temp_word.append(syllable3.pop())
            words3.append(temp_word)
            words3.append(temp_word.reverse())

        haiku3=[]
        # print(haiku3)
        # print(words3)
        syllable4=deque(syllable4)
        syllable5=deque(syllable5)
        while len(words3) and syllable4 and syllable5:
            w3=words3.pop()
            w4=syllable4.popleft()
            w5=syllable5.popleft()
            try:
                haiku3.append((w3[0],w5,w4,w3[1]))
            except:
                pass  
        return haiku3

    first_or_second_lines=generate_first_or_second_line()
    third_lines=generate_third_line(syllable4,syllable5)
    # print(first_or_second_lines)

    haiku=list()
    haiku.append(random.choice(first_or_second_lines))
    haiku.append(random.choice(first_or_second_lines))
    # print(third_lines)
    haiku.append(random.choice(third_lines))

    print("하이쿠 시작합니다!")
    for idx, line in enumerate(haiku,start=1):
        print(f"{idx}장:", end=" ")
        for word in line:
            print(word, end=" ")
        print()
        
    return

if __name__ == '__main__':
    generate_haiku_lines(new_haiku, syllables_model)
    