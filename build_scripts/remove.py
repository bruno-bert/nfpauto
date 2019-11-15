import os
APP_NAME='NotaAmiga'

files =  ['..//dist//' + APP_NAME + '//Qt5Bluetooth.dll' ,
    './/dist//' + APP_NAME + '//Qt5DBus.dll' ,
    './/dist//' + APP_NAME + '//Qt5Designer.dll' ,
    './/dist//' + APP_NAME + '//Qt5Location.dll' ,
    './/dist//' + APP_NAME + '//Qt5Multimedia.dll' ,
    './/dist//' + APP_NAME + '//Qt5MultimediaWidgets.dll' ,
    './/dist//' + APP_NAME + '//Qt5Network.dll' ,
    './/dist//' + APP_NAME + '//Qt5NetworkAuth.dll' ,
    './/dist//' + APP_NAME + '//Qt5Nfc.dll' ,
    './/dist//' + APP_NAME + '//Qt5OpenGL.dll' ,
    './/dist//' + APP_NAME + '//Qt5Positioning.dll' ,
    './/dist//' + APP_NAME + '//Qt5PositioningQuick.dll' ,
    './/dist//' + APP_NAME + '//Qt5Qml.dll' ,
    './/dist//' + APP_NAME + '//Qt5Quick.dll' ,
    './/dist//' + APP_NAME + '//Qt5RemoteObjects.dll' ,
    './/dist//' + APP_NAME + '//Qt5Svg.dll' ,
    './/dist//' + APP_NAME + '//Qt5WebChannel.dll' ,
    './/dist//' + APP_NAME + '//Qt5WebSockets.dll' ,
    './/dist//' + APP_NAME + '//Qt5WinExtras.dll' ,
    './/dist//' + APP_NAME + '//Qt5Xml.dll' ,
    './/dist//' + APP_NAME + '//Qt5XmlPatterns.dll',
    './/dist//' + APP_NAME + '//PyQt5//QtBluetooth.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtDBus.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtDesigner.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtLocation.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtMultimediaWidgets.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtNetworkAuth.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtNfc.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtPositioning.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtRemoteObjects.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtWebChannel.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtWebSockets.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtWinExtras.pyd',
    './/dist//' + APP_NAME + '//PyQt5//QtXmlPatterns.pyd' ]

for f in files:
    try:
        os.remove(f)
        print('removed file: ' + f)
    except Exception as err:
        print(repr(err))
        
