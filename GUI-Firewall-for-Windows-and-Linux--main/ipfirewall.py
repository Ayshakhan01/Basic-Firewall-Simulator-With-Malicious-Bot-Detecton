# #DETECT THE LOCAL MACHINE IP RANGE AND SUBNET MASK 

# import platform
# import subprocess
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget

# class FirewallApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Firewall App")
#         self.layout = QVBoxLayout()
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)

#         # Create input field for IP address
#         self.ip_input = QLineEdit()
#         self.block_button = QPushButton("Block IP")
#         self.unblock_button = QPushButton("Unblock IP")
#         self.ip_list = QListWidget()

#         self.layout.addWidget(self.ip_input)  # Add input field to layout
#         self.layout.addWidget(self.block_button)
#         self.layout.addWidget(self.unblock_button)
#         self.layout.addWidget(self.ip_list)

#         self.block_button.clicked.connect(self.block_ip)
#         self.unblock_button.clicked.connect(self.unblock_ip)

#     def get_connected_ips(self):
#         system = platform.system()
#         if system == "Linux":
#             # Using the correct subnet range
#             output = subprocess.check_output(['nmap', '-sn', '192.168.67.0/24']).decode('utf-8')
#             lines = output.split('\n')
#             ips = []
#             for line in lines:
#                 if 'Nmap scan report' in line:
#                     ip = line.split()[-1]
#                     ips.append(ip)
#             print("Connected IPs (Linux):", ips)  # Debugging print statement
#             return ips
#         elif system == "Windows":
#             output = subprocess.check_output(['arp', '-a']).decode('utf-8')
#             lines = output.split('\n')
#             ips = []
#             for line in lines:
#                 if line.strip() and line.startswith('  '):
#                     ip = line.split()[0]
#                     ips.append(ip)
#             print("Connected IPs (Windows):", ips)  # Debugging print statement
#             return ips
#         else:
#             print("Unsupported OS for retrieving IPs.")  # Debugging print statement
#             return []

#     def block_ip(self):
#         ip_address = self.ip_input.text()
#         system = platform.system()
#         if system == "Linux":
#             subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
#             print("Blocked IP:", ip_address)
#         elif system == "Windows":
#             subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="BlockIP"', 'dir=in', 'action=block', 'remoteip=' + ip_address])
#             print("Blocked IP:", ip_address)
#         else:
#             print("Unsupported operating system.")
#         self.verify_iptables()

#     def unblock_ip(self):
#         ip_address = self.ip_input.text()
#         system = platform.system()
#         if system == "Linux":
#             subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip_address, '-j', 'DROP'])
#             print("Unblocked IP:", ip_address)
#         elif system == "Windows":
#             subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name="BlockIP"', 'dir=in', 'action=block', 'remoteip=' + ip_address])
#             print("Unblocked IP:", ip_address)
#         else:
#             print("Unsupported operating system.")
#         self.verify_iptables()

#     def verify_iptables(self):
#         system = platform.system()
#         if system == "Linux":
#             output = subprocess.check_output(['sudo', 'iptables', '-L', '-v', '-n']).decode('utf-8')
#             print("Current iptables rules (Linux):")
#             print(output)
#         elif system == "Windows":
#             output = subprocess.check_output(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all']).decode('utf-8')
#             print("Current firewall rules (Windows):")
#             print(output)
#         else:
#             print("Unsupported operating system.")

#     def update_ip_list(self):
#         self.ip_list.clear()
#         connected_ips = self.get_connected_ips()
#         self.ip_list.addItems(connected_ips)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = FirewallApp()
#     window.update_ip_list()  # Ensure the IP list is updated when the window is shown
#     window.show()
#     app.exec_()







import platform
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QTextEdit

class FirewallApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firewall App")
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Create input field for IP address
        self.ip_input = QLineEdit()
        self.block_button = QPushButton("Block IP")
        self.unblock_button = QPushButton("Unblock IP")
        self.ip_list = QListWidget()
        self.rules_text = QTextEdit()  # Text box to display iptables rules
        self.rules_text.setReadOnly(True)

        self.layout.addWidget(self.ip_input)  # Add input field to layout
        self.layout.addWidget(self.block_button)
        self.layout.addWidget(self.unblock_button)
        self.layout.addWidget(self.ip_list)
        self.layout.addWidget(self.rules_text)  # Add rules text box to layout

        self.block_button.clicked.connect(self.block_ip)
        self.unblock_button.clicked.connect(self.unblock_ip)

    def get_connected_ips(self):
        system = platform.system()
        if system == "Linux":
            output = subprocess.check_output(['nmap', '-sn', '192.168.67.0/24']).decode('utf-8')
            lines = output.split('\n')
            ips = []
            for line in lines:
                if 'Nmap scan report' in line:
                    ip = line.split()[-1]
                    ips.append(ip)
            print("Connected IPs (Linux):", ips)  # Debugging print statement
            return ips
        elif system == "Windows":
            output = subprocess.check_output(['arp', '-a']).decode('utf-8')
            lines = output.split('\n')
            ips = []
            for line in lines:
                if line.strip() and line.startswith('  '):
                    ip = line.split()[0]
                    ips.append(ip)
            print("Connected IPs (Windows):", ips)  # Debugging print statement
            return ips
        else:
            print("Unsupported OS for retrieving IPs.")  # Debugging print statement
            return []

    def block_ip(self):
        ip_address = self.ip_input.text()
        system = platform.system()
        if system == "Linux":
            subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
            print("Blocked IP:", ip_address)
        elif system == "Windows":
            subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="BlockIP"', 'dir=in', 'action=block', 'remoteip=' + ip_address])
            print("Blocked IP:", ip_address)
        else:
            print("Unsupported operating system.")
        self.update_iptables()

    def unblock_ip(self):
        ip_address = self.ip_input.text()
        system = platform.system()
        if system == "Linux":
            subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip_address, '-j', 'DROP'])
            print("Unblocked IP:", ip_address)
        elif system == "Windows":
            subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name="BlockIP"', 'dir=in', 'action=block', 'remoteip=' + ip_address])
            print("Unblocked IP:", ip_address)
        else:
            print("Unsupported operating system.")
        self.update_iptables()

    def update_iptables(self):
        system = platform.system()
        if system == "Linux":
            output = subprocess.check_output(['sudo', 'iptables', '-L', '-v', '-n']).decode('utf-8')
            self.rules_text.setText(output)  # Update the text box with the current iptables rules
            print("Current iptables rules (Linux):")
            print(output)
        elif system == "Windows":
            output = subprocess.check_output(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all']).decode('utf-8')
            self.rules_text.setText(output)  # Update the text box with the current firewall rules
            print("Current firewall rules (Windows):")
            print(output)
        else:
            print("Unsupported operating system.")

    def update_ip_list(self):
        self.ip_list.clear()
        connected_ips = self.get_connected_ips()
        self.ip_list.addItems(connected_ips)

if __name__ == "__main__":
    app = QApplication([])
    window = FirewallApp()
    window.update_ip_list()  # Ensure the IP list is updated when the window is shown
    window.update_iptables()  # Ensure the iptables rules are updated when the window is shown
    window.show()
    app.exec_()

