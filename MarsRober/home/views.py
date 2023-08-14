from django.shortcuts import render
from django.http import HttpResponse
import requests
import plotly.graph_objects as go
from django.core.paginator import Paginator
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive mode
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime
import serial
import subprocess
import os

# deesanjog@gmail.com


def control(request):
    return render(request, 'control.html')

def run_script(request):
    if request.method == 'POST':
        # Execute the Python script
        subprocess.run(['python', 'D:/Softwarica/SEM4/MarsRover/MarsRober/template/controller.py']) # give the correct path for the file
    
    return render(request, 'control.html')