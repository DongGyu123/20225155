import httpx
from pydantic import BaseModel, Field
from pydantic_core import Url
import json

class MobileXClient(BaseModel):
    base_url: Url = Field(
        default=Url('http://localhost:8000'),
    )

    def call[To: BaseModel](
        self,
        function: str,
        input: BaseModel,
        output_model: type[To],
    ) -> To | None:
        response = httpx.post(
            url=f'{self.base_url}func/{function}',
            json=input.model_dump(),
            timeout=300.0,
        )
        json_data = input.model_dump()  # 전송할 데이터를 변수에 저장
        print('Request data:', json_data)  # 전송할 데이터를 출력
        print('respons url and data', response.url, type(response))
        data = response.json()
        if data is None:
            return None

        return output_model.model_validate(data)
