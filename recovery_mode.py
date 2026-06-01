import shutil

verification_status = "failed"

if verification_status == "failed":

    print("[SECURITY ALERT]")
    print("Firmware verification failed.")
    print("Entering recovery mode...\n")

    shutil.copy(
        "firmware/backup_firmware.bin",
        "firmware/restored_firmware.bin"
    )

    print("Backup firmware restored successfully.")
    print("Recovery process completed.")

else:
    print("Firmware verification successful.")
    print("Normal boot process continued.")
