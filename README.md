# Basic Firewall Simulator with Malicious Bot Detection

## Project Description

Network security is a critical concern, especially with the rising threats posed by malicious bots. Traditional manual methods of monitoring and blocking IP addresses are often inefficient and time-consuming. This project introduces a Basic Firewall Simulator with Malicious Bot Detection, designed to enhance the identification and management of malicious IP addresses.

The simulator, developed using PyQt5 for its user interface, incorporates the Prophet library for forecasting potential threats and machine learning models for advanced bot detection. This combination of tools aims to streamline the detection process, providing network administrators with a flexible and efficient means to manage network security.
## Screenshots

![GUI Interface](https://github.com/Ayshakhan01/Basic-Firewall-Simulator-With-Malicious-Bot-Detection/blob/main/images/image1.png)
![Prediction Interface](https://github.com/Ayshakhan01/Basic-Firewall-Simulator-With-Malicious-Bot-Detection/blob/main/images/image5.png)
![Data Visualization](https://github.com/Ayshakhan01/Basic-Firewall-Simulator-With-Malicious-Bot-Detection/blob/main/images/image2.png)
![Data Visualization](https://github.com/Ayshakhan01/Basic-Firewall-Simulator-With-Malicious-Bot-Detection/blob/main/images/image3.png)
![Bot Detection using Prophet](https://github.com/Ayshakhan01/Basic-Firewall-Simulator-With-Malicious-Bot-Detection/blob/main/images/image4.png)

## Features

- **Network Traffic Monitoring**: Simulate and monitor network traffic to detect potential threats.
- **Manual IP Blocking/Unblocking**: Allow administrators to manually block or unblock IP addresses, ensuring control over network security operations.
- **Forecasting Threats**: Utilize the Prophet library to predict malicious bot activity based on real-world network data.
- **Advanced Bot Detection**: Implement machine learning models to improve the accuracy and efficiency of bot detection and classification.
- **Visualizations**: Provide visualizations for better understanding and response to threats, making it accessible to users with varying technical expertise.

## Installation Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/firewall-simulator.git
    cd firewall-simulator
    ```

2. **Install Python and pip**:
    - Ensure you have Python and pip installed. You can download Python from [python.org](https://www.python.org/downloads/) and pip usually comes bundled with Python.

3. **Create a Virtual Environment (Optional but Recommended)**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:
    - Install the required libraries with the following commands:
    ```sh
    pip install PyQt5
    pip install prophet
    pip install scikit-learn
    pip install pandas
    pip install numpy
    ```

5. **Run the Simulator**:
    ```sh
    cd GUI-Firewall-for-Windows-and-Linux--main
    sudo python3 ipfirewalls.py
    ```

## Usage

1. **Configure Rules**:
    - Edit the `config/rules.json` file to add or modify detection rules.

2. **Start the Simulator**:
    - Run the simulator and interact with the PyQt5 user interface to monitor network traffic and manage IP addresses.

3. **Review Logs**:
    - Check the `logs` directory for detailed logs of detected bots and blocked traffic.

4. **Visualizations**:
    - Use the built-in visualizations to understand and respond to detected threats effectively.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please submit a pull request or open an issue.

## Acknowledgements

- Inspired by the need for better understanding and practical demonstration of network security concepts.
- Thanks to all contributors and users for their support and feedback.

