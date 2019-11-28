copy "C:\development\projects\gacc\nfpauto\install-script\Output\setup.exe" "c:\development\projects\gacc\nota-do-bem-site\files" /y
copy "C:\development\projects\gacc\nfpauto\install-script\Output\version.json" "c:\development\projects\gacc\nota-do-bem-site\files" /y


rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.1"
rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.2"
rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.3"
rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.4"
rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.5"

mkdir "c:\development\projects\gacc\nota-do-bem-site\files\1.0.6"

copy "output\setup_1.0.6.exe" "c:\development\projects\gacc\nota-do-bem-site\files\1.0.6"

pause