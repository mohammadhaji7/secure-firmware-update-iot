current_version_file = "firmware/current_version.txt"
update_version_file = "firmware/update_version.txt"

with open(current_version_file, "r") as f:
    current_version = f.read().strip()

with open(update_version_file, "r") as f:
    update_version = f.read().strip()

print(f"Current Installed Firmware Version: {current_version}")
print(f"Incoming Firmware Version: {update_version}")

if float(update_version) < float(current_version):
    print("\n[SECURITY ALERT]")
    print("Rollback attack detected!")
    print("Firmware update rejected.")
else:
    print("\nFirmware update accepted.")
