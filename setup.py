#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "notaamiga",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","win32con"],
        'include_files': [
            'assets/icons/ai.png', 
            'assets/icons/cancel.png', 
            'assets/icons/cancel1.png', 
            'assets/icons/checked.png', 
            'assets/icons/close.png', 
            'assets/icons/cnpj.png', 
            'assets/icons/database.png', 
            'assets/icons/favicon2.png', 
            'assets/icons/folder.png', 
            'assets/icons/key.png', 
            'assets/icons/login.png', 
            'assets/icons/password.png', 
            'assets/icons/play1.png', 
            'assets/icons/refresh.png', 
            'assets/icons/shop.png', 
            'assets/icons/stop.png', 
            'assets/icons/up.png', 
            'assets/sounds/error.mp3',
            'assets/entidade.jpg',
            'styles/button_alert.css',
            'styles/button.css',
            'styles/main.css',
            'chromedriver.exe',
            'notas.db'
            ],
        'include_msvcr': True,
    }},
    executables = [Executable("main.py",base="Win32GUI")]
    )