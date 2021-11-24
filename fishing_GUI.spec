# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['fishing_macro.py'],
             pathex=['C:\\Users\\suho\\Desktop\\GUI_auto'],
             binaries=[],
             datas=[('init.txt', '.'), ('alarm.mp3', '.'), ('./img/fishing_point.png', './img'), ('./img/lostark.png', './img'), ('fishing.ico', '.')],
             hiddenimports=['config'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='로스트아크 낚시 알리미',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
		  onefile=True,
		  icon='C:/Users/suho/Desktop/GUI_auto/fishing.ico'
		  )
