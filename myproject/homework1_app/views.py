from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Главная страница.</h1>
    <p>Это главная страница ДЗ № 1.</p>
    """
    logger.info("The main page has been loaded.")
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Здравствуйте, меня зовут Вера</h1>
    <p>Это моя первая попытка работы с Django.</p>
    """
    logger.info("The page about yourself has been loaded.")
    return HttpResponse(html)
