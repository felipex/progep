import logging
#from django.db import connection
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sqlite3
from .forms import UploadFileForm, ServidoresFilterForm
from core.etl_dwsiape import etl_dwsiape
from .models import Servidor
from .etl_siorg import etl_siorg


def index(request):
  return render(request, 'index.html')


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


@login_required
def servidores(request):
  form = ServidoresFilterForm(request.POST)
  servidores = []
  if form.is_valid():
    servidores = Servidor.objects.filter(nome=form.cleaned_data['nome'])

  return render(request, 'servidores.html', {
      'servidores': servidores,
      'form': form
  })
