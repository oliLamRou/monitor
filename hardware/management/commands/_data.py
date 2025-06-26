import subprocess


def get_temperature():
    output = subprocess.check_output(["vcgencmd", " measure_temp"], text=True)
    temp = float(output.split("=")[-1].split("'")[0])
    return temp
