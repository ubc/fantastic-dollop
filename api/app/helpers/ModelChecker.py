import logging
from typing import Dict

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from pydantic import BaseModel

log = logging.getLogger(__name__)

unmatchedIdException = HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                     detail="Course ID in route does not match course ID in request data.")

# id is an optional parameter for incoming data since the id is given in the
# url itself. This check ensures that:
# - If an id is given in the model, it matches the expected one in the url
# - If id is missing in the model, we fill it in
async def checkId(expectedId: int, model: BaseModel):
    if model.id:
        if model.id != expectedId:
            raise unmatchedIdException
    else:
        model.id = expectedId
    return model

# doesn't fill in missing ids, just check them, for checking foreign key fields
async def checkIds(expectedIds: Dict[str, int], model: BaseModel):
    model = model.dict()
    for idKey, idVal in expectedIds.items():
        if model[idKey] != idVal:
            raise unmatchedIdException
    return True
