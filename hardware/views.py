import subprocess

from rest_framework.views import Response
from rest_framework.decorators import api_view

from hardware.models import Stats


@api_view(["GET"])
def temperature(request):
    if request.method == "GET":
        output = subprocess.check_output(["vcgencmd", " measure_temp"], text=True)
        temp = float(output.split("=")[-1].split("'")[0])
        stats = Stats(soc_temp=temp)
        stats.save()
    return Response(f"Current SoC Temp is: {temp}", status=200)

    return Response(status=400)
