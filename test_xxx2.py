# test_xxx2.py

import socket
from unittest.mock import patch, MagicMock
import unittest
from xxx import get_local_ip, reverse_string

class TestGetLocalIP(unittest.TestCase):
    @patch('socket.socket')
    def test_get_local_ip_SuccessfulRetrieval_ReturnsLocalIP(self, mock_socket):
        # 模拟套接字行为
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        mock_socket_instance.getsockname.return_value = ('192.168.1.100', 12345)

        ip_address = get_local_ip()

        self.assertEqual(ip_address, '192.168.1.100')
        mock_socket_instance.connect.assert_called_once_with(('8.8.8.8', 80))
        mock_socket_instance.close.assert_called_once()

    @patch('socket.socket')
    def test_get_local_ip_SocketException_HandlesGracefully(self, mock_socket):
        # 模拟套接字异常
        mock_socket.side_effect = socket.error("Socket error")

        with self.assertRaises(socket.error):
            get_local_ip()

    @patch('socket.socket')
    def test_get_local_ip_NoNetworkConnection_HandlesGracefully(self, mock_socket):
        # 模拟连接失败
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        mock_socket_instance.connect.side_effect = socket.error("Connection failed")

        with self.assertRaises(socket.error):
            get_local_ip()

class TestReverseString(unittest.TestCase):
    def test_reverse_string_NormalCase(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_string_EmptyString(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_SingleCharacter(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_MultipleSpaces(self):
        self.assertEqual(reverse_string("  hello world  "), "  dlrow olleh  ")

if __name__ == '__main__':
    unittest.main()