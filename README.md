# Mobile_App_With_Python
Implement a small smart home control program using Python and the help of Java and artificial intelligence collaboration. An experience in how to control and behave with artificial intelligence as a programming assistant.

### Requirements

### Feasibility Analysis
| Requirement | Feasibility	|  Notes |
|---|---|---|
|Python-based Android app|✅Partially|Python can run on Android via Chaquopy or BeeWare / VOC, but GUI frameworks like Kivy are avoided. Chaquopy is proven for non-GUI apps.|
|Runs on Android 9|✅|Android 9 is supported by Chaquopy.|
|Background SMS sending	|⚠️	|Android has strict background SMS policies. From Android 8 (Oreo), apps cannot run arbitrary background services unless you implement a foreground service (even if there is no GUI, a small notification is mandatory).|
|Reads/writes Excel (CSV)|✅	|Python’s pandas or openpyxl can be used. Chaquopy supports pandas.|
|No GUI|✅|That simplifies things.|
|SMS status tracking (sent/delivered)|⚠️|Requires SMS BroadcastReceiver integration in Java/Kotlin; Python alone cannot receive SMS delivery callbacks directly. Chaquopy can call Java code for this.|

#### Foreground Service Basics
- A foreground service is an app component that runs continuously even when the app UI is not visible, but it must show a persistent notification.
- Android will not kill the service under normal circumstances, so your periodic SMS sending will be reliable.
- The Python code can run in the service via Chaquopy, but it must start when the service starts.
Foreground service trade-off:
✅ Reliable execution
✅ CSV reading/writing works as intended
✅ SMS sending works reliably
✅ Delivery status tracking works
⚠️ Small persistent notification visible
⚠️ Slight increase in resource usage

## Project Outline: Python-Based SMS Foreground App for Android 9

### Project Goal
- Develop an Android app using Python (Chaquopy) that periodically sends SMS messages to control a smart home.
- The app runs as a foreground service, showing a small notification, and handles sending and delivery status tracking.
- No graphical interface is required.
- App is intended for private use on a specific device.

### Functional Requirements
#### SMS Automation
- Reads a CSV file with columns: date, time, phone, text, status.
- Periodically checks records:
    - status = "not sent"
    - Scheduled time has passed
- Sends SMS via Android’s native API.
- Updates status to "sent".

#### Foreground Execution
- App runs continuously as a foreground service.
- Displays a persistent notification to comply with Android restrictions (Android 8+).

#### Excel/CSV Management
- Uses Python pandas (or openpyxl) for reading and writing CSV/Excel.
- Stores files in app-specific storage.

#### Configuration
- CSV checking interval is configurable.
- No GUI; configuration can be stored in a file or hard-coded Python script.


### Technical Stack
#### Python Libraries
- pandas → For CSV/Excel handling.
- datetime → For time comparison.
- time or schedule → For periodic checking.

#### Android Components
- Foreground Service → Runs Python scripts reliably in the background.
- Chaquopy → Python integration with Android Studio.
- Android Studio → Building APK on Windows.
#### APK Build Process
- Android Studio project with Empty Activity.
- Chaquopy plugin installed.
- Python dependencies added in build.gradle.
- Python code called from foreground service using Chaquopy API.

### Program Workflow
#### Service Startup
- User opens the app → foreground service starts.
- Notification displayed (e.g., “SMS Automation Running”).

#### CSV Processing Loop (Python)
- Check CSV periodically (configurable interval).
- For each row:
    - If status = "not sent" and time <= now:
        - Send SMS via Java API.
        - Update status to "sent" in CSV.

### Advantages of This Approach
✅ Works reliably on Android 9+
✅ No GUI, minimal complications
✅ CSV/Excel tracking fully automated
✅ Compatible with Windows + Android Studio
✅ Avoids Kivy, Buildozer, WSL, or kevy issues
✅ Python code reusable for logic changes

### Limitations / Trade-offs
- Persistent notification is required (cannot be fully hidden).
- Slightly higher battery/resource usage due to foreground service.
- SMS delivery tracking requires minimal Java code; cannot be pure Python.

## Strategy for Dividing the Project into Independent Chat Modules

### Principle
- Each chat should be self-contained: all necessary information, libraries, and file structures should be included.
- Use numbered steps or modules — each chat handles one module and produces complete deliverables (code snippets, folder structures, Gradle configs).
- Avoid dependencies on “previous chat state” — each module contains explicit instructions to continue from the last stage.

### Suggested Modules
|Module|Purpose|Deliverables in Chat|
|---|---|---|
|Module 1: Project Setup|Prepare Windows + Android Studio + Chaquopy environment|Step-by-step instructions to install Android Studio, configure Chaquopy plugin, create empty activity project, configure Gradle with Python and dependencies|
|Module 2: CSV Handling (Python)|Implement reading/writing Excel/CSV and status tracking|Python script for: reading CSV, filtering not sent rows, updating status; pandas/openpyxl setup; sample CSV file|
|Module 3: SMS Sending (Python + Java)|Integrate Python with Android SMS API|Java/Kotlin foreground service template; Python functions to call Java SMS API via Chaquopy; sample code for sending SMS|
|Module 4: Foreground Service Setup|Combine CSV, SMS, and delivery handling|Full foreground service template: start notification, run Python loop, handle exceptions, integrate all previous modules|
|Module 5: Testing & Debugging|Validate on device|Steps to test sending SMS, check CSV updates, handle edge cases (missed deliveries, CSV errors)|
|Module 6: APK Build|Build and deploy APK|Gradle build instructions, Chaquopy packaging, testing on Android 9 device|


### Step 2: Key Libraries & Tools
Python Libraries
pandas → For reading/writing Excel/CSV.
datetime → For timestamp comparison.
time or schedule → For periodic checking.
jnius (via Chaquopy) → For calling Android Java APIs for sending SMS and receiving delivery reports.
Android-Specific
Chaquopy → Python integration in Android Studio. Supports background services and calling Java APIs.
Android Studio → Required for building APK. Chaquopy plugin is installed here.
Java/Kotlin code → Minimal code to handle SMS delivery broadcast and foreground service.

### Step 3: Potential Problems
Background Execution
Android will kill background Python threads if the app is not in a foreground service.
Must implement a persistent notification even if invisible to the user.
SMS Delivery Status
Cannot be fully implemented in Python alone.
Need Java BroadcastReceiver integrated with Python via Chaquopy to update CSV.
Building APK
Using WSL + Buildozer is unnecessary here.
Correct approach: Android Studio + Chaquopy plugin.
Must ensure all libraries (pandas, openpyxl) are supported by Chaquopy. Pandas is officially supported.
No GUI
This is fine; just ensure the app is headless except for required notification for foreground service.

### Step 4: Recommended Architecture

### Step 5: Steps for Building APK

### ✅ Step 6: Conclusion
Feasible? ✅ Yes, with Chaquopy + Android Studio.
Not feasible purely in Python? ⚠️ Correct. Python alone cannot:
Receive SMS delivery reports
Run as persistent background service on Android 9+
Problematic approaches to avoid: Kivy, Buildozer, WSL Ubuntu, kevy (as per your past experience).
Required compromise: Minimal Java/Kotlin code for SMS and service integratio



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

