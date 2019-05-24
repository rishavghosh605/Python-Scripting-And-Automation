import win10toast
toaster=win10toast.ToastNotifier()
#icon_path is also an argument of .show_toast
toaster.show_toast('Python',' Success!This is working',duration=10)
exit()
