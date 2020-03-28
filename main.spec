# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['Demo.py', '', 'Demo_add.py', '', 'Demo_delete.py', '', 'Demo_error.py', '', 'Demo_login.py', '', 'Demo_re.py', '', 'Demo_show.py', '', 'Demo_success.py', '', 'Demo_update.py', '', 'C:\\Users\\Administrator\\Desktop\\pro'],
             binaries=[],
             datas=[],
             hiddenimports=['pymysql', 'wx'],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
