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
In this experience, in addition to trying to experience mobile programming with Python, I was also looking for another experience, which was to get help from AI as an assistant. At first, it was not a good experience at all. Over time, I realized that working with AIs like ChatGPT has its own method. When working with AIs, you should consider the following:
- Never trust the words of AI completely. He makes decisions by searching through the experiences of others, which may have thousands of exceptions and detailed issues.
- Help him analyze the problem to choose the best solution. This can be done by constantly asking questions about small things that he may not have considered.
- Never leave big issues to her in their entirety, but talk to her about the whole thing at one stage, then plan smaller issues based on the results and solve each one in different chats.
- Don't let it elaborate on issues or make off-topic suggestions. Be aware that these AIs can easily get sidetracked and forget things.
- If the chat gets too long, your segmentation may be flawed. In these cases, try to close the chat somewhere and get an understandable summary from the AI ​​and continue it in the next chat.
In general, in programming and system design, consider artificial intelligence only as an assistant that helps you achieve high speed in design, implementation, and documentation, but if you leave it alone, it will definitely not be able to complete the project and will lead the project astray. So, if you don't have the basics of designing and coding with programming languages ​​and the science behind these topics, never program with AI, especially if your program is a bit large and complex.

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

### How to Start Each Chat
- At the beginning of each chat, copy a short summary of the project:

Project: Python-based Android SMS automation app for Android 9
Features: Foreground service, CSV tracking, SMS sending, delivery status
Libraries: pandas, openpyxl, jnius (Chaquopy)
Goal: Implement module X

- Include previous deliverables or file names, so the new chat has everything it needs.

### Tips to Avoid Confusion or Loops
- Always reference module number (“We are implementing Module 2: CSV Handling”).
- Use self-contained code snippets — never rely on “previous chat” to define variables or paths.
- Test each module independently before moving to the next.
- Save all file names, folder structure, and Gradle configs; copy them into the new chat as context.
- Include comments in code to remind the next chat where it fits in the architecture.

