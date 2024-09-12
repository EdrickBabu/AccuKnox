import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'accuknox.settings'

import django
django.setup()




import time
import threading
from django.db import transaction
from my_app.models import MyModel


def main():
    try:
        # Start a new transaction block
        with transaction.atomic():
            # Output to check the thread in which the main function runs
            print(f"Main function running in thread: {threading.current_thread().name}")
            
            # Create an object to trigger the post_save signal
            obj = MyModel.objects.create(name="Initial Name")
            print("Object created.")
            
            # Raise an exception to trigger a rollback
            raise Exception("Triggering rollback")
    except Exception as e:
        print("Transaction rolled back.")

    # After the transaction block, check if the signal-modified name was persisted
    is_modified = MyModel.objects.filter(name="Signal Modified").exists()
    print(f"Was the signal-modified name persisted? {is_modified}")

if __name__ == "__main__":
    main()
