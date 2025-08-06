import logging
#from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .etl_siorg import etl_siorg
import sqlite3
from .forms import UploadFileForm
from core.etl_dwsiape import etl_dwsiape


def import_siorg(request):
  return render(request, 'import_siorg.html')


def import_siorg2(request):

  unidade = "122391"
  logging.info('Iniciando ETL...')
  conn = sqlite3.connect('db.sqlite3')
  etl_siorg(unidade, conn)
  logging.info('ETL finalizado!')

  return render(request, 'import_siorg2.html')


def handle_uploaded_file(f):
  with open("teste.csv", "wb+") as destination:
    for chunk in f.chunks():
      destination.write(chunk)


def upload_file(request):
  if request.method == "POST":
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      handle_uploaded_file(request.FILES["file"])
      etl_dwsiape(sqlite3.connect('db.sqlite3'), filename='teste.csv')
      return HttpResponseRedirect("/success/url/")
  else:
    form = UploadFileForm()
  return render(request, "upload_form.html", {"form": form})
