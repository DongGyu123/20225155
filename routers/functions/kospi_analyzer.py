from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 절대 경로
grandparent_dir = os.path.dirname(os.path.dirname(current_dir))  # 이중 상위 디렉토리의 경로
sys.path.append(grandparent_dir)
from Models.kospi_analyzer import InputModel, OutputModel

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
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # Latest News
                * Headline: {model.latest_news}
            ''',
        }),
    )
