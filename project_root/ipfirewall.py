# from PyQt5 import QtWidgets, uic
# import pandas as pd
# import subprocess

# class FirewallApp(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(FirewallApp, self).__init__()
#         uic.loadUi('firewall.ui', self)

#         # Connect buttons to fcunctions
#         self.forecastButton.clicked.connect(self.show_forecast)

#     def show_forecast(self):
#         # Load the forecasted data
#         forecast_data = pd.read_csv('forecasted_data.csv')

#         # Display the forecast in a table widget
#         self.forecastTable.setRowCount(len(forecast_data))
#         self.forecastTable.setColumnCount(4)
#         self.forecastTable.setHorizontalHeaderLabels(['Date', 'Forecast', 'Lower Bound', 'Upper Bound'])

#         for i, row in forecast_data.iterrows():
#             self.forecastTable.setItem(i, 0, QtWidgets.QTableWidgetItem(row['ds']))
#             self.forecastTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['yhat'])))
#             self.forecastTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['yhat_lower'])))
#             self.forecastTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row['yhat_upper'])))

#         self.forecastTable.resizeColumnsToContents()

#     def automate_ip_blocking(self):
#         forecast_data = pd.read_csv('forecasted_data.csv')
#         threshold = 100  # Define your threshold based on your data

#         for i, row in forecast_data.iterrows():
#             if row['yhat'] > threshold:
#                 # Block IP address (example)
#                 subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', '192.168.67.10', '-j', 'DROP'])
#             else:
#                 # Unblock IP address (example)
#                 subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', '192.168.67.10', '-j', 'DROP'])

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = FirewallApp()
#     window.show()
#     sys.exit(app.exec_())









import pandas as pd
from prophet import Prophet
from PyQt5 import QtWidgets, uic
import subprocess

class FirewallApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FirewallApp, self).__init__()
        uic.loadUi('firewall.ui', self)

        # Connect buttons to functions
        self.forecastButton.clicked.connect(self.show_forecast)

    def show_forecast(self):
        # Load the forecasted data
        forecast_data = pd.read_csv('forecasted_data.csv')

        # Display the forecast in a table widget
        self.forecastTable.setRowCount(len(forecast_data))
        self.forecastTable.setColumnCount(5)  # Added one more column for State
        self.forecastTable.setHorizontalHeaderLabels(['Date', 'Forecast', 'Lower Bound', 'Upper Bound', 'State'])

        for i, row in forecast_data.iterrows():
            ip_address = '192.168.67.10'  # Example IP address
            state = self.check_ip_state(ip_address)  # Check if IP is blocked or unblocked
           
            self.forecastTable.setItem(i, 0, QtWidgets.QTableWidgetItem(row['ds']))
            self.forecastTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['yhat'])))
            self.forecastTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['yhat_lower'])))
            self.forecastTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row['yhat_upper'])))
            self.forecastTable.setItem(i, 4, QtWidgets.QTableWidgetItem(state))

        self.forecastTable.resizeColumnsToContents()

    def check_ip_state(self, ip_address):
        # Example function to check if an IP address is blocked or unblocked
        result = subprocess.run(['sudo', 'iptables', '-C', 'INPUT', '-s', ip_address, '-j', 'DROP'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return 'Blocked'
        else:
            return 'Unblocked'

    def automate_ip_blocking(self):
        forecast_data = pd.read_csv('forecasted_data.csv')
        threshold = 100  # Define your threshold based on your data

        for i, row in forecast_data.iterrows():
            if row['yhat'] > threshold:
                ip_address = '192.168.67.10'  # Example IP address
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
            else:
                ip_address = '192.168.67.10'  # Example IP address
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip_address, '-j', 'DROP'])
           
            # Update state in GUI
            state = self.check_ip_state(ip_address)
            self.update_ip_state_in_table(ip_address, state)

    def update_ip_state_in_table(self, ip_address, state):
        # Update the state of the IP address in the GUI table
        for row in range(self.forecastTable.rowCount()):
            if self.forecastTable.item(row, 0).text() == ip_address:
                self.forecastTable.setItem(row, 4, QtWidgets.QTableWidgetItem(state))
                break

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = FirewallApp()
    window.show()
    sys.exit(app.exec_())
