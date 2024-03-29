import commands
 
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    #return float(1.8*cpu_temp)+32
 
def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return  float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8* gpu_temp)+32
 
def main():
    print "CPU temp: ", str(get_cpu_temp())
    print "GPU temp: ", str(get_gpu_temp())

    resCPU = '{"value":%f}' %get_cpu_temp()
    resGPU = '{"value":%f}' %get_gpu_temp()

    output = open('/home/pi/MyApp/UploadTempToYeelink/cpuTemp.txt', 'w')
    output.write(resCPU)
    output.close

    output = open('/home/pi/MyApp/UploadTempToYeelink/gpuTemp.txt', 'w')
    output.write(resGPU)
    output.close
    print "save file done!"

if __name__ == '__main__':
    main()
