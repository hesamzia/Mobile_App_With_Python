# Mobile_App_With_Python
Implement a small smart home control program using Python and the help of Java and artificial intelligence collaboration. An experience in how to control and behave with artificial intelligence as a programming assistant.<br/>

Step 1: Feasibility Analysis<br/>
| Requirement | Feasibility	|  Notes |
|---|---|---|
|Python-based Android app|✅Partially|Python can run on Android via Chaquopy or BeeWare / VOC, but GUI frameworks like Kivy are avoided. Chaquopy is proven for non-GUI apps.|
|Runs on Android 9|✅|Android 9 is supported by Chaquopy.|

|Background SMS sending	|⚠️	|Android has strict background SMS policies. From Android 8 (Oreo), apps cannot run arbitrary background services unless you implement a foreground service (even if there is no GUI, a small notification is mandatory).|
|Reads/writes Excel (CSV)|✅	|Python’s pandas or openpyxl can be used. Chaquopy supports pandas.|
|No GUI|✅|That simplifies things.|
|SMS status tracking (sent/delivered)|⚠️|Requires SMS BroadcastReceiver integration in Java/Kotlin; Python alone cannot receive SMS delivery callbacks directly. Chaquopy can call Java code for this.|

Python itself isn’t native to mobile platforms, but you can use frameworks that package Python code into mobile apps for example 
Chaquopy (for Android)
Python SDK for Android Studio.
Allows running Python code alongside Java/Kotlin in Android apps.
Pros: Easy integration if you already know Android development.
Cons: Not fully standalone; mostly for using Python logic in Android apps.

. Limitations
Performance: Python is slower than Java/Kotlin (Android) or Swift (iOS). For heavy apps, this matters.
Native APIs: Accessing all platform-specific features (like camera, Bluetooth) can be harder.
App size: Apps built with Python frameworks are usually larger.
iOS restrictions: Apple can be picky about apps not written in native languages.


. Limitations
Background SMS restrictions: Modern Android versions are strict about apps sending SMS in the background. Your app may only work reliably if it’s the default SMS app.
App store policies: Google Play may reject apps that send SMS automatically without strong user consent.
Always running app: Python apps don’t run as background services natively; you’d need to integrate with Android services.

Android SMS Restrictions
Starting Android 8+ (and stricter in 10+), apps cannot send SMS in the background unless they are the default SMS app.
Being a default SMS app means your app will replace the user’s SMS app, which is not ideal for most users.
Google Play Store may reject apps that try to send SMS automatically without being the default app.

Unlike Android 10 and later, Android 9 still allows background SMS sending via tools like Termux — so you can 100% build your automatic SMS scheduler in Python, for free, and without needing root or extra hardware.

Option A: Use Kivy + Buildozer
Write the app in Python on Windows.
Kivy supports mobile UI and Android packaging.
You’ll need WSL (Windows Subsystem for Linux) or a Linux virtual machine to run Buildozer, because it only works on Linux systems.
Buildozer packages your Python app into an .apk file you can install on Android.
You can then call Android’s SMS API using Pyjnius.
However, sending SMS automatically will still require the app to:
Request the SEND_SMS permission.
Possibly become the default SMS app on Android 10+ (on Android 9 it’s okay).

Option B: Use Chaquopy (Python inside Android Studio)
Android Studio runs on Windows.
Chaquopy lets you write part of your Android app logic in Python.
You use Java/Kotlin for UI and permissions.
Python handles scheduling and reading files.
This produces a proper Android .apk file.

3. Publishing Limitation
Even if you succeed in building a .apk, publishing on Google Play is very unlikely to be approved if:
It sends SMS automatically.
It doesn’t have clear user interaction before sending each message

Let’s restate what you want:
You want to develop your Android SMS app in Python (on your Windows PC).
You want to test it on a mobile simulator/emulator on Windows.
When ready, you’ll build an .apk and transfer it once to your Android 9 phone for real use.
No Play Store, no publishing — just local testing and maybe uploading the project to GitHub later.
✅ Yes, that’s 100% doable.

