from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
from models.base_model import BaseModel
globals()['BaseModel'] = BaseModel
#globals()['User'] = User
