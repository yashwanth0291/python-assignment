try :
    file=open('sample.txt','r')
    read_file=file.read()
    print(read_file)
    file.close()
except ModuleNotFoundError:
    print("the file simple.txt not found.... ")
finally:
    exit()