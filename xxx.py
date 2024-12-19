# xxx.py

import socket

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def reverse_string(s):
    """Reverses the input string."""
    return s[::-1]

def get_local_ip():
    """
    获取本机的IP地址。
    
    Returns:
        str: 本机的IP地址。
    """
    s = None
    try:
        # 创建一个UDP套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个公共的IPv4地址和端口
        s.connect(("8.8.8.8", 80))
        # 获取本地IP地址
        ip_address = s.getsockname()[0]
    except socket.error as e:
        print(f"Socket error: {e}")
        raise
    finally:
        # 关闭套接字
        if s is not None:
            s.close()
    return ip_address