from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from ..serializers.userSerializers import userResponseEntity

from ..database.database import User
from ..models.schemas import UserResponse
from ..user_auth.oauth2 import require_user

router = APIRouter()


@router.get('/me', response_model=UserResponse)
def get_me(user_id: str = Depends(require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

