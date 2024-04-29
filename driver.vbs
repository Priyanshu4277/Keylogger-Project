Set objShell = CreateObject("WScript.Shell")
currentDirectory = CreateObject("Scripting.FileSystemObject").GetAbsolutePathName(".")
objShell.Run "cmd /c cd /d """ & currentDirectory & """ && executing.bat", 0, False
Set objShell = Nothing