from typing import Literal

from pydantic import BaseModel, Field
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 절대 경로
grandparent_dir = os.path.dirname(os.path.dirname(current_dir))  # 이중 상위 디렉토리의 경로
sys.path.append(grandparent_dir)
from Models.base.image_preview import ImagePreviewModel


class InputModel(BaseModel):
    animation: str = Field(
        description='이름',
        default='홍길동',
        alias='이름',
    )
    my_charactor: Literal[
        '남',
        '여',
    ] = Field(
        default='남',
        alias='성별',
    )
    
    context: str = Field(
        description='년도',
        default='2024',
        alias='생년 년도',
    )
    target_charactor: Literal[
        '1월', '2월','3월','4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월',
    ] = Field(
        default='1월',
        description='월',
        alias='생년 월',
    )
    situation: Literal[
        '1일', '2일', '3일', '4일', '5일', '6일', '7일', '8일', '9일', '10일', '11일', '12일', '13일', 
        '14일', '15일', '16일', '17일', '18일', '19일', '20일', '21일', '22일', '23일', '24일',
        '25일', '26일', '27일', '28일', '29일', '30일', '31일'
    ] = Field(
        default='1일',
        description='생년 일',
        alias='생년 일',
    )

    llm_type: Literal['23:30~01:29', '1:30~3:29', '3:30~5:29', '5:30~7:29', '7:30~9:29', '9:30~11:29', '11:30~13:29', 
                      '13:30~15:29', '15:30~17:29','17:30~19:29', '19:30~21:29', '21:30~23:29', '모름'] = Field(
        description='태어난 시각',
        default='모름',
        alias='태어난 시각'
    )


class OutputModel(ImagePreviewModel):
    output: str = Field(
        description='응답',
    )
