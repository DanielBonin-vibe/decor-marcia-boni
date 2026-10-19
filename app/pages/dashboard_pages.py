from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates, Request
from sqlalchemy.orm import Session
from app.api.dependencias import get_db

from app.core.jwt import 


router = APIRouter(
    prefix='/dashboard',
    tags=['Dashboard']
    )

templates = Jinja2Templates(directory='app/templates')

@router.get('/')
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='pages/dashboard.html'
    )