from common import *
from apps.common import storage
from storage import mock_storage
from trezor.messages import BackupType

from trezor import io
from trezor.db import DB


class TestTrezorDb(unittest.TestCase):

    def setUp(self):
        self.sd = io.SDCard()
        self.sd.power(True)
        self.fs = io.FatFS()
        self.fs.mkfs()
        self.sd.power(False)

    @mock_storage
    def test_put_get(self):
        storage.device.store_mnemonic_secret(b"abcd", BackupType.Bip39)
        db = DB("test1")
        data = [-23, b"b", {"f1": 1337, "f2": b"b", "f3": "s", "f": True}, "s", False]
        db.put(b"key", data)
        self.assertEqual(db.get(b"key"), data)

    @mock_storage
    def test_put_del_get(self):
        storage.device.store_mnemonic_secret(b"abcd", BackupType.Bip39)
        db = DB("test2")
        db.put(b"key", b"value")
        db.delete(b"key")
        with self.assertRaises(KeyError):
            db.get(b"key")

if __name__ == '__main__':
    unittest.main()
