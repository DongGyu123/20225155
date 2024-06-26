import os

from fastapi import APIRouter

from llm.chat import build as build_chat
from llm.image import build as build_drawer
from llm.store import LLMStore
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 절대 경로
grandparent_dir = os.path.dirname(os.path.dirname(current_dir))  # 이중 상위 디렉토리의 경로
sys.path.append(grandparent_dir)
from Models.today_fortune import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_today_fortune(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build_chat(
        name=NAME,
        llm=store.get('chatgpt'),
    )

    input = f'''
        # About Me
        * Name: {model.name}
        * Gender: {model.gender}
        * Birth Year: {model.year}
        * Birth Month: {model.month}
        * Birth Date: {model.date}
        * Birth Time: {model.time}
    '''

    return OutputModel(
        output = chain.invoke({
            'input_context': input,
        })
    )