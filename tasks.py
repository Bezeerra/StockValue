import os
from pathlib import Path
from pydantic import BaseModel
from models import WebHook


class Tasks(BaseModel):

    @staticmethod
    def create_file(webhook: WebHook) -> bool:
        with open(os.path.join(Path(__file__).parent, "GenerateTask.txt"), "w") as ff:
            convert_str = str(webhook)
            ff.write(f"LOGGIN POST:  {convert_str}")
            return True
