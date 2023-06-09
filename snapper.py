import sched, time
from datetime import datetime



from picamera import PiCamera
camera = PiCamera()



def capture_image(scheduler): 
    # schedule the next call first
    scheduler.enter(60, 1, capture_image, (scheduler,))
    now = datetime.now()

    current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
    camera.capture('../lpa/image_'+current_time+'.jpg'.format(i))
    print("taking photo " + 'image_'+current_time+'.jpg')
    # then do your stuff

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(2, 1, capture_image, (my_scheduler,))
my_scheduler.run()