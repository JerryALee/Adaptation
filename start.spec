# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)

block_cipher = None


a = Analysis(['start.py', 'classfile.py', 'environment.py', 'settings.py', 'showscreen.py', 'text.py'],
             pathex=['C:\\Computational Biology\\软件开发实践\\Adaptation'],
             binaries=[],
             datas=[('C:\\Computational Biology\\软件开发实践\\Adaptation\\images', 'images'), ('C:\\Computational Biology\\软件开发实践\\Adaptation\\fonts', 'fonts')],
             hiddenimports=['pygame', 'os', 'random', 'sys', 'classfile', 'environment', 'settings', 'showscreen', 'text'],
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
          [],
          exclude_binaries=True,
          name='start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='start')
