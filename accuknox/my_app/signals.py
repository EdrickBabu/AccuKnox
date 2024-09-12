import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

# Define a signal handler to test all points
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    # Prevent recursive save operations
    if instance.name == "Signal Modified":
        return

    print(f"Signal received for instance: {instance.name}")
    
    # Test if the signal is in the same thread
    print(f"Signal running in thread: {threading.current_thread().name}")
    
    start_time = time.time()
    
    # Simulate a long-running process to prove synchronous behavior
    time.sleep(3)  # This will block the main thread if signal is synchronous
    
    # Record the end time
    end_time = time.time()
    
    # Calculate and print the waiting time
    waiting_time = end_time - start_time
    print(f"Signal processing completed. Waiting time: {waiting_time:.2f} seconds")
    
    # Modify the instance to test transaction rollback
    instance.name = "Signal Modified"
    instance.save()
