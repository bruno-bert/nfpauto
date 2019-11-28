powershell -Command "Remove-Item 'output\*' -Recurse -Force"

"c:\Program Files (x86)\Inno Setup 5\compil32.exe" /cc install-script.iss
"c:\Program Files (x86)\Inno Setup 5\compil32.exe" /cc update-script.iss

copy "C:\development\projects\gacc\nfpauto\install-script\Output\setup.exe" "c:\development\projects\gacc\nota-do-bem-site\files" /y
copy "C:\development\projects\gacc\nfpauto\install-script\Output\version.json" "c:\development\projects\gacc\nota-do-bem-site\files" /y


rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.1"
rd /s /q "c:\development\projects\gacc\nota-do-bem-site\files\1.0.2"

mkdir "c:\development\projects\gacc\nota-do-bem-site\files\1.0.3"

copy "output\setup_1.0.3.exe" "c:\development\projects\gacc\nota-do-bem-site\files\1.0.3"

cd\
c:
cd development\projects\gacc\nota-do-bem-site\
git add .
git commit -m "publicando versao%RANDOM%"
git push

pause

