from fastapi import APIRouter

router = APIRouter()


@router.get('/items', status_code=200, tags=['items'])
def get_items(recurrence: str | None = None):
    return {'message': 'got items'}


@router.post('/items', status_code=201, tags=['items'])
def create_item():
    return {'message': 'created item'}


@router.put('/items/{item_id}', status_code=204, tags=['items'])
def update_item(item_id: int):
    return


@router.delete('/items/{item_id}', status_code=204, tags=['items'])
def delete_item(item_id: int):
    return
