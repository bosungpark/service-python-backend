"""
File_1: 유효 음절 수 세기

단어의 음절 수를 센다.
새로 작성해야 하는 부분
.py
"""
import json
import string
from typing import Dict
from pathlib import Path
from nltk.corpus import cmudict

def refine_punctuation(syllables_dict:Dict)->Dict:
    """
    CMU 단어의 문장부호 처리하기 함수입니다.
    """
    new_syllables_dict=dict()
    for word, syllables in syllables_dict.items():
        temp_word=''
        for s in word:
            if s not in string.punctuation and s.isalpha():
                temp_word+=s
        new_syllables_dict[temp_word]=syllables
    return new_syllables_dict

def count_syllables(new_syllables_dict:Dict,data:Dict)->Dict:
    """
    모델 생성 함수입니다.
    """
    refined_syllables_dict=dict()
    
    for word, syllables in new_syllables_dict.items():
        cnt = 0
        for syllable in syllables[0]:
            for syllable in syllable:
                if syllable[-1].isdigit():
                    cnt+=1
        refined_syllables_dict[word]=cnt
    #json 데이터 병합
    refined_syllables_dict.update(data)
    return refined_syllables_dict

def count_syllable_main():
    """
    메인함수입니다.
    """  
    file = Path('resources/additional_syllables.json')
    with open(file) as f:
        data = json.load(f)

    syllables_dict= cmudict.dict()

    new_syllables_dict=refine_punctuation(syllables_dict)
    syllables_model= count_syllables(syllables_dict,data)
    # print(syllables_model)
    return syllables_model

if __name__ == '__main__':
    count_syllable_main()