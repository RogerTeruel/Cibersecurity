import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    3389: "RDP", 5900: "VNC", 8080: "HTTP-Alt"
}

def scan_port(ip, port, timeout):
    """
    Attempts to connect to a TCP port and returns the status.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                return (port, "OPEN")
            elif result == 111:
                return (port, "CLOSED")
            else:
                return (port, f"FILTERED / ERROR CODE: {result}")
    except socket.timeout:
        return (port, "FILTERED / TIMEOUT")
    except Exception as e:
        return (port, f"ERROR / {str(e)}")


def tcp_scan(ip, start_port, end_port, timeout=1.0, max_threads=100, resolve_services=True):
    """
    Performs an advanced TCP scan with multi-threading.

    Parameters:
        ip (str): Target IP address.
        start_port (int): Initial port.
        end_port (int): Final port.
        timeout (float): Timeout per port.
        max_threads (int): Number of threads to use.
        resolve_services (bool): Whether to include known service names.

    Returns:
        List of tuples (port, status, service)
    """
    try:
        socket.inet_aton(ip)
    except socket.error:
        raise ValueError("Invalid IP address format.")

    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
        raise ValueError("Port range must be between 1 and 65535.")

    if start_port > end_port:
        raise ValueError("Start port must be less than or equal to end port.")

    results = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {
            executor.submit(scan_port, ip, port, timeout): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port = futures[future]
            try:
                port_number, status = future.result()
                service = COMMON_SERVICES.get(port_number, "Unknown") if resolve_services else ""
                results.append((port_number, status, service))
            except Exception as e:
                results.append((port, f"ERROR / {str(e)}", "Unknown"))

    # Sort results by port
    return sorted(results, key=lambda x: x[0])
