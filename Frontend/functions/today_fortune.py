import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 절대 경로
grandparent_dir = os.path.dirname(os.path.dirname(current_dir))  # 이중 상위 디렉토리의 경로
sys.path.append(grandparent_dir)
from Models.today_fortune import InputModel, OutputModel
from utils.page import PageModel


def execute(
    page: PageModel,
    key: str,
    model: InputModel,
) -> OutputModel | None:
    return page.settings.client.call(
        function=page.function,
        input=model,
        output_model=OutputModel,
    )
