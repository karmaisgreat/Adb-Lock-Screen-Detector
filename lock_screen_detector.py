import os,platform,time,requests
detected_os = platform.system()
if 'Windows' in detected_os:
    print('\nWindows OS Detected!\n')
    while True:
        getinfo = "platform-tools_r29.0.5-windows\\adb.exe shell dumpsys power > lock_detection.txt"
        os.system(getinfo)
        if '  mHoldingWakeLockSuspendBlocker=false' and '  mHoldingDisplaySuspendBlocker=false' in open('lock_detection.txt').read():
            print('PHONE IS LOCKED!')
        elif  '  mHoldingWakeLockSuspendBlocker=false' and '  mHoldingDisplaySuspendBlocker=true' in open('lock_detection.txt').read():
            print('PHONE IS UNLOCKED!')
        time.sleep(5)
elif 'Linux' in detected_os:
    print('\nLinux OS Detected!\n')
    while True:
        getinfo = "platform-tools_r29.0.5-linux\\adb shell dumpsys power > lock_detection.txt"
        os.system(getinfo)
        if '  mHoldingWakeLockSuspendBlocker=false' and '  mHoldingDisplaySuspendBlocker=false' in open('lock_detection.txt').read():
            print('PHONE IS LOCKED!')
        elif  '  mHoldingWakeLockSuspendBlocker=false' and '  mHoldingDisplaySuspendBlocker=true' in open('lock_detection.txt').read():
            print('PHONE IS UNLOCKED!')
        time.sleep(5)
else:
    print('\nUnknown OS Detected!\n')
    exit()