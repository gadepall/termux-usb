Import("env")
import time

def before_upload(source, target, env):
    delay_seconds = 5 # Change this to whatever gives you enough time

    print("\n" + "="*40)
    print(" PREPARE TO PRESS RESET! ")
    print("="*40)

    for i in range(delay_seconds, 0, -1):
        print(f"Starting avrdude in {i} seconds...")
        time.sleep(1)

    print("Uploading now!\n")

# Attach this function to run right before the "upload" process
env.AddPreAction("upload", before_upload)
