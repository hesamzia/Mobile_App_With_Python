from java import jclass

def say():
    Log = jclass("android.util.Log")
    Log.i("ChaquopyTest", "✅ Python function say() executed")
    return "Python is running from Chaquopy"
