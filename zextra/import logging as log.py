import logging as log

log.basicConfig(filename='logfile.log',level=log.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')



try:
    log.info("enter the age ")
    age = int(input("enter the age "))
    log.info('enter the age already %d',age)
    if age<0:
        log.info('in the if block')
        raise ValueError("please enter the +ve value")
        log.info('run the raise')
    
except ValueError as v:
    log.error(v)